import requests
import time
import math
import systemChecks, fn_rolling_average
from config import *
from soundSensor import *
from led import *

TOKEN = "A1E-sD6DHHw6MaKx5gED8bj1A9yVJkwPDi"  # Put your TOKEN here
DEVICE_LABEL = "IOT_project"  # Put your device label here
VARIABLE = "alert_value" # Assign the variable label to obtain the variable value
DELAY = 1  # Delay in seconds

def build_payload(variable_1, variable_2, variable_3, variable_4, variable_5):

    #base sensor values 
    i=reading_count
    sensor_value = (0)
 
    #Check the sensor reading
    value_2 = soundreading()
    sensor_value = value_2
    
    #Check for noise alerts
    value_1 = systemChecks.noiseAlert(sensor_value,alert_value)
    
    #calculate the rolling average
    value_3 = fn_rolling_average.rolling_average(sensor_value,sensor_measurements)
    
    #Check if the system is collecting data
    value_5 = systemChecks.systemlive(sensor_value,lower_reasonable_bound)
                
    payload = {variable_1: int(value_1),
                variable_2: value_2,
                variable_3: {"value": 1, "context": {"lat": lat, "lng": lng}},
                variable_4: value_3,
                variable_5: value_5}

    return payload

def get_var(device, variable):
    try:
        url = "http://things.ubidots.com/"
        url = url + \
            "api/v1.6/devices/{0}/{1}/".format(device, variable)
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        req = requests.get(url=url, headers=headers)
        return req.json()['last_value']['value']
    except:
        pass

    
def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://things.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(0.1)

    # Processes results
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True


def mainPost():

    payload = build_payload(
        VARIABLE_LABEL_1, VARIABLE_LABEL_2, VARIABLE_LABEL_3, VARIABLE_LABEL_4, VARIABLE_LABEL_5)

    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")
    


if __name__ == '__main__':
    while (True):
        #try:
            mainPost()
            #time.sleep(0.1)
        
        #except KeyboardInterrupt:
        #        #Check if the system is collecting data
        #        value_5 = (0)
        #        grovepi.digitalWrite(led1,0)
        #pass

