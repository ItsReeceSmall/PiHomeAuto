import RPi.GPIO as gpio
import time, os, sys
import pins
import LedClass

#Pins
powerLed = 7
tempSensor = 8
tempLed = 10
humidSensor = 12

allPins = [powerLed,tempSensor,tempLed,humidSensor]
    
def setup():
    gpio.setmode(gpio.BOARD)    #set GPIO up
    #gpio.setwarnings(False)
    inputs = [tempSensor,humidSensor]   # Set there categories in arrays
    outputs = [powerLed,tempLed]
    print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
    thepins = pins.Pins(inputs, outputs)    #Set up pins from a class
    print('### ALL PINS ARE IMPORTED AND SETUP SUCCESSFULLY ###')

setup()
ledrun = LedClass.Led(powerLed)
