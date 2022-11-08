from flask import g
import sqlite3

DATABASE_URL = 'task.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE_URL)
    return db
