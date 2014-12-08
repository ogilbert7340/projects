import picamera, time

with picamera.PiCamera() as camera:
    camera.start_preview()
    print("120")
    time.sleep(2)
    print("test")
    for filename in camera.capture_continuous('img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        time.sleep(10) # wait every 10 seconds
