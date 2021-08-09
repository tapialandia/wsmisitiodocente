import json
import datetime
import database

# {"colleges":{"id": "3", "id_new": "ca9a10d4-6d92-4e88-be58-64fbbddd97b9", "description": "Facultad de Ciencias de la Empresa 2", "resume": "FCE"}}
# {"persons": {"id": "9", "id_new": "30839df0-95a1-4f58-a01d-c2a4dd2657a6", "type_document_id": "cffe57e4-f12e-4ff9-be6e-4f8b4e7c1fe0", "document_number": "3982821", "first_name": "MIGUEL AUGUSTO", "last_name": "QUIñONEZ OLMEDO", "nationality_id": "df29c2a1-c7ed-4409-830b-13c0d07752f6", "birthdate": "1984-11-29", "mobile": "(0981) 868-729", "email": "augustoquinonez@hotmail.com", "civil_status_id": "7342c8ca-b0cc-41bb-8603-7dc0808cf374", "sex_id": "7826c432-6eae-414b-8151-b4fe0a8805ae", "city_id": "8afd4c2d-1fbb-4b9e-b48b-5cec7b92a418", "address": "Alejandro Villamayor 2554 c/ Emeterio"}}
# {"period_id": "dbf043db-192d-4404-bfe4-18d89fd896ce", "campus": "185fc9f0-2275-4759-8698-3a8d5738567a", "shift": "f99dca93-2a73-4e9f-8251-6e4b2808cbf6", "career": "","study_plan": "6590d53e-86cd-4d5e-b296-d886d3773557", "subjects": {"97ff3258-8eb2-4928-a785-6556edaa0360":"982da704-197b-40e4-ac16-f1988357b484","a92f69d6-e38f-4fb8-b65f-3839d65c746f":"982da704-197b-40e4-ac16-f1988357b484","4c810b29-c004-4d0c-b021-62229ec1a6ad":"982da704-197b-40e4-ac16-f1988357b484","247faea0-c545-484c-af0d-33f0b6a09ead":"982da704-197b-40e4-ac16-f1988357b484","93d5c9c6-ded0-41f8-9050-df2f7fa5aa61":"982da704-197b-40e4-ac16-f1988357b484","154337f5-bfe5-42b9-8066-0087dedb7362":"8f0f48b1-971c-4e08-921f-7299709ac6ec"}}

# {"careers": {"id_new": "2d1bc3b9-f471-44e9-adfa-1803f580a210",       "college_id": "5f334781-5bb9-49ba-81fb-3f88831a7d78",       "description": "CURSOS CORTOS SIG",       "resume": "CCS"}}
# {"colleges":{"id_new":"5f334781-5bb9-49ba-81fb-3f88831a7d78","description":"Dirección de Postgrado-3","resume":"DPG-3"}}
# {"persons":{"id_new":"6bcdf55b-7710-412a-a1b5-e95f12856973","type_document_id":"33b7d069-427a-43ec-88bb-eae4d53ccf3a","document_number":"2227645-3","first_name":"CLAUDIA MARIEL","last_name":"DOMINGUEZ GRANADA","nationality_id":"253ca4e5-0cdb-4974-b7af-678214ca5e8b","birthdate":"1982-05-19","mobile":"0981 451 166","email":"sin@mail","civil_status_id":"41b28ee3-02fa-47d9-9f81-f402f0a70cfd","sex_id":"881e4a3c-208d-40d8-9465-886769b8093c","city_id":"e1cc3440-3496-43a4-9641-7f1aea43e702","address":"Ramos Alfaro c/ Manfred Stark Coscia"}}
# {"id_new":"719326e8-a2e3-4c1b-8c62-fe7176384442","campus_id":"185fc9f0-2275-4759-8698-3a8d5738567a","career_id":"ee75da52-74f1-4aea-8407-3991025c23db","study_plans_id":"e709d5c9-c421-4e99-864d-5ad1750b4eb1","career_segmentation_groups_detail_id":"b92da35c-f3ad-4221-a88e-38298c08ed8e","type_planning_id":"5628780f-a38a-49ac-8b45-8903a1e4d5f2","shift_id":"cc4ccd35-9934-4ebb-a16b-7e446a8b48b6","academic_date_start":"2020-03-01","academic_date_end":"2020-06-30","inscription_date_start":"2020-01-22","inscription_date_end":"2020-03-31","year":"2020"}
# {"schools":{"id_new":"ecaf02b5-ce3b-4616-8a83-a5302587f1af","description":"Facultad de Ciencias Médicas-2","cities_id":"b69d7b66-23f7-4993-9ef6-1fceed34964d"}}


