import datetime
import locale
from fake_databases import _tables_, _indexes_, _pk_
from datetime import datetime, timedelta
from collections import OrderedDict

import database


def transform_date(_date_: str, return_date: bool = False):
    _date_array_ = _date_.split('.')
    if not return_date:
        return f'{_date_array_[2]}-{_date_array_[1]}-{_date_array_[0]}'
    else:
        return datetime.datetime.strptime(_date_, '%d.%m.%Y')


def get_id_old(table, index_, value_):
    if table in _tables_:
        if index_ in _indexes_[table]:
            if _indexes_[table][index_] != '' and isinstance(_indexes_[table][index_], dict):
                if 'exception' not in _indexes_[table][index_]:
                    try:
                        _index_ = list(_indexes_[table][index_].keys())[0]
                        _cursor_ = database.engine.execute(f"""SELECT id_old FROM {_index_} WHERE id_new::text = %s""",
                                                           (value_,))
                        data_ = [row for row in _cursor_]
                        _id_ = data_[0][0]
                    except Exception as ex:
                        print(ex)
                        return False
                    return _id_[list(_id_.keys())[0]]
                else:
                    try:
                        _index_ = list(_indexes_[table][index_].keys())[0]
                        _cursor_ = database.engine.execute(f"""SELECT id_old FROM {_index_} WHERE id_new::text = %s""",
                                                           (value_,))
                        data_ = [row for row in _cursor_]
                        _id_ = data_[0][_indexes_[table][index_]['id_old']]
                    except Exception as ex:
                        print(ex)
                        return False
                    return _id_
    return False


def get_id_old_variable(table, id_):
    if table in _tables_:
        try:
            _cursor_ = database.engine.execute(f"""SELECT id_old FROM {table} WHERE id_new::text = %s""", (id_,))
            data_ = [row for row in _cursor_]
            _id_ = data_[0][0]
            return _id_[list(_id_.keys())[0]]
        except Exception as ex:
            print("Error:", ex)
            return False
    return False


def get_arancel_discount(id_arancel, date=None):
    _day_ = datetime.today().day
    if date is not None:
        if isinstance(date, datetime):
            _month_ = date.month
            _month_actual_ = datetime.today().month
            if _month_ > _month_actual_:
                _day_ = 1
    cursor = database.execute_raw_sql_bancard(f"SELECT * FROM aranceldescuento inner JOIN descuentopago ON "
                                              f"descuentopago.iddescuentopago = aranceldescuento.iddescuentopago "
                                              f"WHERE aranceldescuento.IDARANCEL = {id_arancel} and (descuentopago.desde "
                                              f"<= {_day_} and descuentopago.hasta >= {_day_})")
    data = [row for row in cursor]
    if len(data) > 0:
        return data[0]['monto']
    return 0


def get_career_segmentation(id_):
    _cursor_ = database.engine.execute(f"""SELECT value1, value2, raw FROM 
    careers_segmentation_groups_details WHERE id_new::text = %s""", (id_,))
    data_ = [row for row in _cursor_]
    return data_[0]


def generate_month(period_id):
    cursor = database.execute_raw_sql_bancard(f"SELECT ACADEMIC_DATE_START, ACADEMIC_DATE_END FROM PERIODS_CLONE "
                                              f"WHERE ID_NEW_SYSTEM = '{period_id}'")
    _cursor_keys_ = cursor.keys()
    data = [row for row in cursor]
    locale.setlocale(locale.LC_TIME, 'es_ES')
    _start_ = datetime.strptime(str(data[0]['academic_date_start']), "%Y-%m-%d")
    _end_ = datetime.strptime(str(data[0]['academic_date_end']), "%Y-%m-%d")
    _month_ = OrderedDict(
        ((_start_ + timedelta(_)).strftime(r"%b, %Y"), None) for _ in range((_end_ - _start_).days)).keys()
    _month_real_ = OrderedDict(((_start_ + timedelta(_)), None) for _ in range((_end_ - _start_).days)).keys()
    _month_expiration_date_ = []
    for v in _month_real_:
        if v.day == 1:
            _month_expiration_date_.append(str(v)[0:10])
    _month_ = [str(_).capitalize() for _ in _month_]
    return [_month_, _month_expiration_date_]


def days_between_two_dates(data_1, data_2):
    if data_2 > data_1:
        return 0
    delta = data_1 - data_2
    return delta.days


def get_shift(id_):
    _cursor_ = database.engine.execute(f"""SELECT description FROM 
    shifts WHERE id_new::text = %s""", (id_,))
    data_ = [row for row in _cursor_]
    return data_[0][0][0]


def get_cant_subjects_on_study_plan(study_plan_id):
    cursor = database.engine.execute("SELECT COUNT(*) as cant FROM study_plans_detail WHERE study_plans_id::text = %s",
                                     (study_plan_id,))
    data = [row for row in cursor]
    return data[0][0]


def get_arancel_data(period_id):
    cursor = database.execute_raw_sql_bancard(f"SELECT * FROM ARANCEL INNER JOIN CONCEPTO ON concepto.idconcepto = "
                                              f"arancel.idconcepto WHERE ARANCEL.IDPERIODS_CLONE = (SELECT "
                                              f"IDPERIODS_CLONE FROM PERIODS_CLONE WHERE ID_NEW_SYSTEM = '"
                                              f"{period_id}')")
    _cursor_keys_ = cursor.keys()
    data = []
    for row in cursor:
        _row_ = {}
        for key in _cursor_keys_:
            _row_[key] = row[key]
        data.append(_row_)
    return data


def get_arancel_subject_data(arancel_id):
    cursor = database.execute_raw_sql_bancard(f"SELECT * FROM ARANCELMATERIA INNER JOIN TIPOMATERIA ON "
                                              f"TIPOMATERIA.IDTIPOMATERIA = ARANCELMATERIA.IDTIPOMATERIA WHERE "
                                              f"IDARANCEL  = {arancel_id} and CANTIDAD = 1")
    _cursor_keys_ = cursor.keys()
    data = []
    for row in cursor:
        _row_ = {}
        for key in _cursor_keys_:
            _row_[key] = row[key]
        data.append(_row_)
    return data


def pretty(d, indent=0):
    for key, value in d.items():
        print('  ' * indent + '"' + str(key) + '": {')
        if isinstance(value, dict):
            pretty(value, indent + 1)
        else:
            print('  ' * (indent + 1) + '"' + str(value) + '"')
        print('  ' * indent + '}')
