from functions import get_id_old, get_id_old_variable, get_career_segmentation, get_shift, get_cant_subjects_on_study_plan
from fake_databases import _indexes_, _tables_, _pk_
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import Json
from sedes import Arancel, ArancelNI

import database

app = FastAPI()
ERROR_MISSING_PARAMETER = 1
ERROR_INVALID_PARAMETER = 2
ERROR_INTERNAL = 3
ERROR_NOT_FOUND = 4


@app.get('/data')
def get_test_data(table_name: str = None):
    inspector = database.get_inspector()
    _tables__ = {}
    tables = _tables_
    if table_name is not None:
        tables = {
            table_name: _tables_[table_name]
        }
    for table_name, equivalent in tables.items():
        _tables__[table_name] = {}
        _registers_ = database.get_registers(table_name=table_name)
        if len(_registers_) > 0:
            for register, data in _registers_.items():
                _tables__[table_name][register] = {}
                _count_ = 0
                print(inspector.get_columns(table_name))
                for column in inspector.get_columns(table_name):
                    _tables__[table_name][register][column['name']] = data[_count_]
                    _count_ += 1
                try:
                    if 'id' in _tables__[table_name][register]:
                        del _tables__[table_name][register]['id']
                    if 'active' in _tables__[table_name][register]:
                        del _tables__[table_name][register]['active']
                    #  if 'id_old' in _tables__[table_name][register]:
                    #    del _tables__[table_name][register]['id_old']
                    if 'migrate' in _tables__[table_name][register]:
                        del _tables__[table_name][register]['migrate']
                    if 'archived' in _tables__[table_name][register]:
                        del _tables__[table_name][register]['archived']
                except Exception as ex:
                    print(ex)
                    pass
    return JSONResponse(status_code=200, content=_tables__)


