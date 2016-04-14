import RPi.GPIO as gpio
import time, os, sys, glob
from distClass import Dist as D
from buzzerClass import Buzz as B
from board import Board

board = Board().board

class carReverse:
    def __init__(self, deSensor, dtSensor, board):
        self.board = board
        self.deSensor = deSensor
        self.dtSensor = dtSensor
        self.carReverseMethod()

    def carReverseMethod(self):
