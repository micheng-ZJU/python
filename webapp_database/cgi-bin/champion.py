__author__ = 'micheng'

import yate
import athletemodel

print(yate.start_response())
print(yate.include_header("The Champion For Now"))
print(yate.para("Here is the best player among all our athletes:"))


best_record = athletemodel.get_all_timing()[0]
best_timing = best_record[1]
champion = athletemodel.get_athlete_from_id(best_record[0])

print(yate.header(champion['Name'] + ', DOB: ' + champion['DOB'] +'.'))

print(yate.para('The entire set of timing data is: '+str(champion['data'])+' (duplicates removed).'))

print(yate.header("The best time is: <b>" + best_timing + "</b>"))
print(yate.include_footer({"Home": "/index.html", "Select another athlete": "generate_list.py"}))

