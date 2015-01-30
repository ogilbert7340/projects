#PiBOOM - Pi Bangs Or Other Mishaps

import picamera, RPi.GPIO as GPIO, time
button = 14
balloon = 2
GPIO.output(balloon, False)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(balloon, GPIO.OUT)
GPIO.wait_for_edge(button, GPIO.FALLING)
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = (90)
    camera.start_preview()
    camera.start_recording("PiBOOM.h264")
    time.sleep(5)
    GPIO.output(balloon, True)
    time.sleep(1)
    camera.annotate_text = "5"
    time.sleep(1)
    camera.annotate_text = "4"
    time.sleep(1)
    camera.annotate_text = "3"
    time.sleep(1)
    camera.annotate_text = "2"
    time.sleep(1)
    camera.annotate_text = "1"
    time.sleep(10)
    GPIO.output(balloon, False)
    camera.annotate_text = "Ignition."
    time.sleep(60)
    camera.stop_recording()
    GPIO.output(balloon, False)
