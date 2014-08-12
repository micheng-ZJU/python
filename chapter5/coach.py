__author__ = 'micheng'

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (min, sec) = time_string.split(splitter)
    return (min + '.' + sec)

def read_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error: '+str(ioerr))
        return None

james = read_coach_data('james.txt')
julie = read_coach_data('julie.txt')
mikey = read_coach_data('mikey.txt')
sarah = read_coach_data('sarah.txt')

print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])