__author__ = 'micheng'

import cgi
import athletemodel
import yate
import json
import sys

# get data from store and return as a dict {Name: AthleteList} for mobile app

form_data = cgi.FieldStorage()
athlete_id = form_data['which_athlete'].value
athlete = athletemodel.get_athlete_from_id(athlete_id)
print(yate.start_response('application/json'))
# try to dump an AthleteList object but will fail
print(json.dumps(athlete))
