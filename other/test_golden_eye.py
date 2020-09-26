import sqlite3

conn = sqlite3.connect('golden-eye.db')
cur = conn.cursor()
# cur.execute("SELECT * FROM xrates")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()

from peewee import (SqliteDatabase)

db = SqliteDatabase('golden-eye.db')


# class XRate(Model):
#     class Meta:
#         database = db
#         db_table = 'xrates'
#         index = (
#             (('from_currency', 'to_currency'), True),
#         )
#
#     from_currency = IntegerField()
#     to_currency = IntegerField()
#     rate = DoubleField()
#     update = DateTimeField(default=peewee_datetime.datetime.now)
from other import models

models.XRate.create_table()
models.XRate.create(from_currency=980, to_currency=840, rate=25)
