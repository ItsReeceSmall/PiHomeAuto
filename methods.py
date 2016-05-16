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
from tkinter import *
from tkinter import messagebox
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
    outputs = [pirLight, tempLed, dtSensor, buzzSensor, fadeLed, lightSensor, ledBlue, ledGreen, ledRed, lsLight]
    buttons = [lightButton, buzzButton]
    print(split)
    print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
    Pins(inputs, outputs, buttons, board, time)    #Set up pins from a class
    print('### ALL THE PINS ARE IMPORTED AND SETUP ###')
    print(split)
    print('### RUNNING HOME AUTOMATION IN GUI MODE ###')
    print(split)

def mainWidgets(frame):
##################################################################################################################################
    pirBut = Button(frame, text=('Get Pir'), borderwidth=1, width=11, command=lambda: getPir(pirSensor, board, pirLight, buzzSensor, frame))
    pirBut.grid(row=3, column=3, padx=5,pady=5)
    tempBut = Button(frame, text=('Get Temperature'), borderwidth=1, width=11, command=lambda: getTemp(frame, board, ledRed, ledGreen, ledBlue, highTemp, lowTemp))
    tempBut.grid(row=4, column=3, padx=5, pady=5)
    lightSenseBut = Button(frame, text=('Get Light Val'), borderwidth=1, width=11, command=lambda: getLight(lightSensor, board, frame, lsLight))
    lightSenseBut.grid(row=5, column=3, padx=5, pady=5)
    distBut = Button(frame, text=('Get Distance'), borderwidth=1, width=11, command=lambda: getDist(dtSensor, deSensor, board, frame))
    distBut.grid(row=6, column=3, padx=5, pady=5)
    doAll = Button(frame, text=('Get All Values'), borderwidth=1, width=11, command=lambda: getAll(0, frame))
    doAll.grid(row=1,column=3,padx=2,pady=5)
    p2lcd = Button(frame, text=('View Sensor Data'), borderwidth=1, command=lambda: getAll(1, frame))
    p2lcd.grid(row=15, column=1,padx=5, pady=5)
    #startAuto = Button(frame, text=('Start Automation'), borderwidth=1, command=lambda: runAuto(1)).grid(row=16,column=1,padx=5,pady=5)
    #startAuto1 = Button(frame, text=('Stop Automation'), borderwidth=1, command=lambda: runAuto(2)).grid(row=16,column=2,padx=5, pady=5)
    ##################################################################################################################################
##########################################################################################################
def getAll(lcdyon, frame):
    list, c = getTemp(frame, board, ledRed, ledGreen, ledBlue, highTemp, lowTemp) # Gets the values needed for the print of values
    pir = getPir(pirSensor, board, pirLight, buzzSensor, frame)                   #
    light, ls = getLight(lightSensor, board, frame, lsLight)                                   #
    dist = getDist(dtSensor, deSensor, board, frame)                              #
    layoutString = ('C  PIR Dis Light')
    theString = (str(c) + ' ' + str(pir) + ' ' + str(dist) + '  ' + str(light)) # String for the LCD screen
    if lcdyon == 1:
        lcd1Label = Label(frame, text=(layoutString), borderwidth=1, width=17, fg='white', bg='blue', height=1, anchor=W,justify=LEFT)
        lcd1Label.grid(row=13, column=1, padx=5, pady=5) # Allignment on the grid
        lcd2Label = Label(frame, text=(theString), borderwidth=1, width=17, fg='white', bg='blue', height=1, anchor=W,justify=LEFT)
        lcd2Label.grid(row=14, column=1, padx=5, pady=5)
        lcd.lcd_string('C  PIR Dis Light',lcd.LCD_LINE_1)
        lcd.lcd_string(str(c) + ' ' + str(pir) + ' ' + str(dist) + '  ' + str(light),lcd.LCD_LINE_2)
    return c, pir, light, dist
