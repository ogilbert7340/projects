import RPi.GPIO as GPIO, time, math #TIS A PULLUP

pin = 17
count = 0

def spin(channel1):
	global count
	count += 1
	print (count)

def calcspeed():
	speedCMps = ((9 * math.pi) * count / 5)
	global speedKMph
	speedKMph = ((speedCMps * 100000) *3600)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.FALLING, callback=spin, bouncetime=300)

while True:
	count = 0
	time.sleep(5)
	calcspeed()

input("Press enter to exit")
