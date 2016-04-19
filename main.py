import time, os, sys, glob, threading
# FILES IMPORT BELOW
from board import Board
import pins
import methods as M
from lcd1602 import LCD1602

#Pins
tempSensor = 7
tempLed = 23
dtSensor = 31
deSensor = 29
pirSensor = 32
buzzSensor = 35
fadeLed = 11
lightButton = 22
nextButton = 12
backButton = 16
lightSensor = 18
pirLight = 31
ledRed = 36
ledGreen = 38
ledBlue = 40

board = Board().board
lcd = LCD1602(board)

def setup():
    board.setmode(board.BOARD)    #set GPIO up
    board.setwarnings(False)
    inputs = [tempSensor, pirSensor, deSensor]   # Set there categories in arrays
    outputs = [pirLight, tempLed, dtSensor, buzzSensor, fadeLed, lightSensor, ledBlue, ledGreen, ledRed]
    buttons = [lightButton, nextButton, backButton]
    print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
    pins.Pins(inputs, outputs, buttons, board, time)    #Set up pins from a class
    print('### ALL PINS ARE IMPORTED AND SETUP SUCCESSFULLY ###')
    board.output(fadeLed, board.HIGH)

try:
    M.tempSet()
    setup()
    lightState = 'on'
    counter = 0
    lcd.lcd_string('C  F  Pir Dis Cm', lcd.LCD_LINE_1)
    loopVal = 1
    threading.Thread(target=M.lightSwitch, args=(fadeLed, lightButton, board, lightState)).start()
    threading.Thread(target=M.endButton, args=(board, backButton)).start()
    while True:
        if loopVal >= 2:
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[F")
        print('### Loop ' + str(loopVal) + ' ###')
        #lightState = M.lightSwitch(fadeLed, lightButton, board, lightState)
        #M.endButton(board, backButton)
        loopVal = loopVal + 1
        pir, counter = M.getPir(pirSensor, board, counter, pirLight, buzzSensor)
        temp, celcius = M.getTemp()
        M.tempLight(celcius, board, ledRed, ledGreen, ledBlue)
        light = M.getLight(lightSensor, board)
        #dist = getDist(dtSensor, deSensor, board)
        lcd.lcd_string('C  F  Pir Dis Cm', lcd.LCD_LINE_1)
        lcd.lcd_string(temp + ' ' + pir + ' ' + str(light), lcd.LCD_LINE_2)
except KeyboardInterrupt:
    print('### Ctrl-C Pressed: Exiting ###')
    time.sleep(0.1)
    lcd.lcd_clear()
    lcd.cleanup()
    sys.exit()
