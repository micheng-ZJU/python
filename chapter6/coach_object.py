__author__ = 'micheng'

class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])
    def add_time(self, new_time):
        self.times.append(new_time)
    def add_times(self, new_times):
        self.times.extend(new_times)

def read_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp = data.strip().split(',')
        return Athlete(temp.pop(0), temp.pop(0), temp)
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (min, sec) = time_string.split(splitter)
    return (min + '.' + sec)

james = read_coach_data('james2.txt')
julie = read_coach_data('julie2.txt')
mikey = read_coach_data('mikey2.txt')
sarah = read_coach_data('sarah2.txt')

print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))