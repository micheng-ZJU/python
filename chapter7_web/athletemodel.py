__author__ = 'micheng'

import pickle
from athletelist import AthleteList

def read_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp = data.strip().split(',')
        return AthleteList(temp.pop(0), temp.pop(0), temp)
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        a = read_coach_data(each_file)
        all_athletes[a.name] = a
    try:
        with open('althletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle','rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
    return(all_athletes)
