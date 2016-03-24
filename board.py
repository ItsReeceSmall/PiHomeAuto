import sys, os, time
import RPi.GPIO as gpio

class Board:
    def __init__(self):
        self.board = gpio
    
    def setup(self):
        self.board.setwarnings(False)
        self.board.setmode(self.board.BOARD)
