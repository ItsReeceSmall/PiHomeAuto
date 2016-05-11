#!/usr/bin/env python
from bottle import route, static_file, debug, run, get, redirect
from bottle import post, request
import os, inspect, json

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
s = [100,100,100]
#enable bottle debug
debug(True)

# WebApp route path
routePath = '/bottle'
# get directory of WebApp (bottleJQuery.py's dir)
rootPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

@route(routePath)
def rootHome():
    return redirect(routePath+'/index.html')

@route(routePath + '/<filename:re:.*\.html>')
def html_file(filename):
    return static_file(filename, root=rootPath)

@route('/text', method='POST')
def getText():
    text = request.forms.get('texttodisplay')
    print('DEBGUG: text = ' + str(text))
    sense.show_message(text)

@route('/setup', method='GET')
def setup():
    t = sense.temp
    t = str(int(t))
    p = sense.pressure
    p = str(int(p))
    h = sense.humidity
    h = str(int(h))
    data = {}
    data['temp'] = t
    data['pressure'] = p
    data['humidity'] = h
    json_data = json.dumps(data)
    return json_data
    #'temp:'+str(int(temp))+',pressure:'+str(int(pressure))+',humidity:'+str(int(humidity))

@route('/led', method='POST')
def action():
    r = request.forms.get('rValue')
    print('DEBUG: red value = ' + str(r))
    g = request.forms.get('gValue')
    print('DEBUG: green value = ' + str(g))
    b = request.forms.get('bValue')
    print('DEBUG: blue value = ' +str(b))
    led = request.forms.get('buttonState')    
    print('DEBUG: led state = ' + str(led))
    global s
    
    on = bool(int(led))
    print('DEBUG: buttonState = ' + str(on))
    if on:    
        s[0] = r
        s[1] = g
        s[2] = b
        print('DEBUG: s = '+ str(s))

        sense.clear(int(s[0]),int(s[1]),int(s[2]))
    else:
        sense.clear()

run(host='0.0.0.0', port=8080, reloader=True)
