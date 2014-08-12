
import sqlite3
import sys

db_name = 'coachdata.sqlite'

def get_names_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("SELECT name FROM athletes")
    # for each row in results list, get the first element (name) to build a list
    response = [row[0] for row in results.fetchall()]
    connection.close()
    return(response)

def get_namesID_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("SELECT name,id FROM athletes")
    response = results.fetchall()
    connection.close()
    return(response)


def get_athlete_from_id(athlete_id):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("SELECT name,dob FROM athletes WHERE id=?", (athlete_id,))
    (name, dob) = results.fetchone()

    results = cursor.execute("SELECT value FROM timing_data WHERE athlete_id=?",(athlete_id,))
    data = sorted([float(row[0]) for row in results.fetchall()])

    response = {'Name': name, 'DOB': dob, 'data': data, 'top3':data[0:3]}
    connection.close()
    return(response)

def add_timing_by_id(athlete_id, value):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    athlete = get_athlete_from_id(athlete_id)
    if float(value) in athlete['data']:
        print('Already exist', file=sys.stderr)
        pass
    else:
        cursor.execute("INSERT INTO timing_data (athlete_id, value) VALUES (?,?)",(athlete_id, value))
        connection.commit()

    connection.close()

def get_all_timing():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("SELECT athlete_id, value FROM timing_data ORDER BY value").fetchall()
    return(results)