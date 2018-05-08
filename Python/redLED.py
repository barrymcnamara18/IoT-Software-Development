
 * Classname e.g. redLED.py
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

    # Connect the red LED to digital port D3
    redLED = 7
    pinMode(redLED,"OUTPUT")
    digitalWrite(redLED,enable)	#Send a value to switch on or off the LED
    
    if enable == 1:
        return ("red LED Turned On")
    else:
        return ("red LED Turned Off")