@app.get('/update')
def update_(operation_type: str = None, data: Optional[Json] = Query({})):
    if operation_type is None:
        return JSONResponse(status_code=403,
                            content={
                                'error': True,
                                'message': 'MissingParameters: operation_type not found.',
                                'code': ERROR_MISSING_PARAMETER
                            })

    if list(data.keys())[0] not in _tables_:
        return JSONResponse(status_code=400,
                            content={
                                'error': True,
                                'message': f'InvalidParameters: La tabla {list(data.keys())[0]} no es valida.',
                                'code': ERROR_INVALID_PARAMETER
                            })
    table = list(data.keys())[0]

    _query_ = ''
    if operation_type == 'insert':
        sql_insert = """INSERT INTO {}({}) VALUES({})"""
        _tab_idx_ = ''
        _values_ = ''
        try:
            if 'id' in data:
                del data['id']
            if 'id_old' in data:
                del data['id_old']
            if 'id_new' in data:
                del data['id_new']
            if 'active' in data:
                del data['active']
            if 'archived' in data:
                del data['archived']
            if 'type_planning_id' in data:
                del data['type_planning_id']
        except:
            pass
        for key, value in data[table].items():
            if _indexes_[table][key] != '':
                _old_ = get_id_old(table, key, value)
                if isinstance(_indexes_[table][key], dict):
                    if _old_ is False:
                        return JSONResponse(status_code=404, content={
                            'error': True,
                            'message': f'InvalidParameters: id_old not found for {key} on table {key}.',
                            'code': ERROR_NOT_FOUND
                        }
                                            )
                if _old_:
                    _index_ = list(_indexes_[table][key].keys())[0]
                    __index = list(_indexes_[table][key][_index_].values())[0]
                    if "exception" in list(_indexes_[table][key][_index_].keys()):
                        __index = _indexes_[table][key][_index_]['id_old']
                    if str(_old_).isdecimal():
                        _tab_idx_ += f"{_tables_[table]}.{__index}, "
                        _values_ += f"{_old_},"
                    else:
                        _tab_idx_ += f"{_tables_[table]}.{__index}, "
                        _values_ += f"'{_old_}',"
                else:
                    if value is None:
                        _tab_idx_ += f"{_tables_[table]}.{_indexes_[table][key]}, "
                        _values_ += f"null,"
                    else:
                        if value.isdecimal():
                            _tab_idx_ += f"{_tables_[table]}.{_indexes_[table][key]}, "
                            _values_ += f"{value},"
                        else:
                            _tab_idx_ += f"{_tables_[table]}.{_indexes_[table][key]}, "
                            _values_ += f"'{value}',"

        _query_ = sql_insert.format(f"{_tables_[table]}", f"{_tab_idx_[:-2]}", f"{_values_[:-1]}")
    elif operation_type == 'update':
        id_ = data[table]['id_new']
        try:
            if 'id' in data:
                del data['id']
            if 'id_old' in data:
                del data['id_old']
            if 'id_new' in data:
                del data['id_new']
            if 'active' in data:
                del data['active']
            if 'archived' in data:
                del data['archived']
            if 'type_planning_id' in data:
                del data['type_planning_id']
        except:
            pass
        print(id_, table)
        _id_old_ = get_id_old_variable(table, id_)
        sql_update = """UPDATE {} set {} WHERE {}"""
        if _id_old_ is False:
            return JSONResponse(status_code=404, content={
                'error': True,
                'message': f'InvalidParameters: id_old not found for {id_} on table {table}',
                'code': ERROR_NOT_FOUND
            }
                                )
        _changes_ = ''
        for key, value in data[table].items():
            if _indexes_[table][key] != '':
                _old_ = get_id_old(table, key, value)
                if isinstance(_indexes_[table][key], dict):
                    # if 'exception' not in _indexes_[table][key][list(_indexes_[table][key])[0]]:
                    if _old_ is False:
                        return JSONResponse(status_code=404, content={
                            'error': True,
                            'message': f'InvalidParameters: id_old not found for {key} on table {key}.',
                            'code': 5
                        }
                                            )
                if _old_:
                    _index_ = list(_indexes_[table][key].keys())[0]
                    __index = list(_indexes_[table][key][_index_].values())[0]
                    if "exception" in list(_indexes_[table][key][_index_].keys()):
                        __index = _indexes_[table][key][_index_]['id_old']
                    print(__index, "=", _old_)
                    if str(_old_).isdecimal():
                        _changes_ += f"{_tables_[table]}.{__index} = {_old_},"
                    else:
                        _changes_ += f"{_tables_[table]}.{__index} = '{_old_}',"
                else:
                    print(_indexes_[table][key], "=", value)
                    if value is None:
                        _changes_ += f"{_tables_[table]}.{_indexes_[table][key]} = null,"
                    else:
                        if value.isdecimal():
                            _changes_ += f"{_tables_[table]}.{_indexes_[table][key]} = {value},"
                        else:
                            _changes_ += f"{_tables_[table]}.{_indexes_[table][key]} = '{value}',"
        _query_ = sql_update.format(f"{_tables_[table]}", f"{_changes_[:-1]}",
                                    f"{_tables_[table]}.{_pk_[table]} = {_id_old_}")
    elif operation_type == 'delete':
        sql_delete = """DELETE FROM {} WHERE {}"""
        id_ = data[table]['id_new']
        _id_old_ = get_id_old_variable(table, id_)
        _query_ = sql_delete.format(f"{_tables_[table]}", f"{_tables_[table]}.{_pk_[table]} = {_id_old_}")
    else:
        return JSONResponse(status_code=400,
                            content={
                                'error': True,
                                'message': 'InvalidParameters: operation type must be insert, update or delete '
                                           'only',
                                'code': ERROR_INVALID_PARAMETER
                            })
    try:
        print(_query_)
        database.execute_raw_sql_bancard(_query_.replace('\n', ''))
    except Exception as ex:
        return JSONResponse(status_code=500, content={
            'error': True,
            'message': str(ex),
            "query": _query_
        })
    return JSONResponse(status_code=200, content={
        'error': False,
        'message': 'All right!',
        "query": _query_
    })


