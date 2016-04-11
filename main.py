import RPi.GPIO as gpio
import time, os, sys
# FILES IMPORT BELOW
from board import Board
import pins
#from LedClass import led as l
from tempClass import Temp as t
#from distClass import Dist as d
from pirClass import Pir as p
from lcd1602 import LCD1602 as lcd

#Pins
powerLed = 11
tempSensor = 7
tempLed = 10
humidSensor = 37
#dtSensor = 
#deSensor =
pirSensor = 32

rpi = Board()

allPins = [powerLed,tempSensor,tempLed,humidSensor,pirSensor]

def setup():
    gpio.setmode(gpio.BOARD)    #set GPIO up
    #gpio.setwarnings(False)
    inputs = [tempSensor,humidSensor,pirSensor]   # Set there categories in arrays
    outputs = [powerLed,tempLed]
    print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
    thepins = pins.Pins(inputs, outputs)    #Set up pins from a class
    print('### ALL PINS ARE IMPORTED AND SETUP SUCCESSFULLY ###')

setup()
#c = tc.read_temp_c
#print (c)
pResult = p(pirSensor)
print (pResult)
lcd.lcd_string('Temperature', lcd.LCD_LINE_1)
lcd.lcd_string('C ', lcd.LCD_LINE_2)
print (t.read_temp()[0])
print (t.read_temp()[1])
time.sleep(3)
#ledrun = LedClass.Led(powerLed)
