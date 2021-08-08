import os
import sys
import asyncio
import threading

from fake_databases import _tables_ as _tb_
import database
import datetime
import time as tm


class Checker:

    def __init__(self):
        pass

    async def start(self):
        _tables_ = _tb_
        _str_ = ''
        print('Starting checking process.', flush=True)
        for k, v in _tables_.items():
            if v != '':
                _table_name_ = f'{k}_{v}'
                sql_check = f"select 1 as C from rdb$relations where rdb$relation_name = '{_table_name_}'"
                try:
                    cursor = database.execute_raw_sql_bancard(sql_check)
                    data_ = [row for row in cursor]
                    if len(data_) > 0:
                        sql_create = f'CREATE TABLE {_table_name_}(ID_ORIGIN CHAR(40) NOT NULL,ID_FINAL INTEGER NOT ' \
                                     'NULL)'
                        database.execute_raw_sql_bancard(sql_create)
                except Exception as error:
                    error_file = open("stdout_errors.txt", "a")
                    error_file.write(f'ERROR: {datetime.datetime.now()} {str(error)} {_table_name_}\n')
                    pass

        await self.sync_data()

    @staticmethod
    def migrate_data():
        for k, v in _tb_.items():
            if v != '':
                _table_name_ = f'{k}_{v}'
                print(f"Migrating: {_table_name_}", flush=True)
                # Count registers
                toolbar_width = 40

                # setup toolbar
                sys.stdout.write("[%s]" % (" " * toolbar_width))
                sys.stdout.flush()
                sys.stdout.write("\b" * (toolbar_width + 1))  # return to start of line, after '['

                for i in range(toolbar_width):
                    tm.sleep(1)
                    # update the bar
                    sys.stdout.write("-")
                    sys.stdout.flush()

                sys.stdout.write("]\n")

    async def sync_data(self):
        pass


if __name__ == '__main__':
    PACKAGE_PARENT = '..'
    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
    _check_ = Checker()
    if '--migrate' in sys.argv:
        try:
            migration_thread = threading.Thread(target=_check_.migrate_data, name="Migrator", args=[])
            migration_thread.start()
        except Exception as ex:
            f = open("stdout_errors.txt", "a")
            f.write(f'ERROR_MIGRATION: Impossible to start migration process {datetime.datetime.now()} {str(ex)}\n')
            pass
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_check_.start())
