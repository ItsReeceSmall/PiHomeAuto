import time, sys, os
from board import Board

board = Board().board

class Light:
    def __init__(self, lightSensor, board, LSV):
        self.board = board
        self.lightSensor = lightSensor
        self.LSV = 0
        self.lightMethod()

    def lightMethod(self):
        self.board.setup(self.lightSensor, self.board.OUT)
        self.board.output(self.lightSensor, self.board.LOW)
        self.LSV = 0
        time.sleep(0.05)
        self.board.setup(self.lightSensor,self.board.IN)
        for i in range(1,11):
            if (self.board.input(self.lightSensor) == self.board.LOW):
                self.LSV += 1
        return self.LSV

if __name__ == "__main__":
    lightSensor = 18
    LSV = 0
    value = Light(lightSensor, board, LSV)
    print (value)
