import RPi.GPIO as gpio
import time, sys, os

class irSensor:
    def __init__(self, irFL, irFR, irMID):
        self.__irFL = irFL
        self.__irFR = irFR
        self.__irMID = irMID
        self.__detection = 0
        self.irDetection()
    
    @property
    def detection(self):
        return self.__detection
    @detection.setter
    def detection(self, value):
        self.__detection = value
    
    @property
    def irFL(self):
        return self.__irFL
    @irFL.setter
    def irFL(self, value):
        self.__irFL = value
    
    @property
    def irFR(self):
        return self.__irFR
    @irFR.setter
    def irFR(self, value):
        self.__irFR = value
    
    @property
    def irMID(self):
        return self.__irMID
    @irMID.setter
    def irMID(self, value):
        self.__irMID = value
    
    def irDetection(self):
        #print (gpio.input(self.__irFL))
        #print (gpio.input(self.__irFR))
        #print (gpio.input(self.__irMID))
        if gpio.input(self.__irFL)==0:
            self.__detection = 1
        elif gpio.input(self.__irFR)==0:
            self.__detection = 1
        elif gpio.input(self.__irMID)==0:
            self.__detection = 1
        else:
            self.__detection = 0
