import RPi.GPIO as gpio
import time, os, sys

class Sides:
  def __init__(self, TRIG, ECHO):
    self.__TRIG = TRIG
    self.__ECHO = ECHO
    self.__distance = 0
    self.getSideDist()
    
  @property
  def Trig(self):
    return self.__TRIG
  
  @Trig.setter
  def Trig(self, value):
    self.__TRIG = value
  
  @property
  def Echo(self):
    return self.__ECHO
  
  @Echo.setter
  def Echo(self, value):
    self.__ECHO = value
  
  @property
  def Distance(self):
    return self.__distance
  
  @Distance.setter
  def Distance(self, value):
    self.__Distance = value
  
  def getSideDist(self):
    #This is a pre written method which checks an ultrasonic sensor that is connected to the pi
    #So the pins will be imported depending which sensor is running in the while loop further down
    gpio.setup(self.__TRIG,gpio.OUT)
    gpio.setup(self.__ECHO,gpio.IN)
    gpio.output(self.__TRIG, False)
    #print "Waiting For Sensor To Settle"
    time.sleep(0.2)
    gpio.output(self.__TRIG, True)
    time.sleep(0.00001)
    gpio.output(self.__TRIG, False)
    while gpio.input(self.__ECHO)==0:
      pulse_start = time.time()
    while gpio.input(self.__ECHO)==1:
      pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    #print ("Distance: " + str(distance) + "cm")
    self.__distance = distance
