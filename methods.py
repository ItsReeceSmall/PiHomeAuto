import time, os, sys, glob, threading
# FILES IMPORT BELOW

from board import Board
from lightClass import Light as L
from LedClass import Led as l
from tempClass import Temp as t
from distClass import Dist as d
from pirClass import Pir as p
from buzzerClass import Buzz as b
from lcd1602 import LCD1602
from bottle import *
import json, inspect
from pins import Pins

board = Board().board
lcd = LCD1602(board)

def pisetup():
    tempSet()
    split = '###########################################'
    board.setmode(board.BOARD)    #set GPIO up
    inputs = [tempSensor, pirSensor, deSensor]   # Set there categories in arrays
    outputs = [pirLight, dtSensor, buzzSensor, fadeLed, lightSensor, ledBlue, ledGreen, ledRed, lsLight, rgbR, rgbG, rgbB]
    buttons = [lightButton, buzzButton]
    print(split)
    print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
    Pins(inputs, outputs, buttons, board, time)    #Set up pins from a class
    print('### ALL THE PINS ARE IMPORTED AND SETUP ###')
    print(split)
    print('### RUNNING HOME AUTOMATION IN GUI MODE ###')
    print(split)

def pwmpins():
    rpwm = board.PWM(rgbR, 100)
    rpwm.start(0)
    gpwm = board.PWM(rgbG, 100)
    gpwm.start(0)
    bpwm = board.PWM(rgbB, 100)
    bpwm.start(0)
    vpwm = board.PWM(fadeLed, 100)
    vpwm.start(100)
    return rpwm, gpwm, bpwm, vpwm
##########################################################################################################
def getAll(lcdyon):
    list, c, temprgb = getTemp(board, ledRed, ledGreen, ledBlue, highTemp, lowTemp) # Gets the values needed for the print of values
    pir = getPir(pirSensor, board, pirLight, buzzSensor)                   #
    light, ls = getLight(lightSensor, board, lsLight)                                   #
    dist = getDist(dtSensor, deSensor, board)                              #
    layoutString = ('C  PIR Dis Light')
    theString = (str(c) + ' ' + str(pir) + ' ' + str(dist) + '  ' + str(light)) # String for the LCD screen
    if lcdyon == 1:
        lcd.lcd_string('C  PIR Dis Light',lcd.LCD_LINE_1)
        lcd.lcd_string(str(c) + ' ' + str(pir) + ' ' + str(dist) + '  ' + str(light),lcd.LCD_LINE_2)
    return c, pir, light, dist, temprgb, ls
##########################################################################################################
def tempSet():
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'
##########################################################################################################
def getTemp(board, ledRed, ledGreen, ledBlue, highTemp, lowTemp):
    c, f = t.read_temp() # Get temp values
    f = round(f, 2)
    c = round(c, 2)
    ct = str(int(c))     # converts degrees c to string
    ft = str(int(f))     # converts degrees f to string
    temp = (ct + ' Celsius & ' + ft + ' Fahrenheit') # creates compiled string of temperature values
    sys.stdout.write("\033[K")
    print ('### Temperature: ' + temp)
    tempFin = (ct + ' ' + ft)
    gui = (str(c) + ' C ' + str(f) + ' F')
    if f <= lowTemp:
        temprgb = 'blue'
    elif f >= highTemp:
        temprgb = 'red'
    else:
        temprgb = 'green'
    tempLight(board, f, ledRed, ledGreen, ledBlue, highTemp, lowTemp)
    c = round(c)
    return tempFin, c, temprgb
##########################################################################################################
def getDist(dtSensor, deSensor, board):
    dval = d(dtSensor, deSensor, board)
    value = (dval.distValue)
    value = round(value)
    value = str(value)
    sys.stdout.write("\033[K")
    print('### Distance: ' + value)
    return value
##########################################################################################################
def getPir(pirSensor, board, pirLight, buzzSensor):
    pval = p(pirSensor, board)
    value = pval.pirState
    sys.stdout.write("\033[K")
    print ('### PIR Value = ' + str(value) + ' // 1 = on // 0 = off')
    if value == 1:
        finValue = 'ON'
        l(pirLight, board, 0).LedOn() # Turns PIR LIGHT ON
        b(buzzSensor, board).buzzOn()
        time.sleep(0.4)
        b(buzzSensor, board).buzzOff()
    else:
        finValue = 'OFF'
    return finValue
##########################################################################################################
def getLight(lightSensor, board, lsLight):
    LSV = 0
    lval = L(lightSensor, board, LSV)
    value = lval.LSV
    sys.stdout.write("\033[K")
    if value > 1500:
        l(lsLight, board, 0).LedOn()
        finValue = 'ON'
    else:
        l(lsLight, board, 0).LedOff()
        finValue = 'OFF'
    print ('### Light Sensor Value = ' + str(value))
    return value, finValue
