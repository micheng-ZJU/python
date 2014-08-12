__author__ = 'micheng'
import sqlite3

connection = sqlite3.connect('../coachdata.sqlite')
cursor = connection.cursor()
cursor.execute("insert into timing_data (athlete_id, value) values (?,?)", (3,'2.16'))
connection.commit()
connection.close()