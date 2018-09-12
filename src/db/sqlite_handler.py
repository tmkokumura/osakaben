# encode:utf-8

import sqlite3
from .database_handler import DatabaseHandler


class SqliteHandler(DatabaseHandler):
    """ constants """
    _DEFAULT_DB_NAME = "db.name"

    """ constructors """
    def __init__(self, db_name=_DEFAULT_DB_NAME):
        self._conn = sqlite3.connect(db_name)
        self._c = self._conn.cursor()

    """ public methods """
    def execute(self, sql):
        return self._c.execute(sql)

    def commit(self):
        self._c.execute('commit')

    def rollback(self):
        self._c.execute('rollback')
