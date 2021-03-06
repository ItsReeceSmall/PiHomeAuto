from board import Board
import time, os, sys
import RPi.GPIO as gpio
from board import Board

board = Board().board

class Dist:
  def __init__(self, dtSensor, deSensor, board):
      self.board = board
      self.dtSensor = dtSensor
      self.deSensor = deSensor
      self.distValue = 0
      self.distCheck()
  
  def distCheck(self):
      pulse_end, pulse_start = 0, 0
      self.dtSensor = 29
      self.deSensor = 31
      self.board.setup(self.dtSensor,self.board.OUT)
      self.board.setup(self.deSensor,self.board.IN)
      self.board.output(self.dtSensor, False)
      time.sleep(0.2)
      self.board.output(self.dtSensor, True)
      time.sleep(0.00001)
      self.board.output(self.dtSensor, False)
      #print ('DEBUG: while gpio.input(self.deSensor)==0:')
      while self.board.input(self.deSensor)==0:
          pulse_start = time.time()
          #print(str(pulse_start) + ' is start')
      #print ('DEBUG: while gpio.input(self.deSensor)==1:')
      while self.board.input(self.deSensor)==1:
          pulse_end = time.time()
          #print (str(pulse_end) + ' is end')
      pulse_duration = pulse_end - pulse_start
      #print (str(pulse_duration) + ' is pulse duration')
      #print ('DEBUG: pulse_duration = pulse_end - pulse_start')
      distance = pulse_duration * 17150
      distance = round(distance, 1)
      #print (str(distance) + ' is the distance.')
      self.distValue = distance
      return self.distValue

if __name__ == "__main__":
    gpio.setmode(gpio.BOARD)
    dtSensor = 29
    deSensor = 31
    d = Dist(dtSensor, deSensor, board)
    print (d.distValue)
