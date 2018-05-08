from led import *
from takePicture import *


def noiseAlert(sensor_value,alert_value):

    #Check if the sensor has detected a loud noise and light the red LED if true
    if sensor_value > alert_value:
        red(1)
        takePictures()
        return (1)
    else:
        red(0)
        return (0)
    
def systemlive(sensor_value,lower_reasonable_bound):
    
   #Check if the system is live and capturing data
    if int(sensor_value) > (lower_reasonable_bound):
        green(1)
        return True
    else:
        green(0)
        return False

