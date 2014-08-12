__author__ = 'micheng'

""" this is a script added in chapter 8 (mobile app) """

import athletemodel
import yate
import json

athlete_names = athletemodel.get_namesID_from_store()

print(yate.start_response("application/json"))
print(json.dumps(sorted((athlete_names))))

