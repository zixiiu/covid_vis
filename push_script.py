import time
import requests
from datetime import datetime
import state

# #update
# r = requests.get('http://localhost:23333/update')
# if r.status_code != 200:
#     raise ValueError('error updating')

while True:
    #update rules
    do_thing = ''
    #now!
    now = datetime.now()
    tap = now.strftime("%p")
    #last update
    lastUpdateTime = state.getState('last_updated')
    lutDT = datetime.strptime(lastUpdateTime,"%m/%d/%Y, %H:%M:%S %p")
    lastap = lutDT.strftime("%p")

    if tap != lastap:
        do_thing += 'update!'
        r = requests.get('http://localhost:23333/update')


    lastSent = datetime.strptime(state.getState('last_sent'),"%m/%d/%Y, %H:%M:%S %p")
    lastSentAMPM = state.getState('last_sent_ampm')

    if tap != lastSentAMPM:
        do_thing += 'send!'
        r = requests.get('http://localhost:23333/send')


    #he send tweets!

    print(now.strftime("%m/%d/%Y, %H:%M:%S %p") + ': '+ do_thing)
    time.sleep(60)