# user_1.json
#{
#    "nombre": '',
#    "id": '',
#    "chats": ["3453kjh5kj"]
#}

# chats_3453kjh5kj.json



_var_ = {
    "logs": {
        "registers": {
            "1": {
                "id": "1",
                "entity": "persons",
                "username": "admin",
                "datetime": "2021-06-09 21:24:05.045806",
                "data": "{'action': 'create table'}"
            }
        }
    },
    "periods_details_schedule": {
        "registers": {
            "124": {
                "id": "124",
                "id_old": "{'IDPLANMATHORARIO': '1063'}",
                "id_new": "e4bde421-368a-4631-ad59-3f6524b7c60b",
                "migrate": "1",
                "period_detail_id": "c43fb17e-32f1-4127-ac16-fbd4ce36f4c7",
                "type_hour_id": "None",
                "types_hours_groups_details_id": "30f25232-92fa-4a45-8e61-8106cfb12c39",
                "classroom_id": "None",
                "class_date": "None",
                "validity_date_start": "2010-03-01",
                "validity_date_end": "2010-11-08",
                "time_start": "10:00",
                "time_end": "12:00",
                "quantity_hours": "0",
                "day_frequencies": "0",
                "archived": "False"
            }
        }
    },
    "periods_details": {
        "registers": {
            "6109": {
                "id": "6109",
                "id_old": "{'IDPLANMATERIA': '12447'}",
                "id_new": "1c34ffc4-83ca-4131-b6c1-fc1ee8502aba",
                "migrate": "1",
                "number": "12447",
                "used_seats": "0",
                "period_id": "ab4648bb-7dea-4fc6-a060-7f029f4b2c81",
                "study_plans_detail_id": "083ad5d6-dcaa-45d0-bfc8-751ccb40ef20",
                "type_subject_id": "982da704-197b-40e4-ac16-f1988357b484",
                "subject_id": "f666b4b8-1094-4492-9cc2-2c2f0125029c",
                "section": "A",
                "maximum_capacity": "100",
                "validity_date_start": "2016-03-01",
                "validity_date_end": "2016-12-03",
                "day_frequencies": "Lun; Mar; Mié; Jue; Vie; Sáb",
                "total_hours": "0",
                "archived": "False",
                "periods_details_status": "1"
            }
        }
    },
    "migrations": {
        "registers": {
            "1": {
                "id": "1",
                "date_init": "2021-06-09 21:23:32.879806",
                "date_end": "2021-06-18 22:11:00.078449",
                "user_init": "admin",
                "user_end": "daniel.caceres@upacifico.edu.py"
            }
        }
    },
    "periods": {
        "registers": {
            "1322": {
                "id": "1322",
                "id_old": "{'IDPLANCONVDET': '5627'}",
                "id_new": "e417b2f5-76c1-40d8-8543-bd69a80d0fdd",
                "migrate": "1",
                "campus_id": "185fc9f0-2275-4759-8698-3a8d5738567a",
                "career_id": "61124077-b13d-46cb-b32e-b643f52e3ce2",
                "study_plans_id": "45a15571-24e4-4a2a-b2e7-4f648283d9bd",
                "career_segmentation_groups_detail_id": "b92da35c-f3ad-4221-a88e-38298c08ed8e",
                "type_planning_id": "5628780f-a38a-49ac-8b45-8903a1e4d5f2",
                "shift_id": "f99dca93-2a73-4e9f-8251-6e4b2808cbf6",
                "academic_date_start": "2017-10-01",
                "academic_date_end": "2018-03-31",
                "inscription_date_start": "2017-09-01",
                "inscription_date_end": "2017-12-30",
                "year": "2017",
                "active": "False",
                "archived": "False"
            }
        }
    },
    "periods_details_exams": {
        "registers": {
            "29967": {
                "id": "29967",
                "id_old": "{'IDPLANMATEXAMEN': '35292'}",
                "id_new": "44922bbc-016c-4c8c-8e56-5e8a27bcec7a",
                "migrate": "1",
                "period_detail_id": "4f74e4f6-0b4b-40f0-a70b-9a03984576f5",
                "type_exam_id": "daf0c7b0-bb6a-44ea-9a9a-60fdd52386c4",
                "date": "2016-01-27",
                "time_start": "08:00",
                "time_end": "09:00",
                "max_qualification": "100",
                "total_students": "0",
                "user_id": "1",
                "archived": "None"
            }
        }
    },
    "periods_details_teachers": {
        "registers": {
            "95": {
                "id": "95",
                "id_old": "{'IDPLANMATDOCENTE': '186'}",
                "id_new": "5173c1d5-468b-4bba-ba62-08c1a89682ea",
                "migrate": "1",
                "period_detail_id": "a9780bef-1bd5-4367-b604-2d12e6ba6dda",
                "teacher_id": "99f85a25-e6c9-4043-bb98-c886de5e09c0",
                "class_date": "None",
                "validity_date_start": "None",
                "validity_date_end": "None",
                "time_start": "None",
                "time_end": "None",
                "quantity_hours": "None",
                "day_frequencies": "None",
                "archived": "False"
            }
        }
    },
    "prerequisites": {
        "registers": {
            "302": {
                "id": "302",
                "id_old": "{'IDMALLA': '52', 'ITEMNRO': '1', 'IDMATERIA': '318'}",
                "id_new": "6b900864-2779-4e7d-93a7-5198ba6ebc60",
                "migrate": "1",
                "study_plans_detail_id": "dcfee1de-3775-40f4-916d-b4474537b6cb",
                "prerequisites_study_plans_detail_id": "28c38d58-c213-4e7f-b5a0-60e8894a17ab",
                "archived": "None"
            }
        }
    },
    "registration_documents": {
        "registers": {
            "1": {
                "id": "1",
                "id_old": "{'IDTIPODOC': '8'}",
                "id_new": "0a5dfc5b-393e-47a2-b943-36de5706d524",
                "migrate": "1",
                "description": "Fotos tipo Carnet (PG)",
                "grade_title": "False",
                "postgraduate_title": "True",
                "archived": "False"
            }
        }
    },
    "schools": {
        "registers": {
            "3": {
                "id": "3",
                "id_old": "{'IDCOLEGIO': '3'}",
                "id_new": "b58c2aed-f105-43f4-aa00-3e1589c81363",
                "migrate": "1",
                "description": "2261 COLONIA SIERRA LEON",
                "cities_id": "fe0a58e1-e2c3-4dce-b145-80964261fc6a",
                "archived": "False"
            }
        }
    },
    "sexes": {
        "registers": {
            "2": {
                "id": "2",
                "id_old": "{'SEXO': 'F'}",
                "id_new": "881e4a3c-208d-40d8-9465-886769b8093c",
                "migrate": "1",
                "description": "FEMENINO",
                "archived": "False"
            }
        }
    },
    "shifts": {
        "registers": {
            "3": {
                "id": "3",
                "id_old": "{'IDTURNO': '3'}",
                "id_new": "cc4ccd35-9934-4ebb-a16b-7e446a8b48b6",
                "migrate": "1",
                "description": "NOCHE",
                "archived": "False"
            }
        }
    },
    "students": {
        "registers": {
            "1": {
                "id": "1",
                "id_old": "{'IDALUMNO': '1'}",
                "id_new": "eea42c9a-2b6a-4d6d-928c-a99bf3b21029",
                "migrate": "1",
                "person_id": "2eca0bf4-32c9-49b1-b198-3b7899f4a0c1",
                "student_number": "1",
                "school_id": "a21a5f52-07ab-4103-9dc3-f98b468567f7",
                "school_title_id": "2d5695ef-c3bd-4dbf-8560-53cf6c63af5a",
                "school_end_year": "2007",
                "university_id": "cb8ea984-7a18-4c4f-ae34-d5a956a420b1",
                "university_title_id": "None",
                "university_end_year": "None",
                "father_name": "None",
                "mother_name": "None",
                "workplace": "Mario Grande Jeans",
                "work_phone": "021211971",
                "archived": "False"
            }
        }
    },
    "study_plans": {
        "registers": {
            "19": {
                "id": "19",
                "id_old": "{'IDMALLA': '184'}",
                "id_new": "6590d53e-86cd-4d5e-b296-d886d3773557",
                "migrate": "1",
                "number": "184",
                "campus_id": "185fc9f0-2275-4759-8698-3a8d5738567a",
                "career_id": "2eacc7bf-79b7-4abc-9ac0-eb7c69203e41",
                "types_hours_groups_id": "24a52bf3-9652-4c18-83e3-ceb1f0158a74",
                "career_segmentation_group_id": "6863ab6d-f134-4a4b-8834-6f2337092aba",
                "observation": "S/O",
                "validity_date_init": "2012-07-19",
                "resolution_number": "1",
                "resolution_date": "2012-05-08",
                "study_plans_detail": "[]",
                "quantity_hours": "0",
                "total_hours": "0",
                "sum_credits": "0",
                "general_hours_credits": "0",
                "active": "False",
                "archived": "True"
            }
        }
    },
    "study_plans_detail": {
        "registers": {
            "9336": {
                "id": "9336",
                "id_old": "None",
                "id_new": "ba99c1b4-03b0-4001-8bf3-8e2976ec731b",
                "migrate": "1",
                "study_plans_id": "fc2c5b9f-06e0-45bb-96c8-1162b93f7070",
                "study_plans_detail_id": "None",
                "career_segmentation_groups_detail_id": "a5a915ab-8a63-40ba-94f2-4b52c04b357f",
                "hierarchy_id": "6cafdc44-3f1c-402c-9e03-94d2c00848ce",
                "type_subject_id": "c96ce7a9-d38d-45db-a9be-2d5bc23de468",
                "subject_id": "39e53553-8281-4057-bfac-77f6437b3408",
                "credits_per_hour": "None",
                "credits": "None",
                "practice_hours": "None",
                "autonomous_hours": "None",
                "quantity_hours": "None",
                "archived": "None"
            }
        }
    },
    "subjects": {
        "registers": {
            "1": {
                "id": "1",
                "id_old": "{'IDMATERIA': '1'}",
                "id_new": "f87f94f9-7e3e-473b-b1a3-d9e76883984b",
                "migrate": "1",
                "description": "ANATOMIA",
                "resume": "ANATO",
                "archived": "False"
            }
        }
    },
    "teachers": {
        "registers": {
            "787": {
                "id": "787",
                "id_old": "{'IDDOCENTE': '819'}",
                "id_new": "8c62acc7-65fd-481f-849d-9228bd2370cb",
                "migrate": "1",
                "person_id": "d0dd1848-2a05-4177-a69c-9cdb5e410e52",
                "archived": "False"
            }
        }
    },
    "titles": {
        "registers": {
            "78": {
                "id": "78",
                "id_old": "{'IDTITULO': '86'}",
                "id_new": "330458b1-9f69-49a3-af71-6d97e69894d3",
                "migrate": "1",
                "description": "Administración de Marketing",
                "school_title": "True",
                "university_title": "False",
                "archived": "False"
            }
        }
    },
    "types_documents": {
        "registers": {
            "1": {
                "id": "1",
                "id_old": "{'TIPODOC': 'CI'}",
                "id_new": "33b7d069-427a-43ec-88bb-eae4d53ccf3a",
                "migrate": "1",
                "description": "Cédula de Identidad",
                "archived": "False"
            }
        }
    },
    "types_exams": {
        "registers": {
            "1": {
                "id": "1",
                "id_old": "{'IDENTIFICADOR': ' T1'}",
                "id_new": "485f6217-ff64-4169-ade1-ea737cb61228",
                "migrate": "1",
                "description": "( T1)",
                "summarized": " T1",
                "archived": "False"
            }
        }
    },
    "types_hours": {
        "registers": {
            "1": {
                "id": "1",
                "id_old": "None",
                "id_new": "c7d09d2c-1888-4345-988f-496134be4d08",
                "migrate": "1",
                "description": "PRESENCIAL",
                "archived": "False"
            }
        }
    },
    "types_hours_career": {
        "registers": {
            "1": {
                "id": "1",
                "id_old": "None",
                "id_new": "274d26d2-f2af-4706-bff2-27a1969991c6",
                "migrate": "1",
                "type_hour_group_id": "24a52bf3-9652-4c18-83e3-ceb1f0158a74",
                "career_id": "2c39feb4-2099-41ed-b9d0-03fc2cabe243",
                "archived": "None"
            }
        }
    },
    "types_hours_groups": {
        "registers": {
            "2": {
                "id": "2",
                "id_old": "{'TYPE_HOUR_GROUP_ID': '2'}",
                "id_new": "24a52bf3-9652-4c18-83e3-ceb1f0158a74",
                "migrate": "1",
                "description": "POSTGRADO",
                "archived": "False"
            }
        }
    },
    "types_hours_groups_details": {
        "registers": {
            "1": {
                "id": "1",
                "id_old": "None",
                "id_new": "b418ac4e-a590-426e-9c5c-7f09511c68fe",
                "migrate": "1",
                "order": "1",
                "raw": "PRESENCIAL > TEORICO",
                "type_hour_id": "c7d09d2c-1888-4345-988f-496134be4d08",
                "sub_type_hour_id": "84079fdb-cac2-4ebe-b2ef-67a89f529fd4",
                "type_hour_group_id": "",
                "archived": "None"
            }
        }
    },
    "types_subjects": {
        "registers": {
            "3": {
                "id": "3",
                "id_old": "{'IDTIPOMATERIA': '3'}",
                "id_new": "50faf06f-72f6-4a0a-9ab8-e1e55f40d895",
                "migrate": "1",
                "description": "Condicional",
                "set_subject": "False",
                "archived": "False"
            }
        }
    },
    "universities": {
        "registers": {
            "1": {
                "id": "1",
                "id_old": "{'IDUNIVERSIDAD': '0'}",
                "id_new": "cb8ea984-7a18-4c4f-ae34-d5a956a420b1",
                "migrate": "1",
                "description": "(Sin Universidad)",
                "cities_id": "fe0a58e1-e2c3-4dce-b145-80964261fc6a",
                "archived": "False"
            }
        }
    },
    "campus": {
        "registers": {
            "3": {
                "id": "3",
                "id_old": "{'IDSEDE': '3'}",
                "id_new": "cfc01fea-a3ee-44ed-b83b-eae1a56efe68",
                "migrate": "1",
                "description": "PEDRO JUAN CABALLERO",
                "resume": "PEDRO JUAN CABALLERO",
                "phone": "(0336) 272-028",
                "email": "Sin Correo",
                "address": "Sin dirección",
                "archived": "False"
            }
        }
    },
    "blocks": {
        "registers": {}
    },
    "careers": {
        "registers": {
            "1": {
                "id": "1",
                "id_old": "{'IDCARRERA': '2'}",
                "id_new": "f09c8361-1c8f-445d-bd4c-86212c884344",
                "migrate": "1",
                "college_id": "c65fb9f8-3256-408c-87d5-53bf162a31e1",
                "description": "Odontología",
                "resume": "ODON",
                "archived": "False"
            }
        }
    },
    "careers_segmentation": {
        "registers": {
            "2": {
                "id": "2",
                "id_old": "None",
                "id_new": "45c0df9c-b975-4bd7-8b7d-2e675ce4c222",
                "migrate": "1",
                "career_segmentation_id": "None",
                "description": "SEMESTRE",
                "archived": "None"
            }
        }
    },
    "careers_segmentation_groups": {
        "registers": {
            "4": {
                "id": "4",
                "id_old": "None",
                "id_new": "ff833f2d-1735-4057-aa6b-7dbfdba6109c",
                "migrate": "1",
                "description": "MIXTA 421",
                "archived": "None"
            }
        }
    },
    "careers_segmentation_groups_details": {
        "registers": {
            "1": {
                "id": "1",
                "id_old": "None",
                "id_new": "b92da35c-f3ad-4221-a88e-38298c08ed8e",
                "migrate": "1",
                "order": "1",
                "raw": "CURSO 1 SEMESTRE 1",
                "career_segmentation_id": "9cdb67f9-1592-4e1e-8774-0059b5ff5188",
                "value1": "1",
                "sub_career_segmentation_id": "45c0df9c-b975-4bd7-8b7d-2e675ce4c222",
                "value2": "1",
                "career_segmentation_group_id": "6863ab6d-f134-4a4b-8834-6f2337092aba"
            }
        }
    },
    "cities": {
        "registers": {
            "328": {
                "id": "328",
                "id_old": "{'IDDISTRITO': '689'}",
                "id_new": "d95e7ec2-90ef-49e2-b8a4-306178f9db89",
                "migrate": "1",
                "description": "ASSAI",
                "departament_id": "fc85b13e-aa94-4b4e-b3be-2993ce8e3d2d",
                "archived": "False"
            }
        }
    },
    "modifications": {
        "registers": {
            "63": {
                "id": "63",
                "entity": "schools",
                "types": "duplicates",
                "data": "{'id_old_keep': {'IDCOLEGIO': '9112'}, 'id_old_discards': [{'IDCOLEGIO': '9143'}], 'entity_dependencies': [{'students': 'school_id'}]}",
                "migration_id": "30",
                "estado": "A",
                "datetime": "2021-06-15 13:03:52.306698"
            }
        }
    },
    "civil_states": {
        "registers": {
            "4": {
                "id": "4",
                "id_old": "{'ESTADOCIVIL': 'V'}",
                "id_new": "de2efa61-9a9f-4ecb-9ffc-2dd83692398e",
                "migrate": "1",
                "description": "VIUDO/A",
                "archived": "False"
            }
        }
    },
    "classrooms": {
        "registers": {}
    },
    "colleges": {
        "registers": {
            "7": {
                "id": "7",
                "id_old": "{'IDFACULTAD': '6'}",
                "id_new": "ca9a10d4-6d92-4e88-be58-64fbbddd97b9",
                "migrate": "1",
                "description": "Facultad de Ciencias Agropecuarias",
                "resume": "FCA",
                "archived": "False"
            }
        }
    },
    "countries": {
        "registers": {
            "1": {
                "id": "1",
                "id_old": "{'IDPAIS': '2'}",
                "id_new": "8e11767c-dd40-409c-b8fb-59ceda1c8665",
                "migrate": "1",
                "description": "BRASIL",
                "nationality": "brasileña",
                "archived": "False"
            }
        }
    },
    "departaments": {
        "registers": {
            "1": {
                "id": "1",
                "id_old": "{'IDDEPARTAMENTO': '18'}",
                "id_new": "733f1903-7e01-4e56-854f-05232052d2b2",
                "migrate": "1",
                "description": "AMAZONAS",
                "countrie_id": "8e11767c-dd40-409c-b8fb-59ceda1c8665",
                "archived": "False"
            }
        }
    },
    "hierarchies": {
        "registers": {
            "1": {
                "id": "1",
                "id_old": "{'ID': '1'}",
                "id_new": "6cafdc44-3f1c-402c-9e03-94d2c00848ce",
                "migrate": "1",
                "hierarchy_id": "None",
                "description": "ASIGNATURAS",
                "raw": "ASIGNATURAS",
                "is_level_primary_study_plan": "True",
                "archived": "False"
            }
        }
    },
    "inscriptions_documents": {
        "registers": {
            "958": {
                "id": "958",
                "id_old": "{'IDTIPODOC': '8', 'IDINSCRIPCION': '6865'}",
                "id_new": "b2c9e6c4-33b3-4682-8c6f-abf10f4c0f69",
                "migrate": "1",
                "inscription_student_id": "551da34f-696c-402b-ba9d-431689105297",
                "registration_document_id": "0a5dfc5b-393e-47a2-b943-36de5706d524",
                "quantity": "2",
                "delivered_quantity": "0",
                "observation": "None",
                "date": "2011-10-19",
                "url_file": "None",
                "file_name": "None",
                "archived": "False"
            }
        }
    },
    "persons": {
        "registers": {
            "2": {
                "id": "2",
                "id_old": "{'IDPERSONA': '84'}",
                "id_new": "5c7fe63e-b6d5-4d34-81c0-04c774197f80",
                "migrate": "1",
                "type_document_id": "33b7d069-427a-43ec-88bb-eae4d53ccf3a",
                "document_number": "2044308",
                "first_name": "CARLOS ALBERTO",
                "last_name": "DOMINGUEZ BENITEZ",
                "nationality_id": "253ca4e5-0cdb-4974-b7af-678214ca5e8b",
                "birthdate": "1974-01-25",
                "mobile": "0981- 892-931",
                "email": "academico@ioa.com.py",
                "civil_status_id": "e16c5e6f-5451-47f0-9dd8-3017733c1fba",
                "sex_id": "4f370aa0-0c6a-4bef-82a5-3447166aaec4",
                "city_id": "e1cc3440-3496-43a4-9641-7f1aea43e702",
                "address": "Calle 12 c/ Silvio Parodi"
            }
        }
    },
    "study_plans_hours": {
        "registers": {
            "175": {
                "id": "175",
                "id_old": "None",
                "id_new": "5085425a-ed57-4bf9-832e-54b10c36aa91",
                "migrate": "1",
                "study_plans_detail_id": "01e067d9-e247-43b7-afc8-cbeb4288b959",
                "types_hours_groups_details_id": "48f0affa-7275-4481-b8e6-1092a8967f03",
                "type_hour_id": "None",
                "hours": "3",
                "archived": "None"
            }
        }
    },
    "inscriptions_students": {
        "registers": {
            "59107": {
                "id": "59107",
                "id_old": "{'IDINSCRIPCION': '26636'}",
                "id_new": "d4580c9c-4b6c-4b1d-894e-e5045f323780",
                "migrate": "1",
                "number": "26636",
                "student_id": "4d02fdf2-ba13-442b-b260-9b8ce83fbd92",
                "study_plans_id": "25e40a23-55ec-4ceb-bcf6-b88ad81d1ee7",
                "period_id": "5a4dd39f-0620-47af-b426-adec4b548a6e",
                "careers_segmentation_groups_detail_id": "d5811ca1-c36e-489c-a4ff-43943a4c7e2b",
                "shift_id": "ce941d59-51ee-4b52-bae7-60cbaf18a43a",
                "date": "2015-08-05",
                "users_id": "1",
                "inscriptions_students_status": "2",
                "archived": "False"
            }
        }
    },
    "types_plannings": {
        "registers": {
            "2": {
                "id": "2",
                "id_old": "{'IDTIPOPLANIFICACION': '2'}",
                "id_new": "135a4b50-d163-4a8e-9d6c-19363454a5f4",
                "migrate": "1",
                "description": "CURSO",
                "slug": "CURSO",
                "archived": "False"
            }
        }
    },
    "inscriptions_students_subjects": {
        "registers": {
            "100098": {
                "id": "100098",
                "id_old": "{'IDINSCRIPCION': '23028', 'IDPLANMATERIA': '10202'}",
                "id_new": "50bd6c47-e43e-4c48-8a31-e1776d5e1b17",
                "migrate": "1",
                "inscription_student_id": "0848bc9f-180f-4624-ac4d-a4514fb968b1",
                "study_plan_detail_id": "5f27a861-ca63-4f9f-bf3d-80568e069b60",
                "period_detail_id": "2e07bebc-f290-427e-8ebd-29f78de72d51",
                "exams": "None",
                "qualification": "None",
                "note": "None",
                "subjects_status": "2",
                "archived": "False"
            }
        }
    }
}

