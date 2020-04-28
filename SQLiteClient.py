# -*- Coding: utf-8 -*-

import sqlite3

class SQLiteClient:
    
    def __init__(self, _dbname):
        self.connection = sqlite3.connect(_dbname)
        self.cursor = self.connection.cursor()

    def insert(self, _query):
        self.cursor.execute(_query)
        self.connection.commit()

    def selectone(self, _query):
        self.cursor.execute(_query)
        return self.cursor.fetchone()

    def delete_all(self, _table):
        query = "DELETE FROM " + _table +" WHERE 1"
        self.cursor.execute(query)
        self.connection.commit()