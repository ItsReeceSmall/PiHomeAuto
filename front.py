import RPi.GPIO as gpio
import time, os, sys

class Front:
  def __init__(self, sonar):
    self.__sonar = sonar
    self.__distance = 0
    self.getDistance()
    
  @property
  def Sonar(self):
    return self.__sonar
  
  @Sonar.setter
  def Sonar(self, value):
    self.__sonar = value
  
  @property
  def Distance(self):
    return self.__distance
  
  @Distance.setter
  def Distance(self, value):
    self.__Distance = value
    
  def getDistance(self):
    # The Pi2go pre written method changed to work with python3 which checks the ultrasonic sensor on the board
    gpio.setup(self.__sonar, gpio.OUT)
    # Send 10us pulse to trigger
    gpio.output(self.__sonar, True)
    time.sleep(0.00001)
    gpio.output(self.__sonar, False)
    start = time.time()
    count=time.time()
    gpio.setup(self.__sonar, gpio.IN)
    while gpio.input(self.__sonar)==0 and time.time()-count<0.1:
        start = time.time()
    count=time.time()
    stop=count
    while gpio.input(self.__sonar)==1 and time.time()-count<0.1:
        stop = time.time()
    # Calculate pulse length
    elapsed = stop-start
    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound 34000(cm/s) divided by 2
    distance = elapsed * 17000
    self.__distance = distance
