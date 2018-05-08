from grovepi import *
from config import *
from fn_rolling_average import *

# Connect the Grove Sound Sensor to analog port A0
# SIG,NC,VCC,GND
sound_sensor = 0

pinMode(sound_sensor,"INPUT")

# Create an array to store the sound sensor measurements
sensor_measurements = []

#Set the base sensor reading to 0
sensorReading = 0

# Read the sound data from the sensor
def soundreading():
    
    sensorCount = 0
    sensor_measurements = []
    
    while sensorCount <= rolling_average_size:
            sensor_value = float(analogRead(sound_sensor))
            sensor_measurements.append(sensor_value)
            sensorReading = rolling_average(sensor_value, sensor_measurements)
            sensorCount += 1
    return (sensorReading)

