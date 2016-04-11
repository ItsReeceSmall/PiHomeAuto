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

#allPins = [powerLed,tempSensor,tempLed,humidSensor,pirSensor]

def setup():
    gpio.setmode(gpio.BOARD)    #set GPIO up
    #gpio.setwarnings(False)
    inputs = [tempSensor,humidSensor,pirSensor]   # Set there categories in arrays
    outputs = [powerLed,tempLed]
    print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
    pins.Pins(inputs, outputs)    #Set up pins from a class
    print('### ALL PINS ARE IMPORTED AND SETUP SUCCESSFULLY ###')

setup()

lcd.lcd_string('Temperature', lcd.LCD_LINE_1)
lcd.lcd_string('C ', lcd.LCD_LINE_2)
print (t.read_temp()[0])
print (t.read_temp()[1])
time.sleep(3)
#ledrun = LedClass.Led(powerLed)
