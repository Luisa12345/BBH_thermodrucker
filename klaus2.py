import RPi.GPIO as GPIO
import time
from escpos import *

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

Epson= printer.Usb(0x0416,0x5011)


# lsusb -vvv -dID 0416:5011 | grep iInterface

# lsusb -vvv -d 0416:5011 | grep bEndpointAddress | grep OUT

prev_input=0

while True:
    input_state = GPIO.input(18)
    if input_state == False:
                
        # Print text
        Epson.text(" \n")
        # Print image
        Epson.image("/home/pi/Desktop/klaus/01_Klaus.gif")
        # Print image
        Epson.image("/home/pi/Desktop/klaus/02_Erika.gif")		
        # Print text
        Epson.text(" \n \n \n")
        
        
        time.sleep(0.05)
        
        input_state= True
        
        

input_state = prev_input