@app.get('/update_periods')
def update_(operation_type: str = None, id_: str = None, data: Json = Query(None)):
    if operation_type is None:
        return JSONResponse(status_code=403,
                            content={
                                'error': True,
                                'message': 'MissingParameters operation_type not found.',
                                'code': ERROR_MISSING_PARAMETER
                            })

    if id_ is None:
        return JSONResponse(status_code=403,
                            content={
                                'error': True,
                                'message': 'MissingParameters: id can\'t be None',
                                'code': ERROR_MISSING_PARAMETER
                            })
    if data is None:
        return JSONResponse(status_code=403,
                            content={
                                'error': True,
                                'message': 'MissingParameters: data can\'t be None',
                                'code': ERROR_MISSING_PARAMETER
                            })
    _query_ = ''
    if operation_type == 'insert':
        _variables_ = {}
        try:
            if 'id' in data:
                del data['id']
            if 'id_old' in data:
                del data['id_old']
            if 'id_new' in data:
                del data['id_new']
            if 'active' in data:
                del data['active']
            if 'archived' in data:
                del data['archived']
            if 'type_planning_id' in data:
                del data['type_planning_id']
        except:
            pass
        for key, value in data.items():
            if key != 'career_segmentation_groups_detail_id' and key != 'shift_id':
                _id_old_ = get_id_old('periods', key, value)
                if _id_old_:
                    _variables_[key] = _id_old_
                else:
                    _variables_[key] = value
        # career segmentation
        _segmentation_ = list(get_career_segmentation(data['career_segmentation_groups_detail_id']))
        _variables_['course'] = _segmentation_[0]
        _variables_['semester'] = _segmentation_[1]
        _variables_['raw'] = _segmentation_[2]

        # shift
        _variables_['shift'] = get_shift(data['shift_id'])
        # Query generation
        _cursor_ = database.engine.execute("""SELECT id_old FROM periods WHERE id_new = %s""", (id_,))
        data_ = [row for row in _cursor_]
        _id_ = data_[0][0]
        _id_old_ = _id_[list(_id_.keys())[0]]
        _set_ = ''
        for key, value in _variables_.items():
            _set_ += f"'{value}', "
        _set_ += f"'{id_}'"
        _query_ = f"""INSERT INTO PERIODS_CLONE(PERIODS_CLONE.campus_id, PERIODS_CLONE.career_id, 
        PERIODS_CLONE.study_plans_id, PERIODS_CLONE.academic_date_start, PERIODS_CLONE.academic_date_end, 
        PERIODS_CLONE.inscription_date_start, PERIODS_CLONE.inscription_date_end, PERIODS_CLONE."YEAR", 
        PERIODS_CLONE.course, PERIODS_CLONE.semester, PERIODS_CLONE.raw, PERIODS_CLONE.shift, 
        PERIODS_CLONE.id_new_system) VALUES({_set_}); """
        print('*************************')
        _query_ = _query_.replace('\n', '').replace('        ', '')
        print(_query_)
        print('*************************')
        try:
            _query__ = database.engine_B.execute(_query_)
        except Exception as ex:
            print(ex)
            return JSONResponse(status_code=500,
                                content={
                                    'error': True,
                                    'message': f'HOST ERROR:{ex}',
                                    'code': ERROR_INTERNAL
                                })
    elif operation_type == 'update':
        _variables_ = {}
        try:
            if 'id' in data:
                del data['id']
            if 'id_old' in data:
                del data['id_old']
            if 'id_new' in data:
                del data['id_new']
            if 'active' in data:
                del data['active']
            if 'archived' in data:
                del data['archived']
            if 'type_planning_id' in data:
                del data['type_planning_id']
        except:
            pass
        for key, value in data.items():
            if key != 'career_segmentation_groups_detail_id' and key != 'shift_id':
                _id_old_ = get_id_old('periods', key, value)
                if _id_old_:
                    _variables_[key] = _id_old_
                else:
                    _variables_[key] = value
        # career segmentation
        _segmentation_ = list(get_career_segmentation(data['career_segmentation_groups_detail_id']))
        _variables_['course'] = _segmentation_[0]
        _variables_['semester'] = _segmentation_[1]
        _variables_['raw'] = _segmentation_[2]

        # shift
        _variables_['shift'] = get_shift(data['shift_id'])
        # Query generation
        _cursor_ = database.engine.execute("""SELECT id_old FROM periods WHERE id_new = %s""", (id_,))
        data_ = [row for row in _cursor_]
        _id_ = data_[0][0]
        _id_old_ = _id_[list(_id_.keys())[0]]
        _set_ = ''
        for key, value in _variables_.items():
            if key == "year":
                _set_ += f"""PERIODS_CLONE."YEAR" = '{value}',"""
            else:
                _set_ += f"PERIODS_CLONE.{key} = '{value}',"
        _query_ = f"""UPDATE PERIODS_CLONE set {_set_[:-1]} WHERE PERIODS_CLONE.id_new_system = '{id_}';"""
        print(_query_)
        try:
            _query__ = database.engine_B.execute(_query_)
        except Exception as ex:
            print(ex)
            return JSONResponse(status_code=500,
                                content={
                                    'error': True,
                                    'message': f'HOST ERROR:{ex}',
                                    'code': ERROR_INTERNAL
                                })
    elif operation_type == 'delete':
        try:
            _query_ = f"""DELETE FROM PERIODS_CLONE WHERE PERIODS_CLONE.id_new_system = '{id_}'"""
            print(_query_)
            _query__ = database.engine_B.execute(_query_)
        except Exception as ex:
            return JSONResponse(status_code=500,
                                content={
                                    'error': True,
                                    'message': ex,
                                    'code': ERROR_INTERNAL
                                })
    else:
        return JSONResponse(status_code=405,
                            content={
                                'error': True,
                                'message': 'Method Not Allowed: operation type must be insert, update or delete '
                                           'only',
                                'code': ERROR_INVALID_PARAMETER
                            })
    return JSONResponse(status_code=200, content={
        'error': False,
        'message': 'All right!',
        "query": _query_
    })


