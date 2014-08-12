__author__ = 'micheng'

import sqlite3

connection = sqlite3.connect('../coachdata.sqlite')
cursor = connection.cursor()
cursor.execute("delete from timing_data where rowid = 49")
connection.commit()
connection.close()