##########################################################################################################
def tempSet():
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'
##########################################################################################################
def createWidgets(frame, root):
    ##################################################
    #titleLabel = Label(frame, text=('Home\nAutomation\nSystem'), borderwidth=1).grid(row=1, column=1, padx=5, pady=5)
    ##################################################
    for i in range(1,4):
        sepLabel = Label(frame, text=('###########'), borderwidth=1).grid(row=2, column=i, padx=5, pady=5)
    ##################################################
    PirLabel = Label(frame, text=('Pir Value: '), borderwidth=1).grid(row=3, column=1, padx=5, pady=5)
    TempLabel = Label(frame, text=('Temperature: '), borderwidth=1).grid(row=4, column=1, padx=5, pady=5)
    LightLabel = Label(frame, text=('Light Sensor Value: '), borderwidth=1).grid(row=5, column=1, padx=5, pady=5)
    DistLabel = Label(frame, text=('Distance: '), borderwidth=1).grid(row=6, column=1, padx=5, pady=5)
    BuzzerLabel = Label(frame, text=('Buzzer: '), borderwidth=1).grid(row=7, column=1, padx=5, pady=5)
    ##################################################
    line1lab = Label(frame, text=('LCD Line 1: '), fg='blue', borderwidth=1).grid(row=8,column=1,padx=5,pady=2)
    line2lab = Label(frame, text=('LCD Line 2: '), fg='blue', borderwidth=1).grid(row=9, column=1, padx=5, pady=2)
    ##################################
    line1 = StringVar(frame, value='')
    lcdLine1 = Entry(frame, bd =2, width=16, textvariable=line1).grid(row=8,column=2,padx=5,pady=2)
    ##################################
    line2 = StringVar(frame, value='')
    lcdLine2 = Entry(frame, bd=2, width=16, textvariable=line2).grid(row=9, column=2, padx=5, pady=2)
    ##################################
    lcdBut = Button(frame, text=('Set Text'), borderwidth=1, width=11, command=lambda: setLcd(line1, line2, frame)).grid(row=8, column=3, padx=5, pady=2)
    lcdClearBut = Button(frame, text=('Clear LCD'), borderwidth=1, width=11, command=lambda: clearLcd(line1, line2, frame)).grid(row=9, column=3, padx=5, pady=2)
    ##################################################
    BuzzButton = Button(frame, text=('Use Buzzer'), borderwidth=1, width=11, command=lambda: testBuzz(board, 35, frame)).grid(row=7,column=3,padx=5,pady=2)
    CloseButton = Button(frame, text=('Quit'), fg=('red'), borderwidth=1, command=lambda: root.quit()).grid(row=1, column=2, padx=5, pady=5)
    HelpButton = Button(frame, text=('Help'), fg=('black'), bg=('yellow'), borderwidth=1, command=lambda: helpscreen).grid(row=1,column=1,padx=5,pady=5)
    ##################################################
    for i in range(1,4):
        sepLabel = Label(frame, text=('###########'), borderwidth=1).grid(row=11, column=i, padx=5, pady=5)
    ##################################################
    lcdLabel = Label(frame, text=('LCD State'),borderwidth=1).grid(row=12,column=1,padx=5,pady=5)
    lcd1Label = Label(frame, text=(line1.get()), borderwidth=1, width=17, fg='white', bg='blue', height=1, anchor=W, justify=LEFT).grid(row=13,column=1,padx=5,pady=5)
    lcd2Label = Label(frame, text=(line2.get()), borderwidth=1, width=17, fg='white', bg='blue', height=1, anchor=W, justify=LEFT).grid(row=14,column=1,padx=5,pady=5)
    ##################################################
#####################################################
def getTemp(frame, board, ledRed, ledGreen, ledBlue, highTemp, lowTemp):
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
    TempValue = Label(frame, text=('              '), borderwidth=1).grid(row=4,column=2,padx=5,pady=5)
    if f <= lowTemp:
        TempValue = Label(frame, text=(gui), fg='blue', borderwidth=1).grid(row=4, column=2, padx=5, pady=5)
    elif f >= highTemp:
        TempValue = Label(frame, text=(gui), fg='red', borderwidth=1).grid(row=4, column=2, padx=5, pady=5)
    else:
        TempValue = Label(frame, text=(gui), fg='green', borderwidth=1).grid(row=4, column=2, padx=5, pady=5)
    tempLight(board, f, ledRed, ledGreen, ledBlue, highTemp, lowTemp)
    c = round(c)
    return tempFin, c
