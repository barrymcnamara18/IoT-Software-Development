from ubidotsREST import *
from systemChecks import *

#Global settings

TOKEN = "A1E-sD6DHHw6MaKx5gED8bj1A9yVJkwPDi" # Assign your Ubidots Token
DEVICE = "IOT_project" # Assign the device label to obtain the variable
DELAY = 1  # Delay in seconds

#Set the system variables for Ubidots
VARIABLE_LABEL_1 = "noise-alert"  # Put your first variable label here
VARIABLE_LABEL_2 = "sensordata"  # Put your second variable label here
VARIABLE_LABEL_3 = "location"  # Put your second variable label here
VARIABLE_LABEL_4 = "rollingaverage"  # Put your second variable label here
VARIABLE_LABEL_5 = "capturingdata" #Check if the sensor is capturing data
VARIABLE_LABEL_6 = "vRollingAverage"
VARIABLE_LABEL_7 = "vUpper"
VARIABLE_LABEL_8 = "vLower"
VARIABLE_LABEL_9 = "capturingdata"

#Take pictures when alerted
pictureAlert = 0

#rolling average of sensor values every 60 sec
rolling_average_size = 10

#set the iniitial reading count to prevent division by 0
reading_count = 1

#Upper acceptable sensor value
upper_reasonable_bound = 800

#Lower acceptable sensor value
lower_reasonable_bound = 10

#Alerts per reading loop
alerts = 0

# Alert threshold per 60 readings
alert_threshold = 30

# The threshold to turn the Red (Alert) led on 300.00 * 5 / 1024 = 1.46v
alert_value = 230

# The threshold to take series of pictures is 400.00 * 5 / 1024 = 1.95v
camera_alert = 250

# Check the average sound to see for continous loud noise
continuous_loud = 250

# Create gps coordinates for location
lat = ("53.3488206")
lng = ("-6.245368")

#Set initial device values
value_1 = (0)
value_2 = (0)
value_3 = ("")
value_4 = (0)
value_5 = (0)






