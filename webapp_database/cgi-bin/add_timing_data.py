__author__ = 'micheng'

import os
import cgi
import time
import sys
import yate
import sqlite3
from athletelist import AthleteList
import athletemodel

print(yate.start_response('text/plain'))
# addr = os.environ['REMOTE_ADDR']
# host = os.environ['REMOTE_HOST']
# method = os.environ['REQUEST_METHOD']
# cur_time = time.asctime(time.localtime())
# print(host+', '+addr+', '+cur_time+': '+method+': ', end='',file=sys.stderr)

form = cgi.FieldStorage()
# for each_form_item in form.keys():
#     print(each_form_item+' -> '+form[each_form_item].value, end=' ',file=sys.stderr)
# print(file=sys.stderr)

the_id = form['Athlete'].value
the_time = form['Time'].value

# unify the format
the_time = AthleteList.sanitize(the_time)

athletemodel.add_timing_by_id(the_id, the_time)

# connection = sqlite3.connect('coachdata.sqlite')
# cursor = connection.cursor()
# athlete = athletemodel.get_athlete_from_id(the_id)
# remember we have changed data format in athletemodel


# if float(the_time) in athlete['data']:
#     print('Already exist', file=sys.stderr)
#     pass
# else:
#     cursor.execute("INSERT INTO timing_data (athlete_id, value) VALUES (?,?)",(the_id, the_time))
#     connection.commit()
#
#     # results = cursor.execute("SELECT value FROM timing_data WHERE athlete_id=3")
#     # validate_values = [row[0] for row in results.fetchall()]
#     # print(validate_values,file=sys.stderr)
#     connection.close()
#     print('OK.')