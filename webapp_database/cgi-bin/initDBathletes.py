__author__ = 'micheng'

import sqlite3

connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()

import glob
import athletemodel
data_files = glob.glob('../data/*.txt')
athletes = athletemodel.put_to_store(data_files)

for each_ath in athletes:
    name = athletes[each_ath].name
    dob = athletes[each_ath].dob
    # add athletes
    cursor.execute("INSERT INTO athletes (name,dob) VALUES (?,?)", (name, dob))
    connection.commit()
    cursor.execute("SELECT id FROM athletes WHERE name=? AND dob=?",(name,dob))
    current_id = cursor.fetchone()[0]
    # add every athletes timing data
    for each_time in athletes[each_ath].clean_data:
        cursor.execute("INSERT INTO timing_data (athlete_id, value) VALUES (?,?)", (current_id,each_time))
        connection.commit()

connection.close()