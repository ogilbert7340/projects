import time, picamera

with picamera.PiCamera() as camera:
    camera.start_preview() #starts camera preview
    time.sleep(2)
    camera.capture(filename + ".jpg") #takes photo
    time.sleep(1)
    camera.stop_preview #stops camera preview
