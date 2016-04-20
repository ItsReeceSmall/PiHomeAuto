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

board = Board().board
lcd = LCD1602(board)

def tempSet():
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

def getTemp():
    c, f = t.read_temp() # Get temp values
    ct = str(int(c))     # converts degrees c to string
    ft = str(int(f))     # converts degrees f to string
    temp = (ct + ' Celsius & ' + ft + ' Fahrenheit') # creates compiled string of temperature values
    print ('### Temperature: ' + temp)
    tempFin = (ct + ' ' + ft)
    return tempFin, c

def getDist(dtSensor, deSensor, board):
    dval = d(dtSensor, deSensor, board)
    value = (str(dval.distValue))
    print('### Distance: ' + value)
    return value

def getPir(pirSensor, board, counter, pirLight, buzzSensor):
    if counter >= 5:
        l(pirLight, board).LedOff()
        counter = 0
    pval = p(pirSensor, board)
    value = pval.pirState
    print ('### PIR Value = ' + str(value) + ' // 1 = on // 0 = off')
    if value == 1:
        finValue = 'ON '
        l(pirLight, board).LedOn()
        #print ('counter was: ' + str(counter))
        counter = 0
        #print ('counter now is: ' + str(counter))
        b(buzzSensor, board).buzzOn()
        time.sleep(0.4)
        b(buzzSensor, board).buzzOff()
    else:
        finValue = 'OFF'
        counter = (counter + 1)
    return finValue, counter

def getLight(lightSensor, board):
    LSV = 0
    lval = L(lightSensor, board, LSV)
    value = lval.LSV
    print ('### Light Sensor Value = ' + str(value))
    return value

def lightSwitch(fadeLed, lightButton, board, lightState):
    while True:
        time.sleep(0.05)
        if board.input(lightButton) == False:
            if lightState == 'on':
                l(fadeLed, board).LedOff()
                lightState = 'off'
            elif lightState == 'off':
                l(fadeLed, board).LedOn()
                lightState = 'on'
        #elif board.input(backButton) == False:
            #lcd.lcd_clear()
            #board.cleanup()
            #sys.exit()

def tempLight(celcius, board, ledRed, ledGreen, ledBlue):
    if celcius < 18:
        l(ledBlue, board).LedOn()
        l(ledGreen, board).LedOff()
        l(ledRed, board).LedOff()
    elif celcius > 22:
        l(ledRed, board).LedOn()
        l(ledGreen, board).LedOff()
        l(ledBlue, board).LedOff()
    else:
        l(ledGreen, board).LedOn()
        l(ledRed, board).LedOff()
        l(ledBlue, board).LedOff()