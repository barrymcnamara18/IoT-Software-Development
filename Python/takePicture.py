from picamera import PiCamera
from time import sleep
from led import *

camera = PiCamera()
camera.resolution = (1280, 720)
camera.led = False
#camera.start_preview()
#camera.preview.alpha = 128
#camera.preview.fullscreen = False
#camera.preview.window = (0, 0, 640, 480)

def takePictures():
    
    variable_led(1)
    camera.start_preview()
    
    for i in range(1):
        camera.start_preview()
        #sleep(1)
        filedate = time.strftime("%Y%m%d-%H%M%S")
        camera.capture('/home/pi/Desktop/IoT Project/Pictures/image%s.jpg' % filedate)
        i+= 1
        variable_led(0)
        camera.stop_preview()
        
    

