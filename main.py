import RPi.GPIO as gpio
import time, os, sys
import pins
import front
import sides
import wheels
import ir

def setup():
    #set GPIO up
    gpio.setmode(gpio.BOARD)
    #Set up pins from a class
    lmf = 19
    lmb = 21
    rmf = 26
    rmb = 24
    sonar = 8
    trigL = 38
    echoL = 36
    trigR = 37
    echoR = 35
    irFL = 11
    irFR = 7
    irMID = 13
    # Set there categories
    inputs = [trigL,trigR,irFL,irFR,irMID]
    outputs = [sonar,lmf,lmb,rmf,rmb,echoL,echoR]
    print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
    thepins = pins.Pins(inputs, outputs)
    print('### ALL PINS IMPORTED AND SETUP SUCCESSFULLY ###')
# Right Wheel Forward
    rmfPWM = gpio.PWM(rmf,100)  # Right Motor Forward, sets power output to 100
    rmbPWM = gpio.PWM(rmb,100)  # Right Motor Back, sets power output to 100
    rmfPWM.start(0) # starts on 0
    rmbPWM.start(0) # starts on 0
    rmfPWM.ChangeDutyCycle(96)  # Right Motor Forward changes its power its recieving to 96
    rmbPWM.ChangeDutyCycle(0)   # Right Motor Back has 0 recieving power as we dont want it to go back
# Left Wheel Forward
    lmfPWM = gpio.PWM(lmf,100)  # Left Motor Forward, sets power output to 100
    lmbPWM = gpio.PWM(lmb,100)  # Left Motor Back, sets power output to 100
    lmfPWM.start(0) # starts on 0
    lmbPWM.start(0) # starts on 0
    lmfPWM.ChangeDutyCycle(100) # Left Motor Forward changes its power its recieving to 96
    lmbPWM.ChangeDutyCycle(0)   # Left Motor Back has 0 recieving power as we dont want it to go back
    while True:
        thefront = front.Front(sonar)
        thesidesLeft = sides.Sides(trigL, echoL)
        thesidesRight = sides.Sides(trigR, echoR)
        f = (thefront.Distance)
        l = (thesidesLeft.Distance)
        r = (thesidesRight.Distance)
        irResponse = ir.irSensor(irFL, irFR, irMID)
        i = (irResponse.detection)
        #print (i)
        thewheels = wheels.Wheels(rmf,rmb,lmf,lmb,f,l,r,i,lmfPWM,lmbPWM,rmfPWM,rmbPWM)
    #print(thefront.Distance)
    #print('left ' + thesidesLeft.Distance)
    #print('right ' + thesidesRight.Distance)
    
setup()
gpio.cleanup()
