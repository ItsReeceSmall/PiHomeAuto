import RPi.GPIO as gpio
import time, sys, os

class Wheels:
  def __init__(self, rmf, rmb, lmf, lmb, f, l, r, i, lmfPWM, lmbPWM, rmfPWM, rmbPWM):
    self.__rmf = rmf
    self.__rmb = rmb
    self.__lmf = lmf
    self.__lmb = lmb
    self.__f = f
    self.__l = l
    self.__r = r
    self.__i = i
    self.__rmfPWM = rmfPWM
    self.__rmbPWM = rmbPWM
    self.__lmfPWM = lmfPWM
    self.__lmbPWM = lmbPWM
    self.wheelsGo()
    
  @property
  def rmfPWM(self):
    return self.__rmfPWM
  @rmfPWM.setter
  def rmfPWM(self, value):
    self.__rmfPWM = value
    
  @property
  def rmbPWM(self):
    return self.__rmbPWM
  @rmbPWM.setter
  def rmbPWM(self, value):
    self.__rmbPWM = value

  @property
  def lmfPWM(self):
    return self.__lmfPWM
  @lmfPWM.setter
  def lmfPWM(self, value):
    self.__lmfPWM = value
  
  @property
  def lmbPWM(self):
    return self.__lmbPWM
  @lmbPWM.setter
  def lmbPWM(self, value):
    self.__lmbPWM = value
    
  @property
  def rmf(self):
    return self.__rmf
  @rmf.setter
  def rmf(self, value):
    self.__rmf = value
  
  @property
  def rmb(self):
    return self.__rmb
  @rmb.setter
  def rmb(self, value):
    self.__rmb = value

  @property
  def lmf(self):
    return self.__lmf
  @lmf.setter
  def lmf(self, value):
    self.__lmf = value

  @property
  def lmb(self):
    return self.__lmb
  @lmb.setter
  def lmb(self, value):
    self.__lmb = value

  @property
  def f(self):
    return self.__f
  @f.setter
  def f(self, value):
    self.__f = value

  @property
  def l(self):
    return self.__l
  @l.setter
  def l(self, value):
    self.__l = value

  @property
  def r(self):
    return self.__r
  @r.setter
  def r(self, value):
    self.__r = value
    
  @property
  def i(self):
    return self.__r
  @i.setter
  def i(self, value):
    self.__i = value
    
  def wheelsGo(self):
    print ('#######################')
    print ('Left: ' + str(self.__l))        # Prints the distance on screen to show what the pi is detecting
    if self.__l < 25:
        self.__lmfPWM.ChangeDutyCycle(65)
        print('')
        print ('lmf speed = 65')
        self.__lmbPWM.ChangeDutyCycle(0)
        self.__rmfPWM.ChangeDutyCycle(100)
        print ('rmf speed = 100')
        print(' ')
        self.__rmbPWM.ChangeDutyCycle(0)
        time.sleep(1)
        print ('reset to 100 and 96')
        print (' ')
        self.__lmfPWM.ChangeDutyCycle(100)
        self.__rmfPWM.ChangeDutyCycle(96)                    # If the distance is lower than 25cm then the code below is ran.
    print ('Right: ' + str(self.__r))      # Prints the distance on screen to show what the pi is detecting
    if self.__r < 25:
        self.__lmfPWM.ChangeDutyCycle(100)
        print('')
        print ('lmf speed = 100')
        self.__lmbPWM.ChangeDutyCycle(0)
        self.__rmfPWM.ChangeDutyCycle(65)
        print ('rmf speed = 65')
        print('')
        self.__rmbPWM.ChangeDutyCycle(0)
        time.sleep(1)
        print ('reset to 96')
        print (' ')
        self.__rmfPWM.ChangeDutyCycle(96)                   # If the distance is lower than 25cm then the code below is ran.
    print ('Front: ' + str(self.__f))      # Prints the distance on screen to show what the pi is detecting
    if self.__f < 50 or self.__i == 1:    # If the front sensor is less than 40cm away from a block, it will run the code below
        self.__i = 0
        self.__lmfPWM.ChangeDutyCycle(0)
        self.__lmbPWM.ChangeDutyCycle(0)       # All the motors are stopped, set to 0
        self.__rmfPWM.ChangeDutyCycle(0)
        self.__rmbPWM.ChangeDutyCycle(0)
        if self.__l < self.__r or self.__i == 1:                # Checks if the left distance is less than the right, if True, code below is ran
            self.__i = 0
            print('Going Back')
            self.__lmbPWM.ChangeDutyCycle(55)  # The wheels go backwards
            self.__rmbPWM.ChangeDutyCycle(55) 
            time.sleep(2)               # For 2 seconds
            print('Rotating Right')
            self.__lmbPWM.ChangeDutyCycle(53)
            self.__rmfPWM.ChangeDutyCycle(53)  # The Wheels rotate opposite ways to turn away from the block
            time.sleep(1.3)             # For 1.7 seconds
            self.__lmbPWM.ChangeDutyCycle(0)   # Both wheels stop and are set to 0
            self.__rmfPWM.ChangeDutyCycle(0)
        if self.__r < self.__l or self.__i == 1:                # Checks if the right distance is less than the left, if True, code below is ran
            self.__i = 0
            print('Going Back')
            self.__lmbPWM.ChangeDutyCycle(55)  # The wheels go backwards
            self.__rmbPWM.ChangeDutyCycle(55)
            time.sleep(2)               # For 2 seconds
            print('Rotating Left')
            self.__lmfPWM.ChangeDutyCycle(53)
            self.__rmbPWM.ChangeDutyCycle(53)  # The wheels rotate opposite ways to turn away from the block
            time.sleep(1.3)             # For 1.7 seconds
            self.__lmfPWM.ChangeDutyCycle(0)   # Both wheels stop and are set to 0
            self.__rmbPWM.ChangeDutyCycle(0)
        print('Normal Speed')
        self.__lmfPWM.ChangeDutyCycle(100)
        self.__rmfPWM.ChangeDutyCycle(96)     # Wheels return to normal speed before restarting the loop and checking for blockages again.
        self.__lmbPWM.ChangeDutyCycle(0)
        self.__rmbPWM.ChangeDutyCycle(0)
