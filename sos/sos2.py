#SOS flaher by Owen Gilbert

import RPi.GPIO as GPIO,time

GPIO.setmode(GPIO.BOARD) #Set the pin numbering system

GPIO.setup(11,GPIO.OUT) #Set pin 11 as an output

#Function definition
def dot():
	GPIO.output(11,True) #Turns the LED on
	time.sleep(0.5) #Waiting
	GPIO.output(11,False) #Turns LED off
	time.sleep(0.5)
#calling the dot() function
dot()

#Funstion Definition 2
def dash():
	GPIO.output(11,True) #Turns the LED on
	time.sleep(2) #Waiting
	GPIO.output(11,False) #Turns LED off
	time.sleep(0.5)
#calling the dash() function
dash()



def a():
	dot()
	dash()
a()

def b()
	dash()
	dot()
	dot()
	dot()
b()

def c()
	dash()
	dot()
	dash()
	dot()
c()

def d()
	dash()
	dot()
	dot()
d()

def e()
	dot()
e()

def f()
	dot()
	dot()
	dash()
	dot()
f()

def g()
	dash()
	dash()
	dot()
g()

def h()
	dot()
	dot()
	dot()
	dot()
h()

def i()
	dot()
	dot()
i()

def j()
	dot()
	dash()
	dash()
	dash()
j()

def k()
	dash()
	dot()
	dash()
k()

def l()
	dot()
	dash()
	dot()
	dot()
l()

#Starting the Program
a()
