import RPi.GPIO as gpio     # All parts that say 'gpio' are like that because it's set here in the import
import time                 # Time is required to pause the program at required times
import sys                  # Used to access sys functions, like sys.exit()

def getSideDist(TRIG, ECHO):
    #This is a pre written method which checks an ultrasonic sensor that is connected to the pi
    #So the pins will be imported depending which sensor is running in the while loop further down
    gpio.setup(TRIG,gpio.OUT)
    gpio.setup(ECHO,gpio.IN)
    gpio.output(TRIG, False)
    #print "Waiting For Sensor To Settle"
    time.sleep(0.2)
    gpio.output(TRIG, True)
    time.sleep(0.00001)
    gpio.output(TRIG, False)
    while gpio.input(ECHO)==0:
      pulse_start = time.time()
    while gpio.input(ECHO)==1:
      pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    #print ("Distance: " + str(distance) + "cm")
    return distance

def getDistance(sonar):
    # The Pi2go pre written method changed to work with python3 which checks the ultrasonic sensor on the board
    gpio.setup(sonar, gpio.OUT)
    # Send 10us pulse to trigger
    gpio.output(sonar, True)
    time.sleep(0.00001)
    gpio.output(sonar, False)
    start = time.time()
    count=time.time()
    gpio.setup(sonar, gpio.IN)
    while gpio.input(sonar)==0 and time.time()-count<0.1:
        start = time.time()
    count=time.time()
    stop=count
    while gpio.input(sonar)==1 and time.time()-count<0.1:
        stop = time.time()
    # Calculate pulse length
    elapsed = stop-start
    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound 34000(cm/s) divided by 2
    distance = elapsed * 17000
    return distance

def startMotor(lmf, lmb, rmf, rmb): # sets up all the motor pins
    gpio.setup(lmf, gpio.OUT)
    gpio.setup(lmb, gpio.OUT)   # sets all the pins to output
    gpio.setup(rmf, gpio.OUT)
    gpio.setup(rmb, gpio.OUT)

gpio.setmode(gpio.BOARD)    # sets what board type we will use

# all the pins we will use
lmf = 19
lmb = 21
rmf = 26
rmb = 24
sonar = 8
trigL = 38
echoL = 36
trigR = 37
echoR = 35

startMotor(lmf, lmb, rmf, rmb)  # runs setup for all the motor pins
#Wheels
    # Right wheel Forward
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
    print ('#######################')
    left = getSideDist(trigL, echoL)    # Imports the two pins from higher up in the code in that order in to the method
    print ('Left: ' + str(left))        # Prints the distance on screen to show what the pi is detecting
    if left < 25:
        lmfPWM.ChangeDutyCycle(65)
        print('')
        print ('lmf speed = 65')
        lmbPWM.ChangeDutyCycle(0)
        rmfPWM.ChangeDutyCycle(100)
        print ('rmf speed = 100')
        print(' ')
        rmbPWM.ChangeDutyCycle(0)
        time.sleep(1)
        print ('reset to 100 and 96')
        print (' ')
        lmfPWM.ChangeDutyCycle(100)
        rmfPWM.ChangeDutyCycle(96)                    # If the distance is lower than 25cm then the code below is ran.
    right = getSideDist(trigR, echoR)   # Imports the two pins from higher up in the code in that order in to the method
    print ('Right: ' + str(right))      # Prints the distance on screen to show what the pi is detecting
    if right < 25:
        lmfPWM.ChangeDutyCycle(100)
        print('')
        print ('lmf speed = 100')
        lmbPWM.ChangeDutyCycle(0)
        rmfPWM.ChangeDutyCycle(65)
        print ('rmf speed = 65')
        print('')
        rmbPWM.ChangeDutyCycle(0)
        time.sleep(1)
        print ('reset to 96')
        print (' ')
        rmfPWM.ChangeDutyCycle(96)                   # If the distance is lower than 25cm then the code below is ran.
    front = getDistance(sonar)          # The front ultrasonic is ran by the pi2go board and only has one pin, but also it's own method, so the value of the front sensor is stored in the variable 'front'
    print ('Front: ' + str(front))      # Prints the distance on screen to show what the pi is detecting
    if front < 40:                      # If the front sensor is less than 40cm away from a block, it will run the code below
        lmfPWM.ChangeDutyCycle(0)
        lmbPWM.ChangeDutyCycle(0)       # All the motors are stopped, set to 0
        rmfPWM.ChangeDutyCycle(0)
        rmbPWM.ChangeDutyCycle(0)
        if left < right:                # Checks if the left distance is less than the right, if True, code below is ran
            print('Going Back')
            lmbPWM.ChangeDutyCycle(50)  # The wheels go backwards
            rmbPWM.ChangeDutyCycle(50) 
            time.sleep(2)               # For 2 seconds
            print('Rotating Right')
            lmbPWM.ChangeDutyCycle(52)
            rmfPWM.ChangeDutyCycle(52)  # The Wheels rotate opposite ways to turn away from the block
            time.sleep(1.7)             # For 1.7 seconds
            lmbPWM.ChangeDutyCycle(0)   # Both wheels stop and are set to 0
            rmfPWM.ChangeDutyCycle(0)
        if right < left:                # Checks if the right distance is less than the left, if True, code below is ran
            print('Going Back')
            lmbPWM.ChangeDutyCycle(50)  # The wheels go backwards
            rmbPWM.ChangeDutyCycle(50)
            time.sleep(2)               # For 2 seconds
            print('Rotating Left')
            lmfPWM.ChangeDutyCycle(52)
            rmbPWM.ChangeDutyCycle(52)  # The wheels rotate opposite ways to turn away from the block
            time.sleep(1.7)             # For 1.7 seconds
            lmfPWM.ChangeDutyCycle(0)   # Both wheels stop and are set to 0
            rmbPWM.ChangeDutyCycle(0)
        print('Normal Speed')
        lmfPWM.ChangeDutyCycle(96)
        rmfPWM.ChangeDutyCycle(100)     # Wheels return to normal speed before restarting the loop and checking for blockages again.
        lmbPWM.ChangeDutyCycle(0)
        rmbPWM.ChangeDutyCycle(0)
gpio.cleanup()  # If the while loop is broken then all the gpio pins are cleared
sys.exit()      # This exits the program safely
