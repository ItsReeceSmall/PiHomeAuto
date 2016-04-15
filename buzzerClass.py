import RPi.GPIO as gpio
import time
from lcd1602 import LCD1602 as lcd
from board import Board
board = Board().board

class Buzz:
    def __init__(self, buzzSensor, board, lcd):
        self.lcd = lcd
        self.board = board
        self.buzzSensor = buzzSensor
        self.buzzMethod()

    def buzzMethod(self):
        self.board.setup(self.buzzSensor, self.board.OUT)
        self.lcd.lcd_string('Presence', self.lcd.LCD_LINE_1)
        self.lcd.lcd_string('Detected', self.lcd.LCD_LINE_2)
        self.board.output(self.buzzSensor, self.board.HIGH)  # Buzzer On
        time.sleep(5)
        self.board.output(self.buzzSensor, self.board.LOW)   # Buzzer Off
        self.lcd.lcd_clear()                     # Clear LCD

if __name__ == "__main__":
    gpio.setmode(gpio.BOARD)
    buzzSensor = 35
    gpio.setup(buzzSensor, gpio.OUT)
    b = Buzz(buzzSensor, board, lcd)
    #b.buzzMethod()