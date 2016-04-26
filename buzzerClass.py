import RPi.GPIO as gpio
import time
from board import Board
board = Board().board

class Buzz:
    def __init__(self, buzzSensor, board, frame):
        self.frame = frame
        self.board = board
        self.buzzSensor = 35
        self.outpin()

    def outpin(self):
        self.board.setup(self.buzzSensor, self.board.OUT)

    def buzzOn(self):
        self.board.output(self.buzzSensor, self.board.HIGH)
        #print ('buzzer on')# Buzzer On

    def buzzOff(self):
        self.board.output(self.buzzSensor, self.board.LOW)
        #print('buzzer off')  # Buzzer Off

    def buzzTest(self):
        BuzzValue = Label(self.frame, text=('ON'), borderwidth=1).grid(row=7, column=2, padx=5, pady=5)
        self.board.output(self.buzzSensor, self.board.HIGH)
        time.sleep(0.5)
        BuzzValue = Label(self.frame, text=('OFF'), borderwidth=1).grid(row=7, column=2, padx=5, pady=5)
        self.board.output(self.buzzSensor, self.board.LOW)

if __name__ == "__main__":
    gpio.setmode(gpio.BOARD)
    buzzSensor = 35
    gpio.setup(buzzSensor, gpio.OUT)
    b = Buzz(buzzSensor, board, 1)
    #b.buzzMethod()