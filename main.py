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
            self.titleLabel = Label(frame, text=('Home Automation System'), borderwidth=1).grid(row=1, column=2,padx=10, pady=10)
            M.tempSet()
            setup()
            lightState = 'on' # Current state of the light stored in a variable
            counter = 0 # Counter for pir light
            loopVal = 1 # Shows what loop the program is on
            screen = 0
            self.PirLabel = Label(frame, text=('Pir Value: '), borderwidth=1).grid(row=3, column=1, padx=10, pady=10)
            self.TempLabel = Label(frame, text=('Temperature: '), borderwidth=1).grid(row=4, column=1, padx=10, pady=10)
            self.LightLabel = Label(frame, text=('Light Sensor Value: '), borderwidth=1).grid(row=5, column=1, padx=10,pady=10)
            self.DistLabel = Label(frame, text=('Distance: '), borderwidth=1).grid(row=6, column=1, padx=10, pady=10)
            screen = threading.Thread(target=M.lightSwitch, args=(fadeLed, lightButton, board, lightState, nextButton, backButton, screen)).start()
            self.close = Button(frame, text="Close", command=frame.quit).grid(row=7, column=2, padx=10, pady=10)
            print('')
            while True:
                if loopVal >= 2:
                    for i in range(1,7):
                        sys.stdout.write("\033[F")
                print('### Loop ' + str(loopVal) + ' ###')
                self.LoopLabel = Label(frame, text=('Loop ' + str(loopVal)), borderwidth=1).grid(row=2, column=2,padx=10, pady=10)
                loopVal = loopVal + 1
                pir, counter = M.getPir(pirSensor, board, counter, pirLight, buzzSensor)
                temp, far = M.getTemp()
                M.tempLight(far, board, ledRed, ledGreen, ledBlue)
                light = M.getLight(lightSensor, board)
                dist = M.getDist(dtSensor, deSensor, board)
                #dist = float(dist)
                print (screen)
                lcd.lcd_string('C  F  Pir Dis Cm', lcd.LCD_LINE_1)
                lcd.lcd_string(temp + ' ' + pir + ' ' + str(dist), lcd.LCD_LINE_2)
                self.PirValue = Label(frame, text=(pir), borderwidth=1).grid(row=3, column=2, padx=10, pady=10)
                self.TempValue = Label(frame, text=(temp), borderwidth=1).grid(row=4, column=2, padx=10, pady=10)
                self.LightValue = Label(frame, text=(light), borderwidth=1).grid(row=5, column=2, padx=10, pady=10)
                self.DistValue = Label(frame, text=(dist), borderwidth=1).grid(row=6, column=2, padx=10, pady=10)
                root.mainloop()
        except (KeyboardInterrupt, SystemExit):
            print('\n \n \n \n### Ctrl-C Pressed: Exiting ###')
            time.sleep(0.1)
            lcd.lcd_clear()
            board.cleanup()
            sys.exit()

root = Tk()
print('')
root.title('Home Automation System v0.3 by Reece Small')
app = App(root)
root.destroy()