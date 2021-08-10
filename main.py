#from functions import get_id_old, get_id_old_variable, get_career_segmentation, get_shift, get_cant_subjects_on_study_plan
#from fake_databases import _indexes_, _tables_, _pk_
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from typing import Optional
#from pydantic import Json
#from sedes import Arancel, ArancelNI

import database

app = FastAPI()
ERROR_MISSING_PARAMETER = 1
ERROR_INVALID_PARAMETER = 2
ERROR_INTERNAL = 3
ERROR_NOT_FOUND = 4

@app.get('/docente_datos_personales')
def get_test_data(al_iddocente: str = None):
    try:
        #ll_iddocente = 2037 
        ls_sql =    f""" select c.prefijo, a.idpersona, a.iddocente, b.nombre, b.apellido, 
                    b.cinro, b.tipodoc, EXTRACT(day FROM b.fechanac) || '/' || EXTRACT(month FROM b.fechanac) || '/' || EXTRACT(year FROM b.fechanac) as fechanac,
                    b.estadocivil, b.sexo, b.gruposanguineo, 
                    b.email,b.telefparticular, b.telefmovil, cast(TRIM(b.direccion) as varchar(150)) as direccion 
                    from docente a, persona b, prefijo c 
                    where a.iddocente = {al_iddocente} 
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
        #registro = [{"uno":"dato1" , "dos":"dato2"}]
        print(data) 
    except Exception as ex:
            print(ex)
            pass
    return JSONResponse(status_code=200, content=data)


