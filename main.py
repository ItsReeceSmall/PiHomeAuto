import RPi.GPIO as gpio
import time, os, sys, glob
# FILES IMPORT BELOW
from board import Board
import pins
#from LedClass import led as l
from tempClass import Temp as t
#from distClass import Dist as d
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
#dtSensor = 
#deSensor =
pirSensor = 32

lcd = LCD1602()
rpi = Board()

def setup():
    gpio.setmode(gpio.BOARD)    #set GPIO up
    gpio.setwarnings(False)
    inputs = [tempSensor,humidSensor,pirSensor]   # Set there categories in arrays
    outputs = [powerLed,tempLed]
    print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
    pins.Pins(inputs, outputs)    #Set up pins from a class
    print('### ALL PINS ARE IMPORTED AND SETUP SUCCESSFULLY ###')

def getTemp():
    c, f = t.read_temp() # Get temp values
    ct = str(int(c))     # converts degrees c to string
    ft = str(int(f))     # converts degrees f to string
    temp = (ct + ' C & ' + ft + ' F') # creates compiled string of temperature values
    lcd.lcd_string('Temperature', lcd.LCD_LINE_1)
    lcd.lcd_string(msg, lcd.LCD_LINE_2)
    return temp
    
setup()
getTemp()
time.sleep(2)
lcd.lcd_string('swap', lcd.LCD_LINE_1)
lcd.lcd_string('close', lcd.LCD_LINE_2)
time.sleep(3)
#ledrun = LedClass.Led(powerLed)
