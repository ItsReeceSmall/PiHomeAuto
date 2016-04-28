import time, sys, threading, os, glob
from board import Board
import pins
import methods as M # All methods stored here
from lcd1602 import LCD1602
from tkinter import *

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

board = Board().board
lcd = LCD1602(board) # Can use 'lcd' as a shortened way to access the lcd1602 class

root = Tk()
print('')
root.title('Home Automation System v0.3 by Reece Small')
frame = Frame(root)
frame.grid()

def setup():
    split = '###########################################'
    board.setmode(board.BOARD)    #set GPIO up
    inputs = [tempSensor, pirSensor, deSensor]   # Set there categories in arrays
    outputs = [pirLight, tempLed, dtSensor, buzzSensor, fadeLed, lightSensor, ledBlue, ledGreen, ledRed]
    print(split)
    print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
    pins.Pins(inputs, outputs, lightButton, board, time)    #Set up pins from a class
    print('### ALL THE PINS ARE IMPORTED AND SETUP ###')
    print(split)
    print('### RUNNING HOME AUTOMATION IN GUI MODE ###')
    print(split)
    board.output(fadeLed, board.HIGH) # Starts the light connected to the variable resistor

def getAll(lcdyon):
    pir = M.getPir(pirSensor, board, pirLight, buzzSensor, frame)
    list, c = M.getTemp(frame, board, ledRed, ledGreen, ledBlue, highTemp, lowTemp)
    light = M.getLight(lightSensor, board, frame)
    dist = M.getDist(dtSensor, deSensor, board, frame)
    if lcdyon == 1:
        lcd1Label = Label(frame, text=('C  PIR Dis Light'), borderwidth=1, width=17, fg='white', bg='blue', height=1, anchor=W,justify=LEFT)
        lcd1Label.grid(row=13, column=1, padx=5, pady=5)
        lcd2Label = Label(frame, text=(str(c) + ' ' + str(pir) + ' ' + str(dist) + '  ' + str(light)), borderwidth=1, width=17, fg='white', bg='blue', height=1, anchor=W,justify=LEFT)
        lcd2Label.grid(row=14, column=1, padx=5, pady=5)
        lcd.lcd_string('C  PIR Dis Light',lcd.LCD_LINE_1)
        lcd.lcd_string(str(c) + ' ' + str(pir) + ' ' + str(dist) + '  ' + str(light),lcd.LCD_LINE_2)

try:
    M.tempSet()
    setup()
    lightState = 'on' # Current state of the light stored in a variable
    counter = 0 # Counter for pir light
    screen = threading.Thread(target=M.lightSwitch, args=(fadeLed, lightButton, board, lightState, frame)).start()
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
    lightSenseBut = Button(frame, text=('Get Light Val'), borderwidth=1, width=11, command=lambda: M.getLight(lightSensor, board, frame))
    lightSenseBut.grid(row=5, column=3, padx=5, pady=5)
    distBut = Button(frame, text=('Get Distance'), borderwidth=1, width=11, command=lambda: M.getDist(dtSensor, deSensor, board, frame))
    distBut.grid(row=6, column=3, padx=5, pady=5)
    doAll = Button(frame, text=('Get All Values'), borderwidth=1, width=11, command=lambda: getAll(0))
    doAll.grid(row=1,column=3,padx=2,pady=5)
    p2lcd = Button(frame, text=('View Sensor Data'), borderwidth=1, command=lambda: getAll(1))
    p2lcd.grid(row=15, column=1,padx=5, pady=5)
    testbut = Button(frame, text=('test'), borderwidth=1).grid(row=15,column=1,pady=5).pack()
    ##################################################################################################################################
    getAll(0) # Initial Run of the components
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