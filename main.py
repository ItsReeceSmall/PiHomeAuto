import RPi.GPIO as gpio
import time, os, sys, glob
# FILES IMPORT BELOW
from board import Board
import pins
#from LedClass import led as l
from tempClass import Temp as t
from distClass import Dist as d
from pirClass import Pir as p
from lcd1602 import LCD1602

#Temp sense setup
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

#Pins
powerLed = 11
tempSensor = 7
tempLed = 10
humidSensor = 37
dtSensor = 36
deSensor = 38
pirSensor = 32

lcd = LCD1602()
rpi = Board()

def setup():
    gpio.setmode(gpio.BOARD)    #set GPIO up
    gpio.setwarnings(False)
    inputs = [tempSensor,humidSensor,pirSensor,deSensor]   # Set there categories in arrays
    outputs = [powerLed,tempLed,dtSensor]
    print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
    pins.Pins(inputs, outputs)    #Set up pins from a class
    print('### ALL PINS ARE IMPORTED AND SETUP SUCCESSFULLY ###')

def getTemp():
    c, f = t.read_temp() # Get temp values
    ct = str(int(c))     # converts degrees c to string
    ft = str(int(f))     # converts degrees f to string
    temp = (ct + ' C & ' + ft + ' F') # creates compiled string of temperature values
    lcd.lcd_string('Temperature', lcd.LCD_LINE_1)
    lcd.lcd_string(temp, lcd.LCD_LINE_2)
    return temp
    
def getDist(dtSensor, deSensor):
    d(dtSensor, deSensor)
    dval = d.distValue
    lcd.lcd_string('Distance', lcd.LCD_LINE_1)
    lcd.lcd_string(dval + 'cm', lcd.LCD_LINE_2)
    return dval
def getPir():
    return value

setup()
try:
    while True:
        getTemp()
        time.sleep(1)
        getDist(dtSensor, deSensor)
except KeyboardInterrupt:
    print('Error exiting')
    lcd.lcd_string('     Ending', lcd.LCD_LINE_1)
    lcd.lcd_string('     Program', lcd.LCD_LINE_2)
    time.sleep(2)
    lcd.lcd_clear()
    lcd.cleanup()
    sys.exit()
    
