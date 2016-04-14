import RPi.GPIO as gpio
import os, time, sys, glob
from lcd1602 import LCD1602

lcd = LCD1602()

class Buzz:
    def __init__(self, buzzSensor):
        self.buzzSensor = buzzSensor
        self.buzzMethod()
        
    def buzzMethod(self):
        gpio.output(buzzSensor, gpio.HIGH)
        time.sleep(2)
        gpio.output(buzzSensor, gpio.LOW)

if __name__ == "__main__":
    gpio.setmode(gpio.BOARD)
    buzzSensor = 35
    gpio.setup(buzzSensor, gpio.OUT)
    b = Buzz(buzzSensor)
    b.buzzMethod()
