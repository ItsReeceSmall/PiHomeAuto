import RPi.GPIO as gpio
import time, os, sys, glob
# FILES IMPORT BELOW
from board import Board
import pins
#from LedClass import led as l
from tempClass import Temp as t
from distClass import Dist as d
from pirClass import Pir as p
from buzzerClass import Buzz as b
from lcd1602 import LCD1602

#Pins
powerLed = 11
tempSensor = 7
tempLed = 10
dtSensor = 36
deSensor = 38
pirSensor = 32
buzzSensor = 35

board = Board().board
lcd = LCD1602(board)

def tempSet():
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

def setup():
    board.setmode(board.BOARD)    #set GPIO up
    board.setwarnings(False)
    inputs = [tempSensor,pirSensor,deSensor]   # Set there categories in arrays
    outputs = [powerLed,tempLed,dtSensor,buzzSensor]
    print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
    pins.Pins(inputs, outputs, board)    #Set up pins from a class
    print('### ALL PINS ARE IMPORTED AND SETUP SUCCESSFULLY ###')

def getTemp():
    c, f = t.read_temp() # Get temp values
    ct = str(int(c))     # converts degrees c to string
    ft = str(int(f))     # converts degrees f to string
    temp = (ct + ' C & ' + ft + ' F') # creates compiled string of temperature values
    print ('The temperature is: ' + temp)
    lcd.lcd_string('Temperature', lcd.LCD_LINE_1)
    lcd.lcd_string(temp, lcd.LCD_LINE_2)
    return temp
    
def getDist(dtSensor, deSensor):
    dval = d(dtSensor, deSensor, board)
    value = dval.distValue
    lcd.lcd_string('Distance', lcd.LCD_LINE_1)
    lcd.lcd_string(value + 'cm', lcd.LCD_LINE_2)
    return value

def getPir(buzzSensor, pirSensor):
    lcd.lcd_string('Checking', lcd.LCD_LINE_1)
    lcd.lcd_string('PIR Sensor', lcd.LCD_LINE_2)
    pval = p(pirSensor, board)
    value = pval.pirState
    if value == '1':
        b(buzzSensor, board)
    else:
        pass
    lcd.lcd_clear()
    return value

tempSet()
setup()
try:
    while True:
        pir = getPir(pirSensor, buzzSensor)
        temp = getTemp()
        time.sleep(2)
        #dist = getDist(dtSensor, deSensor)
        #time.sleep(10)
except KeyboardInterrupt:
    print('Error exiting')
    lcd.lcd_string('Ending   Program', lcd.LCD_LINE_1)
    lcd.lcd_string('Shutting    Down', lcd.LCD_LINE_2)
    time.sleep(2)
    lcd.lcd_clear()
    lcd.cleanup()
    sys.exit()
    
