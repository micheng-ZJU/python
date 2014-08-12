__author__ = 'micheng'


import sqlite3

connection = sqlite3.connect('../coachdata.sqlite')
cursor = connection.cursor()
the_id =3
result = cursor.execute("select athlete_id,value from timing_data where athlete_id = ?", (the_id,)).fetchall()
print(result)
connection.close()