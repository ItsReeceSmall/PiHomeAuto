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

try:
    M.tempSet()
    M.pisetup()
    #screen = threading.Thread(target=M.ButtonSwitch, args=(fadeLed, lightButton, board, lightState, frame, buzzButton, buzzSensor)).start()
    M.createWidgets(frame, root)
    M.mainWidgets(frame)
    print('')
    #threading.Thread(target=run(host='0.0.0.0', port=8080, reloader=False).start()) # BOTTLE
    #threading.Thread(target=root.mainloop().start())
    M.runme()
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
