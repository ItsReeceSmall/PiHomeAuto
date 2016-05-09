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
buzzButton = 16
lsLight = 12

board = Board().board
lcd = LCD1602(board) # Can use 'lcd' as a shortened way to access the lcd1602 class

root = Tk()
print('')
root.title('Home Automation System by Reece Small')
frame = Frame(root)
frame.grid()

def setup():
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
    setup()
    lightState = 'on' # Current state of the light stored in a variable
    counter = 0 # Counter for pir light
    screen = threading.Thread(target=M.ButtonSwitch, args=(fadeLed, lightButton, board, lightState, frame, buzzButton, buzzSensor)).start()
    M.createWidgets(frame, root)
    highTemp = 68
    lowTemp = 63
    lcdyon = 0
    print('')

except (KeyboardInterrupt):
    print('\n \n \n \n### Exiting ###')
    root.destroy()
    lcd.lcd_clear()
    board.cleanup()
    sys.exit()
