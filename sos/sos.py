#SOS flaher by Owen Gilbert

import RPi.GPIO as GPIO,time

GPIO.setmode(GPIO.BOARD) #Set the pin numbering system

GPIO.setup(11,GPIO.OUT) #Set pin 11 as an output

GPIO.output(11,True) #Turns the LED on, Switches the current to that pin
time.sleep(0.5)
GPIO.output(11,False)
time.sleep(0.5)
GPIO.output(11,True)
time.sleep(0.5)
GPIO.output(11,False)
time.sleep(0.5)
GPIO.output(11,True)
time.sleep(0.5)
GPIO.output(11,False)
time.sleep(0.5)
GPIO.output(11,True)
time.sleep(2)
GPIO.output(11,False)
time.sleep(1)
GPIO.output(11,True)
time.sleep(2)
GPIO.output(11,False)
time.sleep(1)
GPIO.output(11,True)
time.sleep(2)
GPIO.output(11,False)
time.sleep(1)
GPIO.output(11,True)
time.sleep(0.5)
GPIO.output(11,False)
time.sleep(0.5)
GPIO.output(11,True)
time.sleep(0.5)
GPIO.output(11,False)
time.sleep(0.5)
GPIO.output(11,True)
time.sleep(0.5)
GPIO.output(11,False)
