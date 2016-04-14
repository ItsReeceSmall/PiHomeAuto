import RPi.GPIO as gpio
import os, time, sys, glob
from lcd1602 import LCD1602
from board import Board

board = Board().board
lcd = LCD1602(board)

class Buzz:
    def __init__(self, buzzSensor, board):
        self.board = board
        self.buzzSensor = buzzSensor
        self.buzzMethod()

    def buzzMethod(self):
        lcd.lcd_string('Presence', lcd.LCD_LINE_1)
        lcd.lcd_string('Detected', lcd.LCD_LINE_2)
        gpio.output(buzzSensor, gpio.HIGH)  # Buzzer On
        time.sleep(2)
        gpio.output(buzzSensor, gpio.LOW)   # Buzzer Off
        lcd.lcd_clear()                     # Clear LCD

if __name__ == "__main__":
    gpio.setmode(gpio.BOARD)
    buzzSensor = 35
    gpio.setup(buzzSensor, gpio.OUT)
    b = Buzz(buzzSensor, board)
    #b.buzzMethod()