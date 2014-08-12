
import android
import json
import time

from urllib import urlencode
from urllib import urlopen

hello_msg     = "Welcome to NUAC's Timing App"
list_title    = 'Here is your list of athletes:'
quit_msg      = "Quitting NUAC's App."
web_server    = 'http://10.197.38.208:8080'
get_names_cgi = '/cgi-bin/generate_names.py'
get_data_cgi  = '/cgi-bin/generate_data_mobile.py'

# Send a request and post data to web server. And return web response, in this case which is a JSON
def send_to_server(url, post_data=None):
    if post_data:
        page = urlopen(url, urlencode(post_data))
    else:
        page = urlopen(url)
    return(page.read())#.decode("utf8"))

app = android.Android()

def status_update(msg, how_long=2):
    app.makeToast(msg)
    time.sleep(how_long)

status_update(hello_msg,1)

# Open "http://xx.xx.xx.xx:8080/cgi-bin/generate_name.py", get the JSON response and transfer it to a list
athletes = sorted(json.loads(send_to_server(web_server + get_names_cgi)))
athlete_names = [ath[0] for ath in athletes]
app.dialogCreateAlert(list_title)
app.dialogSetSingleChoiceItems(athlete_names)
app.dialogSetPositiveButtonText('Select')
app.dialogSetNegativeButtonText('Quit')
app.dialogShow()
resp = app.dialogGetResponse().result
if resp['which'] in ('positive'):
    # index of selected items
    selected_athlete = app.dialogGetSelectedItems().result[0]
    # selected athlete's id
    which_athlete = athletes[selected_athlete][1]

    athlete = json.loads(send_to_server(web_server + get_data_cgi, {'which_athlete':which_athlete}))

    athlete_title = athlete['Name'] + ' (' + athlete['DOB'] + '), top 3 times:'
    app.dialogCreateAlert(athlete_title)
    app.dialogSetItems(athlete['top3'])
    app.dialogSetPositiveButtonText('OK')
    # add a button
    app.dialogSetNegativeButtonText('Add Time')
    app.dialogShow()
    resp = app.dialogGetResponse().result
    if resp['which'] in ('positive'):
        pass
    elif resp['which'] in ('negative'):
        timing_title = 'Enter a new time'
        timing_msg = 'Provide a new timing value for ' + athlete['Name'] +': '
        add_time_cgi = '/cgi-bin/add_timing_data.py'
        resp = app.dialogGetInput(timing_title, timing_msg).result
        print(resp)

        if resp is not None:
            new_time = resp
            # which_athlete not changed
            send_to_server(web_server+add_time_cgi, {'Time':new_time, 'Athlete':which_athlete})



status_update(quit_msg)

