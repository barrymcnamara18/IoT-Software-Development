from config import *

#Upper acceptable sensor value
upper_reasonable_bound = int(900)

#Lower acceptable sensor value
lower_reasonable_bound = int(10)

#rolling average of sensor values every 60 sec
rolling_average_size = 10


def average(measurements):
    
  # Handle division by zero error
  if len(measurements) != 0:
    return sum(measurements)/len(measurements)
  else:
    # When you use the average later, make sure to include something like
    # sensor_average = rolling_average(sensor_measurements)
    # if (conditions) and sensor_average > -1:
    # This way, -1 can be used as an "invalid" value
    return -1

def rolling_average(measurement, measurements):
    
  # Update rolling average if measurement is ok, otherwise return the average from previous values
  if lower_reasonable_bound < measurement < upper_reasonable_bound:
      
    # Remove first item from list if it's full according to our chosen size
    if len(measurements) >= rolling_average_size:
      measurements.pop(0)
    measurements.append(measurement)
  return average(measurements)