##########################################################################################################
def getDist(dtSensor, deSensor, board, frame):
    dval = d(dtSensor, deSensor, board)
    value = (dval.distValue)
    value = round(value)
    value = str(value)
    sys.stdout.write("\033[K")
    print('### Distance: ' + value)
    DistValue = Label(frame, text=(str(value) + 'cm'), borderwidth=1)
    DistValue.grid(row=6, column=2, padx=5, pady=5)
    return value
##########################################################################################################
def getPir(pirSensor, board, pirLight, buzzSensor, frame):
    pval = p(pirSensor, board, frame)
    value = pval.pirState
    sys.stdout.write("\033[K")
    print ('### PIR Value = ' + str(value) + ' // 1 = on // 0 = off')
    if value == 1:
        finValue = 'ON'
        PirValue = Label(frame, text=(finValue), fg='green', borderwidth=1).grid(row=3, column=2, padx=5, pady=5)
        l(pirLight, board).LedOn() # Turns PIR LIGHT ON
        BuzzValue = Label(frame, text=(' ON '), fg='green', borderwidth=1).grid(row=7,column=2,padx=5,pady=5)
        b(buzzSensor, board).buzzOn()
        time.sleep(0.4)
        BuzzValue = Label(frame, text=(''), borderwidth=1).grid(row=7, column=2, padx=5, pady=5)
        BuzzValue = Label(frame, text=('OFF'), fg='red', borderwidth=1).grid(row=7, column=2, padx=5, pady=5)
        b(buzzSensor, board).buzzOff()
    else:
        finValue = 'OFF'
        PirValue = Label(frame, text=(finValue), fg='red', borderwidth=1).grid(row=3, column=2, padx=5, pady=5)
    BuzzValue = Label(frame, text=('OFF'), fg='red', borderwidth=1).grid(row=7, column=2, padx=5, pady=5)
    return finValue
##########################################################################################################
def getLight(lightSensor, board, frame, lsLight):
    LSV = 0
    lval = L(lightSensor, board, LSV)
    value = lval.LSV
    sys.stdout.write("\033[K")
    if value > 1500:
        lsLightLabel = Label(frame, text=(' ON '), fg='green', borderwidth=1).grid(row=19,column=3,padx=5,pady=5)
        l(lsLight, board).LedOn()
        finValue = 'ON'
    else:
        lsLightLabel = Label(frame, text=('OFF'), fg='red', borderwidth=1).grid(row=19, column=3, padx=5, pady=5)
        l(lsLight, board).LedOff()
        finValue = 'OFF'
    print ('### Light Sensor Value = ' + str(value))
    LightValue = Label(frame, text=(value), borderwidth=1)
    LightValue.grid(row=5, column=2, padx=5, pady=5)
    return value, finValue
##########################################################################################################
def ButtonSwitch(fadeLed, lightButton, board, lightState, frame, buzzSensor, buzzButton):
    while True:
        time.sleep(0.05)
        if board.input(lightButton) == False:
            if lightState == 'on':
                lsta = Label(frame, text=('OFF'), borderwidth=1, fg=('red')).grid(row=14,column=2,padx=5,pady=5)
                l(fadeLed, board).LedOff()
                lightState = 'off'
            elif lightState == 'off':
                lsta = Label(frame, text=(' ON '), borderwidth=1, fg=('green')).grid(row=14, column=2, padx=5, pady=5)
                l(fadeLed, board).LedOn()
                lightState = 'on'
        if board.input(buzzButton) == False:
            doorbell = Label(frame, text=(' ON '), borderwidth=1, fg=('green'))
            doorbell.grid(row=16, column=2, padx=5, pady=5)
            for i in range(1,6):
                b(buzzSensor, board).buzzOn()
                time.sleep(0.1)
                b(buzzSensor, board).buzzOff()
            doorbell = Label(frame, text=('OFF'), borderwidth=1, fg=('red'))
            doorbell.grid(row=16, column=2, padx=5, pady=5)
