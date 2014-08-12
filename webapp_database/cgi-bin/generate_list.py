__author__ = 'micheng'

import athletemodel
import yate
import glob
import cgitb

athletes = athletemodel.get_namesID_from_store()

print(yate.start_response())
print(yate.include_header("NUAC's List of Athletes"))
print(yate.start_form("generate_data_web.py"))
print(yate.para("Select an athlete from the list to work with:"))

for each_athlete in sorted(athletes):
    print(yate.radio_button_id("which_athlete", each_athlete[0], str(each_athlete[1])))
print(yate.end_form("Select"))

print(yate.include_footer({"See the Champion": "/cgi-bin/champion.py"}))

print(yate.include_footer({"Home":"/index.html"}))
