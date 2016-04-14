import RPi.GPIO as gpio
import os, time, sys, glob

gpio.setmode(gpio.BOARD)
gpio.setup(35, gpio.OUT)

gpio.output(35, gpio.HIGH)
time.sleep(3)
gpio.output(35, gpio.LOW)
gpio.cleanup()
sys.exit()
