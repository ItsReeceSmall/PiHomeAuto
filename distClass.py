import RPi.GPIO as gpio
import time, os, sys

class Dist:
  def __init__(self, dtSensor, deSensor):
      self.dtSensor = dtSensor
      self.deSensor = deSensor
      self.distCheck()
  
  def distCheck(self):
      gpio.setup(self.dtSensor,gpio.OUT)
      gpio.setup(self.deSensor,gpio.IN)
      gpio.output(self.dtSensor, False)
      time.sleep(1)
      gpio.output(self.dtSensor, True)
      time.sleep(0.00001)
      gpio.output(self.dtSensor, False)
      while gpio.input(self.deSensor)==0:
          pulse_start = time.time()
      while gpio.input(self.deSensor)==1:
          pulse_end = time.time()
      pulse_duration = pulse_end - pulse_start
      distance = pulse_duration * 17150
      distance = round(distance, 2)
      dist = str(distance)
      return dist

if __name__ == "__main__":
    gpio.setmode(gpio.BOARD)
    dtSensor = 36
    deSensor = 38
    Dist(dtSensor, deSensor)
