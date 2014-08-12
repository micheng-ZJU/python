__author__ = 'micheng'


import pickle

man = []
other =[]

try:
    with open('sketch.txt') as data:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(':',1)
                line_spoken = line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Other Man':
                    other.append(line_spoken)
            except ValueError:
                pass
except IOError as err:
    print('File error' + str(err))

try:
    with open('man_data.txt', "wb") as man_file:
        pickle.dump(man, man_file)
    with open('other_data.txt', "wb") as other_file:
        pickle.dump(other, other_file)
except IOError as err:
    print('File Error: '+str(err))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))
