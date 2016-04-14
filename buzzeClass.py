import RPi.GPIO as gpio
import os, time, sys, glob
from lcd1602 import LCD1602

lcd = LCD1602()

class Buzz:
    def __init__(self, buzzSensor):
        self.buzzSensor = buzzSensor
        self.buzzMethod()
        
    def buzzMethod(self):
        lcd.lcd_string('Presence', lcd.LCD_LINE_1)
        lcd.lcd_string('        Detected', lcd.LCD_LINE_1)
        gpio.output(buzzSensor, gpio.HIGH)
        time.sleep(0.5)
        gpio.output(buzzSensor, gpio.LOW)
        lcd.lcd_clear()

if __name__ == "__main__":
    gpio.setmode(gpio.BOARD)
    buzzSensor = 35
    gpio.setup(buzzSensor, gpio.OUT)
    b = Buzz(buzzSensor)
    #b.buzzMethod()