@app.get('/arancel')
def get_arancel(id_student: str = None):
    if id_student is None:
        return JSONResponse(status_code=403,
                            content={
                                'error': True,
                                'message': 'MissingParameters',
                                'code': ERROR_MISSING_PARAMETER
                            })
    else:
        try:
            _arancel_ = Arancel(id_student=id_student)
            _data_ = _arancel_.get_student_data()
            if _data_[0]:
                value = _arancel_.get_r()
                return JSONResponse(status_code=200, content={
                    'error': False,
                    'amount': value,
                    'detail': _arancel_.get_detail_amount()
                })
        except Exception as ex:
            print(ex)
            return JSONResponse(status_code=500, content={
                'error': True,
                'message': str(ex)
            })


@app.get('/arancel_ni')
def get_arancel(data: Json = Query(None)):
    if data is None:
        return JSONResponse(status_code=403,
                            content={
                                'error': True,
                                'message': 'MissingParameters',
                                'code': ERROR_MISSING_PARAMETER
                            })
    else:
        try:
            # 12582, 7650714a-a169-47d9-bbc9-67318e0bed2c,
            _data_ = ArancelNI()
            _data_.campus_old = get_id_old_variable('campus', data['campus'])
            _data_.shift_old = get_shift(data['shift'])
            _data_.q_subjects_sp = get_cant_subjects_on_study_plan(data['study_plan'])
            _data_.q_subjects = len(data['subjects'].keys())
            _data_.subjects = data['subjects']
            r = _data_.get_r(data['period_id'])
            return JSONResponse(status_code=200, content={"total": r})
        except Exception as ex:
            print(ex)
            return JSONResponse(status_code=500, content={
                'error': True,
                'message': str(ex)
            })
