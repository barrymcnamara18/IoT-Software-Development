import grovepi
from grove_rgb_lcd import *

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
ultrasonic_ranger = 8

lcdText = (grovepi.ultrasonicRead(ultrasonic_ranger))

setText(str(lcdText))
setRGB(0,128,64)


# Print distance value in the console
print(str(lcdText)grovepi.ultrasonicRead(ultrasonic_ranger))