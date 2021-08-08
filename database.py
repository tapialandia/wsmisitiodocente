from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text


DEBUG = True
USER = 'upp'
PASS = 'upp123'
HOST = 'academico.upacifico.edu.py' if DEBUG else '10.0.0.22'
DATABASE_PATH = 'migrator'
PORT = 5432
SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DATABASE_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo_pool=False
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

USER_B = 'SYSDBA'
PASS_B = 'up2013'
HOST_B = '190.104.179.250' if DEBUG else '10.0.0.142'
DATABASE_PATH_B = 'bdbancard'
SQLALCHEMY_DATABASE_URL_B = f"firebird+fdb://{USER_B}:{PASS_B}@{HOST_B}/{DATABASE_PATH_B}?charset=ISO8859_1"

engine_B = create_engine(
    SQLALCHEMY_DATABASE_URL_B, echo_pool=False
)
Session_B = sessionmaker(autocommit=False, autoflush=False, bind=engine_B)


def get_first_register(table_name):
    result = execute_raw_sql(f'SELECT * FROM {table_name} LIMIT 1;')
    data_ = [row for row in result]
    data = []
    for rows in data_:
        for index in rows:
            data.append(str(index))
    return data

def get_registers(table_name):
    result = execute_raw_sql(f'SELECT * FROM {table_name} ORDER BY RANDOM() LIMIT 10;')    
    data_ = [row for row in result]
    data = {}
    count__ = 0
    for rows in data_:
        data[count__] = []
        for index in rows:
            data[count__].append(str(index))
        count__ += 1
    return data


def execute_raw_sql(sql):
    sql = text(sql)
    result = engine.execute(sql)
    return result


def execute_raw_sql_bancard(sql):
    sql = text(sql)
    result = engine_B.execute(sql)
    return result


def get_inspector():
    return inspect(engine)

