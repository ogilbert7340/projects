import RPi.GPIO as GPIO, time, math

rainPin = 27
windPin = 17

rainCount = 0
windCount = 0

def bucketTippedSeconds(channel):
	global rainCount
	rainCount += 1

def bucket_tipped(channel):
	global rainCount
	rainCount += 1
	print (rainCount * 0.2794)

def spin(channel):
	global windCount
	windCount += 1
	print (windCount)

def calcspeed():
	speedCMps = ((9 * math.pi) * windCount / 5)
	global speedKMph
	speedKMph = ((speedCMps * 100000) *3600)

GPIO.setmode(GPIO.BCM)
GPIO.setup(rainPin, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(windPin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(windPin, GPIO.FALLING, callback=spin, bouncetime=300)
GPIO.add_event_detect(rainPin, GPIO.FALLING, callback=bucket_tipped, bouncetime=300)

while True:
	rainCount = 0
	windCount = 0
	time.sleep(5)
	print("Rain Fall: ", rainCount * 0.2794)
	speedKMph = calcspeed()
	print("Wind Speed: ", speedKMph)

input("Print enter to exit...")
	
