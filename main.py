import time, sys, threading, os, glob
from board import Board
import pins
import methods as M # All methods stored here
from lcd1602 import LCD1602
from tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.grid()

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

        def setup():
            board.setmode(board.BOARD)    #set GPIO up
            inputs = [tempSensor, pirSensor, deSensor]   # Set there categories in arrays
            outputs = [pirLight, tempLed, dtSensor, buzzSensor, fadeLed, lightSensor, ledBlue, ledGreen, ledRed]
            buttons = [lightButton, nextButton, backButton]
            print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
            pins.Pins(inputs, outputs, buttons, board, time)    #Set up pins from a class
            print('### ALL THE PINS ARE IMPORTED AND SETUP ###')
            board.output(fadeLed, board.HIGH) # Starts the light connected to the variable resistor

        try:
            M.tempSet()
            setup()
            lightState = 'on' # Current state of the light stored in a variable
            counter = 0 # Counter for pir light
            loopVal = 1 # Shows what loop the program is on
            screen = 0
            screen = threading.Thread(target=M.lightSwitch, args=(fadeLed, lightButton, board, lightState, nextButton, backButton, screen)).start()
            M.createWidgets()
            highTemp = 68
            lowTemp = 64
            print('')
            while True:
                if loopVal >= 2:
                    for i in range(1,7):
                        sys.stdout.write("\033[F")
                print('### Loop ' + str(loopVal) + ' ###')
                loopVal = loopVal + 1
                Label(frame, text=('Loop ' + str(loopVal)), borderwidth=1).grid(row=2, column=2,padx=5, pady=5)
                pir, counter = M.getPir(pirSensor, board, counter, pirLight, buzzSensor)
                Label(frame, text=(pir), borderwidth=1).grid(row=3, column=2, padx=5, pady=5)
                temp, far = M.getTemp()
                Label(frame, text=(temp), borderwidth=1).grid(row=4, column=2, padx=5, pady=5)
                M.tempLight(far, board, ledRed, ledGreen, ledBlue, highTemp, lowTemp)
                light = M.getLight(lightSensor, board)
                Label(frame, text=(light), borderwidth=1).grid(row=5, column=2, padx=5, pady=5)
                dist = M.getDist(dtSensor, deSensor, board)
                Label(frame, text=(dist), borderwidth=1).grid(row=6, column=2, padx=5, pady=5)
                print (screen)
                lcd.lcd_string('C  F  Pir Dis Cm', lcd.LCD_LINE_1)
                lcd.lcd_string(temp + ' ' + pir + ' ' + str(dist), lcd.LCD_LINE_2)
                #root.after(200, frame.quit)
                root.mainloop()
        except (KeyboardInterrupt, SystemExit):
            print('\n \n \n \n### Ctrl-C Pressed: Exiting ###')
            time.sleep(0.1)
            root.destroy()
            lcd.lcd_clear()
            board.cleanup()
            sys.exit()

root = Tk()
print('')
root.title('Home Automation System v0.3 by Reece Small')
app = App(root)