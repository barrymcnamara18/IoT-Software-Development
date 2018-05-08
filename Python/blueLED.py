
 * Classname e.g. blueLED.py
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

    # Connect the blue LED to digital port D3
    blueLED = 3
    pinMode(blueLED,"OUTPUT")
    digitalWrite(blueLED,enable)	#Send a value to switch on or off the LED
    
    if enable == 1:
        return ("blue LED Turned On")
    else:
        return ("blue LED Turned Off")