if 1==2:
    _cursor_ = database.execute_raw_sql_bancard(f"""SELECT * FROM MATERIA WHERE IDMATERIA  = 2360;""")
    _c_fire_ = database.execute_raw_sql(f"""SELECT * FROM subjects where id=1880;""")

    print("------------firebird------------")
    for row in _cursor_:
        print(row)

    print("---------------------------------------------------------------------------------------------------")
    print("------------postgre------------")
    for row in _c_fire_:
        print(row)
if 2==3:
    print( database.get_inspector() );


    
ll_iddocente = 2037 
ls_sql =    f""" select c.prefijo, a.idpersona, a.iddocente, b.nombre, b.apellido, 
            b.cinro, b.tipodoc, b.fechanac,
            b.estadocivil, b.sexo, b.gruposanguineo, 
            b.email,b.telefparticular, b.telefmovil, cast(TRIM(b.direccion) as varchar(150)) as direccion 
            from docente a, persona b, prefijo c 
            where a.iddocente = {ll_iddocente} 
            and a.idpersona = b.idpersona 
            and a.idprefijo = c.idprefijo  """
_cursor_ = database.execute_raw_sql_bancard(ls_sql) 
_cursor_keys_ = _cursor_.keys()
data = []
for row in _cursor_:
    _row_ = {}
    for key in _cursor_keys_:
        _row_[key] = row[key]
    data.append(_row_)
print(data) 


#for row in _cursor_:
    #ljson_registro = json.dumps(row)
    #print(row)
    

