/*
 * Classname e.g. greenLED.py
 *
 * Version information e.g. Rev 1
 *
 * Date e.g. 01/05/2018
 *
 * @reference: https://github.com/DexterInd/GrovePi/blob/master/Software/Python/grove_led_blink.py
 * @author Barry McNamara
 *
 */ 

from grovepi import *

def ledSwitch (enable):

    # Connect the green LED to digital port D3
    greenLED = 4
    pinMode(greenLED,"OUTPUT")
    digitalWrite(greenLED,enable)	#Send a value to switch on or off the LED
    
    if enable == 1:
        return ("Green LED Turned On")
    else:
        return ("Green LED Turned Off")

