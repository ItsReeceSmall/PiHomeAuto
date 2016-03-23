import RPi.GPIO as gpio
import time, os, sys
# FILES IMPORT BELOW
import pins
import LedClass
import tempClass
import lcd1602

#Pins
powerLed = 11
tempSensor = 7
tempLed = 10
humidSensor = 12

allPins = [powerLed,tempSensor,tempLed,humidSensor]

tc = tempClass
lc = LedClass
lcd = lcd1602

def setup():
    gpio.setmode(gpio.BOARD)    #set GPIO up
    #gpio.setwarnings(False)
    inputs = [tempSensor,humidSensor]   # Set there categories in arrays
    outputs = [powerLed,tempLed]
    print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
    thepins = pins.Pins(inputs, outputs)    #Set up pins from a class
    print('### ALL PINS ARE IMPORTED AND SETUP SUCCESSFULLY ###')

setup()
tc.read_temp_c()
#ledrun = LedClass.Led(powerLed)
