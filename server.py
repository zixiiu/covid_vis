from bottle import route, run, template
from Data.getData import getData
from Graph.getAllGraph import getAllGraph
from Twitter.sendTweet import send
from datetime import datetime
import time
import state


@route('/update')
def update():
    print('update!')
    getData()
    getAllGraph()
    now = datetime.now()
    updated =now.strftime("%m/%d/%Y, %H:%M:%S %p")
    state.setState('last_updated', updated)
    return template('<b>updated</b>!')

@route('/send')
def send():
    updated = state.getState('last_updated')
    tweet = 'Top 10 country, by confirmed case count. Updated '+ str(updated) + ' ET'
    print('send tweet: ', tweet)

    tweet = 'Top 10 country, by death count. Updated '+ str(updated) + ' ET'
    print('send tweet: ', tweet)
    now = datetime.now()
    sent =now.strftime("%m/%d/%Y, %H:%M:%S %p")
    state.setState('last_sent', sent)
    state.setState('last_sent_ampm', now.strftime('%p'))

    return template('<b>sent</b>!')

@route('/reply/<id>')
def reply(id):
    updated = state.getState('last_updated')
    tweet = 'Top 10 country, by confirmed case count. Updated ' + str(updated) + ' ET'
    print('send tweet: ', tweet, '\n reply_to:', id)
    return template('<b>replied!</b>!')

run(host='localhost', port=23333)