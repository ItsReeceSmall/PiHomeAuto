import time, sys, threading, os, glob
from bottle import *
import json, inspect
from board import Board
import pins
import methods as M # All methods stored here
from lcd1602 import LCD1602
from tkinter import *

board = Board().board
lcd = LCD1602(board)

s = [100,100,100]
#enable bottle debug
debug(True)
# WebApp route path
routePath = ''
# get directory of WebApp (bottleJQuery.py's dir)
rootPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

@route('/about', method='GET')
def about():
    data = {}
    data['abouttext'] = M.abouttext
    data['toggle'] = M.toggle
    data['slider'] = M.slider
    data['button'] = M.button
    data['txt'] = M.txt
    data['label'] = M.label
    json_data = json.dumps(data)
    return json_data

@route(routePath)
def rootHome():
    return redirect(routePath+'/index.html')

@route(routePath + '/<filename:re:.*\.html>')
def html_file(filename):
    return static_file(filename, root=rootPath)

@route('/lcdclear', method='POST')
def lcdclear():
    lcd.lcd_clear()

@route('/led', method='POST')
def action():
    r = request.forms.get('rValue')
    r = float(r) / 2.55
    int(round(r))
    print('DEBUG: red value = ' + str(r))
    g = request.forms.get('gValue')
    g = float(g) / 2.55
    int(round(g))
    print('DEBUG: green value = ' + str(g))
    b = request.forms.get('bValue')
    b = float(b) / 2.55
    int(round(b))
    print('DEBUG: blue value = ' + str(b))
    led = request.forms.get('buttonState')
    print('DEBUG: led state = ' + str(led))
    on = bool(int(led))
    print('DEBUG: buttonState = ' + str(on))
    print (type(led))
    if led == '0':
        R = M.P(M.rgbR, board, 0).PWMLED()
        G = M.P(M.rgbG, board, 0).PWMLED()
        B = M.P(M.rgbB, board, 0).PWMLED()
        return
    if led == '1':
        R = M.P(M.rgbR, board, int(r)).PWMLED()
        G = M.P(M.rgbG, board, int(g)).PWMLED()
        B = M.P(M.rgbB, board, int(b)).PWMLED()
    else:
        print('error')

@route('/text', method='POST')
def getText():
    text1 = request.forms.get('texttodisplay1')
    text2 = request.forms.get('texttodisplay2')
    print('------------------------------------------------------------')
    print('DEBGUG: text1 = ' + str(text1) + '\n' + 'DEBGUG: text2 = ' + str(text2))
    print('------------------------------------------------------------')
    lcd.lcd_string(text1, lcd.LCD_LINE_1)
    lcd.lcd_string(text2, lcd.LCD_LINE_2)
    lcd1Label = Label(frame, text=(text1), borderwidth=1, width=17, fg='white', bg='blue', height=1,anchor=W, justify=LEFT)
    lcd1Label.grid(row=13, column=1, padx=5, pady=5)  # Allignment on the grid
    lcd2Label = Label(frame, text=(text2), borderwidth=1, width=17, fg='white', bg='blue', height=1, anchor=W,justify=LEFT)
    lcd2Label.grid(row=14, column=1, padx=5, pady=5)

@route('/setup', method='GET')
def setup():
    print('------------------------------------------------------------')
    t, p, l, d, trgb, lslight = M.getAll(0, frame)
    t = str(t)
    p = str(p)
    l = str(l)
    d = str(d)
    trgb = str(trgb)
    lslight = str(lslight)
    print('------------------------------------------------------------')
    ###
    data = {}
    data['temp'] = t
    data['pir'] = p
    data['lightsensor'] = l
    data['distance'] = d
    data['trgb'] = trgb
    data['lslight'] = lslight
    json_data = json.dumps(data)
    return json_data

@route('/buzz', method='POST')
def BuzzerControl():
    r = request.forms.get('buzzVal')
    Buzzer = request.forms.get('buttonState')
    print('DEBUG: Buzzer state = ' + str(Buzzer))
    on = bool(int(Buzzer))
    print('DEBUG: buttonState = ' + str(on))
    if on:
        M.b(M.buzzSensor, board).buzzOn()
    else:
        M.b(M.buzzSensor, board).buzzOff()

@route('/ring', method='POST')
def ringbuzzer():
    print('DEBUG: Ringing Doorbell')
    M.b(M.buzzSensor, board).buzzTest()

@route('/vls', method='POST')
def vls():
    brightness = request.forms.get('VLB')
    VLS = request.forms.get('buttonState')
    print('DEBUG: VLS state = ' + str(VLS))
    print('DEBUG: Brightness Slider = ' + str(brightness))
    on = bool(int(VLS))
    print('DEBUG: buttonState = ' + str(on))
    if VLS == '1':
        light = M.P(M.fadeLed, board, int(brightness)).PWMLED()
    else:
        light = M.P(M.fadeLed, board, 0).PWMLED()

@route('/pirs', method='POST')
def pirs():
    PIRS = request.forms.get('buttonState')
    print('DEBUG: PIRS state = ' + str(PIRS))
    on = bool(int(PIRS))
    print('DEBUG: buttonState = ' + str(on))
    if on:
        M.l(M.pirLight, board, 0).LedOn()
    else:
        M.l(M.pirLight, board, 0).LedOff()

@route('/lsls', method='POST')
def lsls():
    LSLS = request.forms.get('buttonState')
    print('DEBUG: LSLS state = ' + str(LSLS))
    on = bool(int(LSLS))
    print('DEBUG: buttonState = ' + str(on))
    if on:
        M.l(M.lsLight, board, 0).LedOn()
    else:
        M.l(M.lsLight, board, 0).LedOff()

@route('/exit', method='POST')
def exit():
    sys.stderr.close()
    lcd.lcd_clear()
    board.cleanup()
    sys.exit()

highTemp = 68
lowTemp = 63

root = Tk()
print('')
root.title('Home Automation System by Reece Small')
frame = Frame(root)
frame.grid()

try:
    M.pisetup()
    #screen = threading.Thread(target=M.ButtonSwitch, args=(fadeLed, lightButton, board, lightState, frame, buzzButton, buzzSensor)).start()
    M.createWidgets(frame, root)
    M.mainWidgets(frame)
    print('')
    light = M.l(M.fadeLed, board, 100).PWMLED()  # Starts the light connected to the variable resistor
    #threading.Thread(target=run(host='0.0.0.0', port=8080, reloader=False).start()) # BOTTLE
    #threading.Thread(target=root.mainloop().start())
    run(host='0.0.0.0', port=8080, reloader=False)
    #root.mainloop()
    print('\n \n### Exiting ###')
    lcd.lcd_clear()
    board.cleanup()
    sys.exit()
except (KeyboardInterrupt):
    print('\n \n \n \n### Exiting ###')
    root.destroy()
    lcd.lcd_clear()
    board.cleanup()
    sys.exit()
