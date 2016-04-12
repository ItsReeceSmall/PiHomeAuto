import RPi.GPIO as gpio
import time, os, sys, glob
from lcd1602 import LCD1602

lcd = LCD1602()

class Bar:
    def __init__(self):
        self.barMethod()
    
    def barMethod(self):
        val = 1
        for i in range(1, 101):
            val = (val + 1)
            print (str(val))
            time.sleep(0.1)
            

if __name__ == "__main__":
    Bar()
    sys.exit()
