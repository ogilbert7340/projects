import RPi.GPIO as GPIO, time

pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)

while True:
	pin_value = GPIO.input(pin)
	print ("Connected" if pin_value else "Disconnected")
	time.sleep(0.5)
