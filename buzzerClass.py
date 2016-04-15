import RPi.GPIO as gpio
import time
from lcd1602 import LCD1602
from board import Board

board = Board().board

class Buzz:
    def __init__(self, buzzSensor, board, lcd):
        self.lcd = lcd
        self.board = board
        self.buzzSensor = buzzSensor
        self.buzzMethod()

    def buzzMethod(self):
        self.lcd.lcd_string('Presence', self.lcd.LCD_LINE_1)
        self.lcd.lcd_string('Detected', self.lcd.LCD_LINE_2)
        self.board.output(buzzSensor, self.board.HIGH)  # Buzzer On
        time.sleep(2)
        self.board.output(buzzSensor, self.board.LOW)   # Buzzer Off
        self.lcd.lcd_clear()                     # Clear LCD

if __name__ == "__main__":
    gpio.setmode(gpio.BOARD)
    buzzSensor = 35
    gpio.setup(buzzSensor, gpio.OUT)
    b = Buzz(buzzSensor, board)
    #b.buzzMethod()