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
    lcd.lcd_string(text, lcd.LCD_LINE_1)

@route('/setup', method='GET')
def setup():
    notwanted, t = M.getTemp(frame, board, ledBlue, ledGreen, ledRed, highTemp, lowTemp)
    t = str(int(t))
    ###
    p = M.getPir(pirSensor, pirLight, board, buzzSensor, frame)
    p = str(p)
    ###
    l = M.getLight(lightSensor, board, frame, lsLight)
    l = str(int(l))
    ###
    d = M.getDist(dtSensor, deSensor, board, frame)
    d = str(int(d))
    ##
    data = {}
    data['temp'] = t
    data['pir'] = p
    data['lightsensor'] = l
    data['distance'] = d
    json_data = json.dumps(data)
    return json_data
#Pins
tempSensor = 7
tempLed = 23
dtSensor = 29
deSensor = 31
pirSensor = 32
buzzSensor = 35
fadeLed = 11
lightButton = 22
lightSensor = 18
pirLight = 10
ledRed = 36
ledGreen = 38
ledBlue = 40
buzzButton = 16
lsLight = 12

root = Tk()
print('')
root.title('Home Automation System by Reece Small')
frame = Frame(root)
frame.grid()

def pisetup():
    split = '###########################################'
    board.setmode(board.BOARD)    #set GPIO up
    inputs = [tempSensor, pirSensor, deSensor]   # Set there categories in arrays
    outputs = [pirLight, tempLed, dtSensor, buzzSensor, fadeLed, lightSensor, ledBlue, ledGreen, ledRed, lsLight]
    buttons = [lightButton, buzzButton]
    print(split)
    print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
    pins.Pins(inputs, outputs, buttons, board, time)    #Set up pins from a class
    print('### ALL THE PINS ARE IMPORTED AND SETUP ###')
    print(split)
    print('### RUNNING HOME AUTOMATION IN GUI MODE ###')
    print(split)
    board.output(fadeLed, board.HIGH) # Starts the light connected to the variable resistor

def getAll(lcdyon):
    pir = M.getPir(pirSensor, board, pirLight, buzzSensor, frame)                   #
    list, c = M.getTemp(frame, board, ledRed, ledGreen, ledBlue, highTemp, lowTemp) # Gets the values needed for the print of values
    light = M.getLight(lightSensor, board, frame, lsLight)                                   #
    dist = M.getDist(dtSensor, deSensor, board, frame)                              #
    theString = (str(c) + ' ' + str(pir) + ' ' + str(dist) + '  ' + str(light)) # String for the LCD screen
    if lcdyon == 1:
        lcd1Label = Label(frame, text=('C  PIR Dis Light'), borderwidth=1, width=17, fg='white', bg='blue', height=1, anchor=W,justify=LEFT)
        lcd1Label.grid(row=13, column=1, padx=5, pady=5) # Allignment on the grid
        lcd2Label = Label(frame, text=(theString), borderwidth=1, width=17, fg='white', bg='blue', height=1, anchor=W,justify=LEFT)
        lcd2Label.grid(row=14, column=1, padx=5, pady=5)
        lcd.lcd_string('C  PIR Dis Light',lcd.LCD_LINE_1)
        lcd.lcd_string(str(c) + ' ' + str(pir) + ' ' + str(dist) + '  ' + str(light),lcd.LCD_LINE_2)


try:
    M.tempSet()
    pisetup()
    lightState = 'on' # Current state of the light stored in a variable
    counter = 0 # Counter for pir light
    screen = threading.Thread(target=M.ButtonSwitch, args=(fadeLed, lightButton, board, lightState, frame, buzzButton, buzzSensor)).start()
    M.createWidgets(frame, root)
    highTemp = 68
    lowTemp = 63
    lcdyon = 0
    print('')
    ##################################################################################################################################
    pirBut = Button(frame, text=('Get Pir'), borderwidth=1, width=11, command=lambda: M.getPir(pirSensor, board, pirLight, buzzSensor, frame))
    pirBut.grid(row=3, column=3, padx=5,pady=5)
    tempBut = Button(frame, text=('Get Temperature'), borderwidth=1, width=11, command=lambda: M.getTemp(frame, board, ledRed, ledGreen, ledBlue, highTemp, lowTemp))
    tempBut.grid(row=4, column=3, padx=5, pady=5)
    lightSenseBut = Button(frame, text=('Get Light Val'), borderwidth=1, width=11, command=lambda: M.getLight(lightSensor, board, frame, lsLight))
    lightSenseBut.grid(row=5, column=3, padx=5, pady=5)
    distBut = Button(frame, text=('Get Distance'), borderwidth=1, width=11, command=lambda: M.getDist(dtSensor, deSensor, board, frame))
    distBut.grid(row=6, column=3, padx=5, pady=5)
    doAll = Button(frame, text=('Get All Values'), borderwidth=1, width=11, command=lambda: getAll(0))
    doAll.grid(row=1,column=3,padx=2,pady=5)
    p2lcd = Button(frame, text=('View Sensor Data'), borderwidth=1, command=lambda: getAll(1))
    p2lcd.grid(row=15, column=1,padx=5, pady=5)
    #startAuto = Button(frame, text=('Start Automation'), borderwidth=1, command=lambda: runAuto(1)).grid(row=16,column=1,padx=5,pady=5)
    #startAuto1 = Button(frame, text=('Stop Automation'), borderwidth=1, command=lambda: runAuto(2)).grid(row=16,column=2,padx=5, pady=5)
    ##################################################################################################################################
    getAll(0) # Initial Run of the components
    run(host='0.0.0.0', port=8080, reloader=True) # BOTTLE
    root.mainloop()
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
