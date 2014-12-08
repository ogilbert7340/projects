import time, picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    camera.capture(filename + ".jpg")
    time.sleep(1)
    camera.stop_preview
