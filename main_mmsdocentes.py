from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from typing import Optional

import database

app = FastAPI()
ERROR_MISSING_PARAMETER = 1
ERROR_INVALID_PARAMETER = 2
ERROR_INTERNAL = 3
ERROR_NOT_FOUND = 4

@app.get('/docente_personales')
def get_docente_personales(al_iddocente: str = None):
    try:
        #ll_iddocente = 240 
        ls_sql =    f""" select pre.prefijo,
                    doc.idpersona, 
                    doc.iddocente, 
                    per.nombre, 
                    per.apellido, 
                    per.cinro, 
                    per.tipodoc, 
                    EXTRACT(day FROM per.fechanac) || '/' || EXTRACT(month FROM per.fechanac) || '/' || EXTRACT(year FROM per.fechanac) as fechanac,
                    per.estadocivil, 
                    per.sexo, 
                    per.gruposanguineo, 
                    per.email,
                    per.telefparticular, 
                    per.telefmovil, 
                    cast(TRIM(per.direccion) as varchar(150)) as direccion 
                    from docente doc, 
                         persona per, 
                         prefijo pre 
                    where doc.iddocente = {al_iddocente} 
                    and doc.idpersona = per.idpersona 
                    and doc.idprefijo = pre.idprefijo  """
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

@app.get('/docente_profesionales')
def get_docente_profesionales(al_idpersona: str = None):
    try:
        #al_idpersona = 4959
        ls_sql =    f""" select
                        idpersona,
                        nombmpresa,
                        descripcargo,
                        antiguedad,
                        EXTRACT(day FROM fechasalida) || '/' || EXTRACT(month FROM fechasalida) || '/' || EXTRACT(year FROM fechasalida) as fechasalida,
                        telefono,
                        cast(a.tareas as varchar(1000)) as tarea
                        from personaexperiencia a
                        where a.idpersona = {al_idpersona} """
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

@app.get('/docente_estudios')
def get_docente_estudios(al_idpersona: str = None):
    try:
        #al_idpersona = 4959
        ls_sql =    f""" select tin.descripcion as tipoinstruccion,
                         pi.institucion,
                         tit.nombre as titulo,
                         pi.periodotitulo,
                         pi.duracion 
                         from personainstruccion pi,
                            tipo_instruccion tin,
                            titulo tit
                         where pi.idpersona = {al_idpersona}
                         and pi.idtipo_instruccion = tin.idtipo_instruccion
                         and pi.idtitulo = tit.idtitulo """
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

@app.get('/docente_familiares')
def get_docente_familiares(al_idpersona: str = None):
    try:
        #al_idpersona = 4959
        ls_sql =    f""" select par.nombre as parentesco,
                            pf.nombre,
                            pai.nombre as pais,
                            pf.telefono,
                            EXTRACT(day FROM pf.fechanac) || '/' || EXTRACT(month FROM pf.fechanac) || '/' || EXTRACT(year FROM pf.fechanac) as fechanac
                            from personafamilia pf,
                                parentesco par,
                                pais pai
                            where pf.idpersona = {al_idpersona} 
                            and pf.idparentesco = par.idparentesco
                            and pf.idpais = pai.idpais """
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


@app.get('/docente_materias')
def get_docente_materias(al_iddocente: str = None):
    try:
        #al_iddocente = 240
        ls_sql =    f""" select a.idcontrato ,
                            e.denominacion as materia ,
                            cast(b.remuneracion as int) remuneracion,
                            EXTRACT(day FROM a.iniciocontrato) || '/' || EXTRACT(month FROM a.iniciocontrato) || '/' || EXTRACT(year FROM a.iniciocontrato) as iniciocontrato, 
                            EXTRACT(day FROM a.fincontrato) || '/' || EXTRACT(month FROM a.fincontrato) || '/' || EXTRACT(year FROM a.fincontrato) as fincontrato 
                        from contratodocente a,
                            contratodocdetalle b,
                            planmatdocente c,
                            planmateria d,
                            materia e
                        where a.iddocente = {al_iddocente} 
                            and  a.idcontrato = b.idcontrato
                            and b.idplanmatdocente = c.idplanmatdocente
                            and c.idplanmateria = d.idplanmateria
                            and d.idmateria = e.idmateria
                            and a.estado != 'A' and a.vigente = 'SI'
                            group by a.idcontrato,
                            e.denominacion ,
                            b.remuneracion,
                            a.iniciocontrato,
                            a.fincontrato
                            order by a.iniciocontrato,
                            a.fincontrato,
                            a.idcontrato  """
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



