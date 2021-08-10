import database
import main
import datetime
from functions import get_arancel_data, generate_month, days_between_two_dates, get_arancel_subject_data, get_id_old_variable, get_arancel_discount


class ArancelNI:
    def __init__(self):
        self.period_id = None
        self.campus = None
        self.campus_old = None
        self.shift = None
        self.shift_old = None
        self.inscription_student = None
        self.q_subjects = 0
        self.q_subjects_sp = 0
        self._campus_ = None

    def get_r(self, period_id):

        if self.campus_old[0][0] == '1':
            self._campus_ = SM()
        else:
            self._campus_ = PJC()
        self.set_data(period_id=period_id)
        self._campus_.period_id = period_id
        return self._campus_.get_r(number_of_subjects=self.q_subjects, number_of_subjects_sp=self.q_subjects_sp)

    def set_data(self, period_id):
        data = get_arancel_data(period_id=period_id)
        self._campus_.arancel_data = data
        self._campus_.subjects = self.subjects
        _discount_ = None
        '''1 Matricula
            2 Cuota
            3 Materia(s)'''
        for k in data:
            if k['idconcepto'] == 1:
                self._campus_.matriculation = k['monto']
                self._campus_.matriculation_adm = k['montogastoadm']
            if k['idconcepto'] == 2:
                self._campus_.set_p(k['idarancel'])
                self._campus_.CN = k['monto']
                self._campus_.fee_adm = k['montogastoadm']
            if k['idconcepto'] == 3:
                self._campus_.M = k['monto']
                self._campus_.set_d(k['idarancel'])
                self._campus_._arancel_subject_data_ = get_arancel_subject_data(k['idarancel'])
                self._campus_.subject_adm = k['montogastoadm']


class Arancel:
    def __init__(self, id_student):
        self.student = id_student
        self.period_id = None
        self.campus = None
        self.campus_old = None
        self.shift = None
        self.shift_old = None
        self.inscription_student = None
        self.q_subjects = 0
        self.q_subjects_sp = 0
        self._campus_ = None

    def get_subjects_data(self):
        """SELECT periods_details.subject_id,
        periods_details.type_subject_id,
        periods_details.validity_date_start,
        periods_details.validity_date_end
        FROM periods_details
        WHERE periods_details.period_id::text = (SELECT inscriptions_students.period_id
        FROM inscriptions_students WHERE inscriptions_students.student_id = 'a14cb8e2-95ce-4bcb-9dca-448c84fc5eb5')"""

        # 1234 Normal
        # 4567 Auxiliar

    def get_student_data(self):
        try:
            _cursor_ = database.engine.execute("""SELECT inscriptions_students.student_id, 
            inscriptions_students.study_plans_id, inscriptions_students.period_id, inscriptions_students.id_new, 
            inscriptions_students.careers_segmentation_groups_detail_id, inscriptions_students.shift_id, 
            study_plans.campus_id, (SELECT COUNT(*) FROM inscriptions_students_subjects WHERE 
            inscriptions_students_subjects.inscription_student_id::text = inscriptions_students.id_new::text) as 
            q_subjects, (SELECT COUNT(*) FROM study_plans_detail WHERE 
            study_plans_detail.study_plans_id::text = inscriptions_students.study_plans_id::text) as q_subjects_sp  
            FROM inscriptions_students INNER JOIN study_plans ON study_plans.id_new::text = 
            study_plans_id WHERE inscriptions_students.student_id = %s ORDER BY inscriptions_students.date DESC LIMIT 
            1;""", self.student)
            for row in _cursor_:
                self.period_id = row['period_id']
                self.campus = row['campus_id']
                self.campus_old = main.get_id_old_variable('campus', row['campus_id'])
                self.shift = row['shift_id']
                self.shift_old = main.get_shift(row['shift_id'])
                self.inscription_student = row['id_new']
                self.q_subjects = row['q_subjects']
                self.q_subjects_sp = row['q_subjects_sp']
            return True, _cursor_
        except Exception as ex:
            return False, str(ex)

    def get_detail_amount(self):
        return {
            'additional': self._campus_.get_additional(),
            'r1': self._campus_.get_r1(),
            'r2': self._campus_.get_r2()
        }

    def get_r(self):
        if self.campus_old[0][0] == '1':
            self._campus_ = SM()
        else:
            self._campus_ = PJC()
        return self._campus_.get_r(number_of_subjects=self.q_subjects, number_of_subjects_sp=self.q_subjects_sp)


