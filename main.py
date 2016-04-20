import time, sys, threading, os, glob
from board import Board
import pins
import methods as M # All methods stored here
from lcd1602 import LCD1602

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
board.setwarnings(False)

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
    lightState = threading.Thread(target=M.lightSwitch, args=(fadeLed, lightButton, board, lightState)).start()
    print('')
    while True:
        #if loopVal >= 2:
            #for i in range(1,6):
                #sys.stdout.write("\033[F")
        #print('### Loop ' + str(loopVal) + ' ###')
        #lightState = M.Buttons(fadeLed, lightButton, board, lightState, backButton)
        #loopVal = loopVal + 1
        #pir, counter = M.getPir(pirSensor, board, counter, pirLight, buzzSensor)
        #temp, far = M.getTemp()
        #M.tempLight(far, board, ledRed, ledGreen, ledBlue)
        #light = M.getLight(lightSensor, board)
        dist = M.getDist(dtSensor, deSensor, board)
        dist  = float(dist)
        #lcd.lcd_string('C  F  Pir Dis Cm', lcd.LCD_LINE_1)
        #lcd.lcd_string(temp + ' ' + pir + ' ' + dist, lcd.LCD_LINE_2)
        M.Closeness(board, buzzSensor, dist)
except (KeyboardInterrupt, SystemExit):
    print('\n \n \n \n### Ctrl-C Pressed: Exiting ###')
    time.sleep(0.1)
    print('lcd clear')
    lcd.lcd_clear()
    #board.cleanup()
    print('sys exit')
    sys.exit()
    print('')
