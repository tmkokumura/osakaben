# encode:utf-8

import sqlite3
from db.handler.database_handler import DatabaseHandler


class SqliteHandler(DatabaseHandler):
    """ constants """
    _DEFAULT_DB_NAME = "osakaben.db"

    """ constructors """
    def __init__(self, db_name=_DEFAULT_DB_NAME):
        self._conn = sqlite3.connect(db_name)
        self._c = self._conn.cursor()

    """ public methods """
    def execute(self, sql, params):
        return self._c.execute(sql, params)

    def commit(self):
        self._conn.commit()

    def rollback(self):
        self._conn.rollback()