'''
C = Costo de la Cuota normal mes vencido
P = Descuento del Pronto Pago del 1 al 5 correspondiente a la cuota
M = Costo Unitario del Monto por 1 materia mes vencido
D = Descuento del Pronto pago del 1 al 5 por 1 materia. 
CM = Cantidad de Asignaturas  

Formula
Aplicando la siguiente fórmula siendo R1 el resultado 1 y R2 el resultado 2: 
R1 = C – P       
R2 = (M * CM) – (D * CM) 
Se toma en cuenta el resultado de la siguiente comparativa.
Si R2 > R1 = Costo por Cuota
Si R2<= R1 = Costo por materia normal.
'''


class PJC:

    def __init__(self):
        self.CN = 5000000
        self.P = self.get_p()
        self.M = 750000
        self.D = self.get_d()
        self.number_of_subjects = 0
        self.number_of_subjects_sp = 0

    def set_p(self, id_arancel):
        _day_ = datetime.datetime.today().day
        cursor = database.execute_raw_sql_bancard(f"SELECT * FROM aranceldescuento inner JOIN descuentopago ON "
                                                  f"descuentopago.iddescuentopago = aranceldescuento.iddescuentopago "
                                                  f"WHERE aranceldescuento.IDARANCEL = {id_arancel} and (descuentopago.desde "
                                                  f"<= {_day_} and descuentopago.hasta >= {_day_})")
        data = [row for row in cursor]
        if len(data) > 0:
            self.P = data[0]['monto']

    def set_d(self, id_arancel):
        _day_ = datetime.datetime.today().day
        cursor = database.execute_raw_sql_bancard(f"SELECT * FROM aranceldescuento inner JOIN descuentopago ON "
                                                  f"descuentopago.iddescuentopago = aranceldescuento.iddescuentopago "
                                                  f"WHERE aranceldescuento.IDARANCEL = {id_arancel} and (descuentopago.desde "
                                                  f"<= {_day_} and descuentopago.hasta >= {_day_})")
        data = [row for row in cursor]
        if len(data) > 0:
            self.D = data[0]['monto']

    def get_additional(self):
        """A = Total de Adicionales
        TA = Total de Asignaturas en las que el estudiante desea inscribirse.
        CA  = Cantidad de asignaturas que puede cursar según su curso, semestre y turno mayor.
         A = TA – CA
        A = 8 – 6 = 2 materia adiciona a su inscripción.
        """
        if self.number_of_subjects > self.number_of_subjects_sp:
            return (self.number_of_subjects - self.number_of_subjects_sp) * self.M
        return 0

    def get_r1(self):
        return self.CN - self.P

    def get_r2(self):
        return (self.M * self.number_of_subjects) - (self.D * self.number_of_subjects)

    def get_r(self, number_of_subjects, number_of_subjects_sp):
        self.number_of_subjects = number_of_subjects
        self.number_of_subjects_sp = number_of_subjects_sp
        r2 = self.get_r2()
        r1 = self.get_r1() + self.get_additional()
        return r2 if r2 > r1 else r1


