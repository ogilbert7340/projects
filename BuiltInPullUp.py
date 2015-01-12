import RPi.GPIO as GPIO, time

pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

while True:
	pin_value = GPIO.input(pin)
	print ("HIGH" if pin_value else "LOW")
	time.sleep(0.5)