##########################################################################################################
def ButtonSwitch(fadeLed, lightButton, board, lightState):
    while True:
        time.sleep(0.1)
        if board.input(lightButton):
            if lightState == 'on':
                l(fadeLed, board, 0).LedOff()
                lightState = 'off'
            elif lightState == 'off':
                l(fadeLed, board, 0).LedOn()
                lightState = 'on'
        else:
            pass
'''
def BuzzSwitch(board, buzzSensor, buzzButton, buzzState):
    while True:
        time.sleep(2)
        if board.input(buzzButton):
            print(board.input(buzzButton))
            print('buzz supposedly on')
            b(buzzSensor, board).buzzOn()
        else:
            print(board.input(buzzButton))
            print('buzz supposedly off')
            b(buzzSensor, board).buzzOff()
        print('========================')
'''
##########################################################################################################
def tempLight(board, f, ledRed, ledGreen, ledBlue, highTemp, lowTemp):
    if f <= lowTemp:
        l(ledBlue, board, 0).LedOn()
        l(ledGreen, board, 0).LedOff()
        l(ledRed, board, 0).LedOff()
    elif f >= highTemp:
        l(ledRed, board, 0).LedOn()
        l(ledGreen, board, 0).LedOff()
        l(ledBlue, board, 0).LedOff()
    else:
        l(ledGreen, board, 0).LedOn()
        l(ledRed, board, 0).LedOff()
        l(ledBlue, board, 0).LedOff()
##########################################################################################################
def Closeness(board, buzzSensor, dist):
    if dist <= 5:
        b(buzzSensor, board).buzzOn()
        time.sleep(0.6)
        b(buzzSensor, board).buzzOff()
    elif dist <= 10:
        b(buzzSensor, board).buzzOn()
        time.sleep(0.45)
        b(buzzSensor, board).buzzOff()
    elif dist <= 15:
        b(buzzSensor, board).buzzOn()
        time.sleep(0.35)
        b(buzzSensor, board).buzzOff()
    elif dist <= 20:
        b(buzzSensor, board).buzzOn()
        time.sleep(0.2)
        b(buzzSensor, board).buzzOff()
    elif dist <= 25:
        b(buzzSensor, board).buzzOn()
        time.sleep(0.1)
        b(buzzSensor, board).buzzOff()
    else:
        b(buzzSensor, board).buzzOn()
        time.sleep(0.03)
        b(buzzSensor, board).buzzOff()
##########################################################################################################
def setLcd(line1, line2):
    lcd.lcd_string(str(line1.get()), lcd.LCD_LINE_1)
    lcd.lcd_string(str(line2.get()), lcd.LCD_LINE_2)
##########################################################################################################
def testBuzz(board, buzzSensor):
    b(buzzSensor, board).buzzTest()
##########################################################################################################
def clearLcd(line1, line2):
    lcd.lcd_clear()
##########################################################################################################

#Pins
tempSensor = 7
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
rgbR = 19
rgbG = 21
rgbB = 23
# Required Variables
highTemp = 68
lowTemp = 63
lightState = 'on' # Current state of the light stored in a variable
buzzState = 'off'
lcdyon = 0

### ABOUT STRINGS ###
abouttext = ('Welcome, to my Home Automation system running on Python 3 on my RaspberryPi 2, examples showing how the program works are listed the other cards on this page, when you are finished being shown how the user interface functions. Return to the top of the page, navigate back to the home page and begin using the interface.')
toggle = ("Below is a toggle button, when you click a toggle button it switches between 2 values, they are 'TRUE' and 'FALSE', or it can also be interpreted as 'ON' and 'OFF'. It's primary use in this system is to switch lights and buzzers on and off, toggle the toggle button below to see what it does on this card.")
slider = ("A slider is an object that allows a range to be selected from by the method of sliding the dot to the value you desire, it's purpose in this system is to set the power output to a light to vary the brightness, or to set how much Red, Green or Blue is in an RGB LED. Drag the slider below to see what it does.")
button = ("Buttons are multi-purpose interactive objects in which do something when they are clicked if they are programmed to do so. Buttons on this system generally send values to some of the sensors and pull values from the rest to recieve an output, Buttons on this system are also used for pinging the buzzer to act as a doorbell and ring. Click the button below to see what happenes when it is clicked.")
txt = ("Text box's are used to enter strings of data which can be used in a number of ways, in this program, the text box's are used to enter what will be printed to the LCD screen by the user, the LCD screen has a maximum limit of 16 characters per row. Type below and click the button to print the text.")
label = ("Labels are strings which can be modified through the CSS, HTML and other forms of programming, in this program everything readable is a string and some solid blocks of colour are filled text lines to present a colour coded meaning such as green is on and red is off.")