class SM:
    def __init__(self):
        self.CN = 0
        self.P = 0
        self.M = 0
        self.D = 0
        self.matriculation = 0
        self.subject_adm = 0
        self.fee_adm = 0
        self.number_of_subjects = 0
        self.number_of_subjects_sp = 0
        self.period_id = None
        self.subjects = {}
        self._arancel_subject_data_ = {}

    def set_p(self, id_arancel):
        _day_ = datetime.datetime.today().day
        cursor = database.execute_raw_sql_bancard(f"SELECT * FROM aranceldescuento inner JOIN descuentopago ON "
                                                  f"descuentopago.iddescuentopago = aranceldescuento.iddescuentopago "
                                                  f"WHERE aranceldescuento.IDARANCEL = {id_arancel} and (descuentopago.desde "
                                                  f"<= {_day_} and descuentopago.hasta >= {_day_})")
        data = [row for row in cursor]
        if len(data) > 0:
            self.P = data[0]['monto']

    def get_d(self, id_arancel):
        _day_ = datetime.datetime.today().day
        cursor = database.execute_raw_sql_bancard(f"SELECT * FROM aranceldescuento inner JOIN descuentopago ON "
                                                  f"descuentopago.iddescuentopago = aranceldescuento.iddescuentopago "
                                                  f"WHERE aranceldescuento.IDARANCEL = {id_arancel} and (descuentopago.desde "
                                                  f"<= {_day_} and descuentopago.hasta >= {_day_})")
        data = [row for row in cursor]
        print('*********************')
        print(data)
        print('*********************')
        if len(data) > 0:
            self.D = data[0]['monto']

    def set_d(self, id_arancel):
        _day_ = datetime.datetime.today().day
        cursor = database.execute_raw_sql_bancard(f"SELECT * FROM aranceldescuento inner JOIN descuentopago ON "
                                                  f"descuentopago.iddescuentopago = aranceldescuento.iddescuentopago "
                                                  f"WHERE aranceldescuento.IDARANCEL = {id_arancel} and (descuentopago.desde "
                                                  f"<= {_day_} and descuentopago.hasta >= {_day_})")
        data = [row for row in cursor]
        if len(data) > 0:
            self.D = data[0]['monto']

    def get_r1(self):
        return self.CN - self.P

    def get_r2(self):
        _relation_str_ = {}
        _total_ = 0
        _total_discount_ = 0
        for k in self._arancel_subject_data_:
            discount = get_arancel_discount(k['idarancel'], None)
            _relation_str_[k['idtipomateria']] = {"description": k['descripcion'], "amount": k['monto'],
                                                  'adm_fee': k['montogastoadm'],
                                                  'discount': discount}
            if k['idtipomateria'] == 1:
                self.M = k['monto']

        _total_ = 0
        for j, v in self.subjects.items():
            _id_ = int(get_id_old_variable('types_subjects', v))
            _total_ += _relation_str_[_id_]['amount']

        return _total_

    def get_subjects_fee(self, date):
        _relation_str_ = {}
        _total_ = 0
        _total_discount_ = 0
        _total_adm_fee_ = 0
        for k in self._arancel_subject_data_:
            discount = get_arancel_discount(k['idarancel'], date)
            _relation_str_[k['idtipomateria']] = {
                "description": k['descripcion'],
                "amount": k['monto'],
                'adm_fee': k['montogastoadm'],
                'discount': discount
                }
            if k['idtipomateria'] == 1:
                self.M = k['monto']

        for j, v in self.subjects.items():
            _id_ = int(get_id_old_variable('types_subjects', v))
            _total_ += _relation_str_[_id_]['amount']
            if date.month < datetime.datetime.today().month:
                _days_ = days_between_two_dates(datetime.datetime.today(), date)
                _total_adm_fee_ += (_relation_str_[_id_]['adm_fee'] * _days_)
            _total_discount_ += _relation_str_[_id_]['discount']

        return [_total_ - _total_discount_ + _total_adm_fee_, _total_discount_, _total_adm_fee_]

    def get_additional(self):
        """A = Total de Adicionales
        TA = Total de Asignaturas en las que el estudiante desea inscribirse.
        CA  = Cantidad de asignaturas que puede cursar según su curso, semestre y turno mayor.
         A = TA – CA
        A = 8 – 6 = 2 materia adiciona a su inscripción.
        """
        if self.number_of_subjects > self.number_of_subjects_sp:
            return (self.number_of_subjects - self.number_of_subjects_sp) * self.M
        return 0

    def get_r(self, number_of_subjects, number_of_subjects_sp):
        self.number_of_subjects = number_of_subjects
        self.number_of_subjects_sp = number_of_subjects_sp
        r2 = self.get_r2()
        r1 = self.get_r1() + self.get_additional()
        r_final = r2 if r2 > r1 else r1
        _month_ = generate_month(self.period_id)
        _days_ = days_between_two_dates(datetime.datetime.today(), datetime.datetime.strptime(_month_[1][0], "%Y-%m-%d"))
        r_total = [{"concept": f"Matrícula {_month_[0][0]}", "amount": self.matriculation,
                    "expiration_date": _month_[1][0],
                    "fee_number": 1,
                    "administrative_fee": 0,
                    "expiration_amount": self.matriculation}]

        count_ = 1
        for i in _month_[0]:
            _days_ = 0
            if datetime.datetime.today().month > datetime.datetime.strptime(_month_[1][count_-1], "%Y-%m-%d").month:
                _days_ = days_between_two_dates(datetime.datetime.today(),
                                                datetime.datetime.strptime(_month_[1][count_ - 1], "%Y-%m-%d"))
            if r2 > r1:

                _t_ = self.get_subjects_fee(datetime.datetime.strptime(_month_[1][count_ - 1], "%Y-%m-%d"))
                r_total.append({
                    "concept": f"Cuota {i}",
                    "amount": r_final,
                    "expiration_date": _month_[1][count_ - 1],
                    "fee_number": count_,
                    "discount": _t_[1],
                    "administrative_fee": _t_[2],
                    "expiration_amount": _t_[0]
                })
            else:
                r_total.append({
                                   "concept": f"Cuota {i}",
                                   "amount": self.CN,
                                   "expiration_date": _month_[1][count_ - 1],
                                   "fee_number": count_,
                                   "discount": self.P if _days_ == 0 else 0,
                                   "administrative_fee": self.fee_adm * _days_,
                                   "expiration_amount": (r_final if _days_ == 0 else r_final + self.P) + (self.fee_adm * _days_)
                                   })

            count_ += 1
        return r_total