@app.get('/docente_asistencias')
def get_docente_asistencias(al_iddocente: str = None):
    try:
        #al_iddocente = 240
        ls_sql =    f""" select
                        materia as materia,
                        curso as curso,
                        semestre as semestre,
                        turno as turno,
                        seccion as seccion,
                        dia as dia,
                        EXTRACT(day FROM a.fecha_planificada) || '/' || EXTRACT(month FROM a.fecha_planificada) || '/' || EXTRACT(year FROM a.fecha_planificada)  as fecha,
                        substring(HORA_ENTRADA_PLANIF from 1 for 5) as HORA_ENTRADA_PLA,
                        substring(HORA_SALIDA_PLANIF  from 1 for 5) as HORA_SALIDA_PLA,
                        HORA_ENTRADA_REAL as HORA_ENTRADA_REAL  ,
                        HORA_SALIDA_REAL AS HORA_SALIDA_REAL,
                        TOTALHORAS_REAL as TOTAL_HORAS
                        from docenteasistencia_v2 a
                        where a.iddocente = {al_iddocente}
                        and a.vigente = 'S'
                        and extract(year from a.fecha_planificada) >= 2017
                        order by a.fecha_planificada  """
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


@app.get('/docente_familiares')
def get_docente_familiares(al_idpersona: str = None):
    try:
        #al_idpersona = 4959
        ls_sql =    f""" select par.nombre as parentesco,
                            pf.nombre,
                            pai.nombre as pais,
                            pf.telefono,
                            EXTRACT(day FROM pf.fechanac) || '/' || EXTRACT(month FROM pf.fechanac) || '/' || EXTRACT(year FROM pf.fechanac) as fechanac
                            from personafamilia pf,
                                parentesco par,
                                pais pai
                            where pf.idpersona = {al_idpersona} 
                            and pf.idparentesco = par.idparentesco
                            and pf.idpais = pai.idpais """
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


@app.get('/docente_materias')
def get_docente_materias(al_iddocente: str = None):
    try:
        #al_iddocente = 240
        ls_sql =    f""" select a.idcontrato ,
                            e.denominacion as materia ,
                            cast(b.remuneracion as int) remuneracion,
                            EXTRACT(day FROM a.iniciocontrato) || '/' || EXTRACT(month FROM a.iniciocontrato) || '/' || EXTRACT(year FROM a.iniciocontrato) as iniciocontrato, 
                            EXTRACT(day FROM a.fincontrato) || '/' || EXTRACT(month FROM a.fincontrato) || '/' || EXTRACT(year FROM a.fincontrato) as fincontrato 
                        from contratodocente a,
                            contratodocdetalle b,
                            planmatdocente c,
                            planmateria d,
                            materia e
                        where a.iddocente = {al_iddocente} 
                            and  a.idcontrato = b.idcontrato
                            and b.idplanmatdocente = c.idplanmatdocente
                            and c.idplanmateria = d.idplanmateria
                            and d.idmateria = e.idmateria
                            and a.estado != 'A' and a.vigente = 'SI'
                            group by a.idcontrato,
                            e.denominacion ,
                            b.remuneracion,
                            a.iniciocontrato,
                            a.fincontrato
                            order by a.iniciocontrato,
                            a.fincontrato,
                            a.idcontrato  """
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



@app.get('/docente_cedula2id')
def get_doc_ce2id(as_cedula: str = None):
    try:
        #as_cedula = 1568776
        ls_sql =    f""" select per.idpersona as idpersona,
                                ( select max(doc.iddocente) from docente doc where doc.idpersona = per.idpersona ) as iddocente
                        from persona per
                        where per.cinro = {as_cedula} """
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
