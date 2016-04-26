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
nextButton = 12
backButton = 16
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
    board.setmode(board.BOARD)    #set GPIO up
    inputs = [tempSensor, pirSensor, deSensor]   # Set there categories in arrays
    outputs = [pirLight, tempLed, dtSensor, buzzSensor, fadeLed, lightSensor, ledBlue, ledGreen, ledRed]
    buttons = [lightButton, nextButton, backButton]
    print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
    pins.Pins(inputs, outputs, buttons, board, time)    #Set up pins from a class
    print('### ALL THE PINS ARE IMPORTED AND SETUP ###')
    board.output(fadeLed, board.HIGH) # Starts the light connected to the variable resistor

def getAll():
    M.getPir(pirSensor, board, counter, pirLight, buzzSensor, frame)
    M.getTemp(frame)
    M.getLight(lightSensor, board, frame)
    M.getDist(dtSensor, deSensor, board, frame)

try:
    M.tempSet()
    setup()
    lightState = 'on' # Current state of the light stored in a variable
    counter = 0 # Counter for pir light
    screen = 0
    screen = threading.Thread(target=M.lightSwitch, args=(fadeLed, lightButton, board, lightState, nextButton, backButton, screen)).start()
    M.createWidgets(frame, root)
    highTemp = 68
    lowTemp = 64
    print('')
    '''
    pir, counter = M.getPir(pirSensor, board, counter, pirLight, buzzSensor, frame)
    temp, far = M.getTemp(frame)
    M.tempLight(far, board, ledRed, ledGreen, ledBlue, frame, highTemp, lowTemp)
    light = M.getLight(lightSensor, board, frame)
    dist = M.getDist(dtSensor, deSensor, board, frame)
    lcd.lcd_string('C  F  Pir Dis Cm', lcd.LCD_LINE_1)
    lcd.lcd_string(temp + ' ' + pir + ' ' + str(dist), lcd.LCD_LINE_2)
    '''
    ##################################################################################################################################
    pirBut = Button(frame, text=('Get Pir'), borderwidth=1, width=10, command=lambda: M.getPir(pirSensor, board, counter, pirLight, buzzSensor, frame))
    pirBut.grid(row=3, column=3, padx=5,pady=5)
    tempBut = Button(frame, text=('Get Temp'), borderwidth=1, width=10, command=lambda: M.getTemp(frame))
    tempBut.grid(row=4, column=3, padx=5, pady=5)
    lightSenseBut = Button(frame, text=('Get Light Val'), borderwidth=1, width=10, command=lambda: M.getLight(lightSensor, board, frame))
    lightSenseBut.grid(row=5, column=3, padx=5, pady=5)
    distBut = Button(frame, text=('Get Dist'), borderwidth=1, width=10, command=lambda: M.getDist(dtSensor, deSensor, board, frame))
    distBut.grid(row=6, column=3, padx=5, pady=5)
    doAll = Button(frame, text=('Get All'), borderwidth=1, width=10, command=lambda: getAll)
    doAll.grid(row=1,column=3,padx=2,pady=5)
    ##################################################################################################################################
    root.mainloop()
    frame.quit()
except (KeyboardInterrupt, SystemExit):
    print('\n \n \n \n### Exiting ###')
    root.destroy()
    lcd.lcd_clear()
    board.cleanup()
    sys.exit()