##########################################################################################################
def tempLight(board, f, ledRed, ledGreen, ledBlue, highTemp, lowTemp):
    if f <= lowTemp:
        l(ledBlue, board).LedOn()
        l(ledGreen, board).LedOff()
        l(ledRed, board).LedOff()
    elif f >= highTemp:
        l(ledRed, board).LedOn()
        l(ledGreen, board).LedOff()
        l(ledBlue, board).LedOff()
    else:
        l(ledGreen, board).LedOn()
        l(ledRed, board).LedOff()
        l(ledBlue, board).LedOff()
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
def setLcd(line1, line2, frame):
    lcd.lcd_string(str(line1.get()), lcd.LCD_LINE_1)
    lcd.lcd_string(str(line2.get()), lcd.LCD_LINE_2)
    lcd1Label = Label(frame, text=(' ' + line1.get()), borderwidth=1, width=17, fg='white', bg='blue', height=1, anchor=W, justify=LEFT).grid(row=13,column=1,padx=5,pady=5)
    lcd2Label = Label(frame, text=(' ' + line2.get()), borderwidth=1, width=17, fg='white', bg='blue', height=1, anchor=W, justify=LEFT).grid(row=14,column=1,padx=5,pady=5)
##########################################################################################################
def testBuzz(board, buzzSensor, frame):
    BuzzValue = Label(frame, text=(' ON '), fg='green', borderwidth=1).grid(row=7, column=2, padx=5, pady=5)
    b(buzzSensor, board).buzzTest()
    BuzzValue = Label(frame, text=('OFF'), fg='red', borderwidth=1).grid(row=7, column=2, padx=5, pady=5)
##########################################################################################################
def clearLcd(line1, line2, frame):
    lcd1Label = Label(frame, text=(' '), borderwidth=1, width=17, fg='white', bg='blue', height=1, anchor=W, justify=LEFT).grid(row=13,column=1,padx=5,pady=5)
    lcd2Label = Label(frame, text=(' '), borderwidth=1, width=17, fg='white', bg='blue', height=1, anchor=W, justify=LEFT).grid(row=14,column=1,padx=5,pady=5)
    lcd.lcd_clear()
##########################################################################################################
def helpscreen():
    messagebox.showinfo("Help", "Welcome to the the Home Automation help screen.\n \nClick the buttons on the same row as the modules to recieve the sensor value manually.\n \nUsing the text box's, enter what you want to be displayed on the LCD Screen and press 'Set Text' to display it on screen.\n \n")
##########################################################################################################
##########################################################################################################

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
# Required Variables
highTemp = 68
lowTemp = 63
lightState = 'on' # Current state of the light stored in a variable
lcdyon = 0

### ABOUT STRINGS ###
abouttext = ('Welcome, to my Home Automation system running on Python 3 on my RaspberryPi 2, examples showing how the program works are listed the other cards on this page, when you are finished being shown how the user interface functions. Return to the top of the page, navigate back to the home page and begin using the interface.')
toggle = ("Below is a toggle button, when you click a toggle button it switches between 2 values, they are 'TRUE' and 'FALSE', or it can also be interpreted as 'ON' and 'OFF'. It's primary use in this system is to switch lights and buzzers on and off, toggle the toggle button below to see what it does on this card.")
slider = ("A slider is an object that allows a range to be selected from by the method of sliding the dot to the value you desire, it's purpose in this system is to set the power output to a light to vary the brightness, or to set how much Red, Green or Blue is in an RGB LED. Drag the slider below to see what it does.")
button = ("Buttons are multi-purpose interactive objects in which do something when they are clicked if they are programmed to do so. Buttons on this system generally send values to some of the sensors and pull values from the rest to recieve an output, Buttons on this system are also used for pinging the buzzer to act as a doorbell and ring. Click the button below to see what happenes when it is clicked.")
txt = ("Text box's are used to enter strings of data which can be used in a number of ways, in this program, the text box's are used to enter what will be printed to the LCD screen by the user, the LCD screen has a maximum limit of 16 characters per row. Type below and click the button to print the text.")
label = ("Labels are strings which can be modified through the CSS, HTML and other forms of programming, in this program everything readable is a string and some solid blocks of colour are filled text lines to present a colour coded meaning such as green is on and red is off, below are just some examples of lables.")

light = board.PWM(fadeLed, 100)
light.start(100) # Starts the light connected to the variable resistor