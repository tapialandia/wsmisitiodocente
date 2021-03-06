# study_plans_detail, logs, prerequisites
_tables_ = {
            'careers': 'CARRERA',
            'colleges': 'FACULTAD',
            'persons': 'PERSONA',
            'campus': 'SEDE',
            'students': 'ALUMNO',
            'study_plans': 'MALLACURRICULAR',
            'schools': 'N2016_COLEGIO',
            'periods': '',
            'types_subjects': '',
            'subjects': 'MATERIA',
            'teachers': 'DOCENTE'
            }
_pk_ = {
    'careers': 'IDCARRERA',
    'colleges': 'IDFACULTAD',
    'persons': 'IDPERSONA',
    'campus': 'IDSEDE',
    'students': 'IDALUMNO',
    'study_plans': 'IDMALLA',
    'schools': 'IDCOLEGIO',
    'subjects': 'IDMATERIA',
    'teachers': 'IDDOCENTE'
}

_indexes_ = {
             'persons': {'id': '',
                         'id_old': '',
                         'id_new': '',
                         'type_document_id': {'types_documents': {'exception': True, 'id_old': 'TIPODOC'}},
                         'document_number': 'CINRO',
                         'first_name': 'NOMBRE',
                         'last_name': 'APELLIDO',
                         'nationality_id': {'countries': {'PAIS': 'IDPAIS'}},
                         'birthdate': 'FECHANAC',
                         'mobile': 'TELEFPARTICULAR',
                         'email': 'EMAIL',
                         'civil_status_id': {'civil_states': {'exception': True, 'id_old': 'ESTADOCIVIL'}},
                         'sex_id': {'sexes': {'exception': True, 'id_old': 'SEXO'}},
                         'city_id': '',
                         'address': 'DIRECCION'},
             'students':  {'id': '', 'id_old': '', 'id_new': '',
                           'person_id': {'persons': {'PERSONA': 'IDPERSONA'}},
                           'student_number': '', 'school_id': {'schools': {'COLEGIO': 'IDCERTESTUDCOLEGIO2'}},
                           'school_title_id': {'titles': {'TITULO': 'IDTITULO'}},
                           'school_end_year': 'PERIODOLECTIVO',
                           'university_id': {'universities': {'UNIVERSIDAD': 'IDCERTESTUDUNIVERS'}},
                           'university_title_id': 'IDTITULOUNIV',
                           'university_end_year': '',
                           'workplace': 'LUGARTRABAJO',
                           'father_name': 'NOMAPEPADRE',
                           'mother_name': 'NOMAPEMADRE',
                           'work_phone': 'TELEFLABORAL', 'archived': ''},
             'periods': {'id': '', 'id_old': '', 'id_new': '', 'campus_id': {'campus': {'SEDE': 'IDSEDE'}}, 'career_id': {'careers': {'CARRERA': 'IDCARRERA'}}, 'study_plans_id': {'study_plans': {'MALLACURRICULAR': 'IDMALLA'}}, 'career_segmentation_groups_detail_id': '', 'type_planning_id': '', 'shift_id': '', 'academic_date_start': '', 'academic_date_end': '', 'inscription_date_start': '', 'inscription_date_end': '', 'year': '', 'active': '', 'archived': ''},
             'campus': {
                 'id': '', 
                 'id_old': '', 
                 'id_new': '', 
                 'description': 'NOMBRE', 
                 'resume': '', 
                 'phone': 'TELEFONO1', 
                 'email': 'EMAIL', 
                 'address': 'DIRECCION'},
             'colleges': {'id': '', 'id_old': '', 'id_new': '', 'description': 'NOMBRE', 'resume': 'NOMABREV'},
             'careers': {'id': '', 'id_old': '', 'id_new': '', 'college_id': {'colleges': {'FACULTAD': 'IDFACULTAD'}}, 'description': 'DESCRIPCION', 'resume': 'DESCRABREV'},
             'study_plans': {'id': '', 'id_old': '', 'id_new': '', 'number': '',
                             'campus_id': {'campus': {'SEDE': 'IDSEDE'}},
                             'career_id': {'careers': {'CARRERA': 'IDCARRERA'}},
                             'types_hours_groups_id': '',
                             'career_segmentation_group_id': '',
                             'observation': 'OBSERVACION',
                             'validity_date_init': 'FECHAVIGENCIA',
                             'resolution_number': 'RESOLUCIONNRO',
                             'resolution_date': 'RESOLUCIONFEC',
                             'quantity_hours': '',
                             'total_hours': '',
                             'sum_credits': '',
                             'general_hours_credits': '', 'active': '', 'archived': '', 'study_plans_detail': ''},
             'schools': {'id': '', 'id_old': '', 'id_new': '', 'description': 'DESCRIPCION', 'cities_id': {'cities': {'N2016_DISTRITO': 'IDDISTRITO'}}},
             'subjects': {'id': '', 'id_old': '', 'id_new': '', 'description': 'DENOMINACION', 'resume': 'DENOMABREV'},
             'teachers': {'id': '', 'id_old': '', 'id_new': '',
                           'person_id': {'persons': {'PERSONA': 'IDPERSONA'}}
                         }
            }

