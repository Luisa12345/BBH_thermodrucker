import RPi.GPIO as GPIO
import time
from escpos import *

GPIO.setmode(GPIO.BCM)

GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


Epson= printer.Usb(0x0416,0x5011)


# lsusb -vvv -dID 0416:5011 | grep iInterface

# lsusb -vvv -d 0416:5011 | grep bEndpointAddress | grep OUT

prev_input=0

while True:
 
	
    if (GPIO.input(18) == False):
                
        # Print text
        Epson.text(" \n")
		
		# Print Prolog
        #Epson.image("/home/pi/Desktop/BBH_thermodrucker/00_Prolog.gif")
        #Epson.text(" \n \n \n")
				
        # Print Klaus
        Epson.image("/home/pi/Desktop/BBH_thermodrucker/01_Klaus.gif")
        Epson.text(" \n \n \n")
		
        # Print Erika
        #Epson.image("/home/pi/Desktop/BBH_thermodrucker/02_Erika.gif")		
        #Epson.text(" \n \n \n")
		
		# Print Monika
        #Epson.image("/home/pi/Desktop/BBH_thermodrucker/03_Monika.gif")	
        #Epson.text(" \n \n \n")
		
		# Print Golo
        #Epson.image("/home/pi/Desktop/BBH_thermodrucker/04_Golo.gif")	
        #Epson.text(" \n \n \n")
		
		# Print Michael
        #Epson.image("/home/pi/Desktop/BBH_thermodrucker/05_Michael.gif")			
        #Epson.text(" \n \n \n")
		
		# Print Elisabeth
        #Epson.image("/home/pi/Desktop/BBH_thermodrucker/06_Elisabeth.gif")		
        #Epson.text(" \n \n \n")
		
		# Print Leonie
        #Epson.image("/home/pi/Desktop/BBH_thermodrucker/07_Leonie.gif")
        #Epson.text(" \n \n \n")
		

    elif (GPIO.input(15) == False):
                
        # Print text
        Epson.text(" \n")
		
		# Print Prolog
        #Epson.image("/home/pi/Desktop/BBH_thermodrucker/00_Prolog_ENG.gif")
        #Epson.text(" \n \n \n")
				
        # Print Klaus
        Epson.image("/home/pi/Desktop/BBH_thermodrucker/01_Klaus_ENG.gif")
        Epson.text(" \n \n \n")
		
        # Print Erika
        #Epson.image("/home/pi/Desktop/BBH_thermodrucker/02_Erika_ENG.gif")		
        #Epson.text(" \n \n \n")
		
		# Print Monika
        #Epson.image("/home/pi/Desktop/BBH_thermodrucker/03_Monika_ENG.gif")
        #Epson.text(" \n \n \n")
		
		# Print Golo
        #Epson.image("/home/pi/Desktop/BBH_thermodrucker/04_Golo_ENG.gif")	
        #Epson.text(" \n \n \n")
		
		# Print Michael
        #Epson.image("/home/pi/Desktop/BBH_thermodrucker/05_Michael_ENG.gif")			
        #Epson.text(" \n \n \n")
		
		# Print Elisabeth
        #Epson.image("/home/pi/Desktop/BBH_thermodrucker/06_Elisabeth_ENG.gif")		
        #Epson.text(" \n \n \n")
		
		# Print Leonie
        #Epson.image("/home/pi/Desktop/BBH_thermodrucker/07_Leonie_ENG.gif")		
        #Epson.text(" \n \n \n")
		
        # Print text
        #Epson.text(" \n \n \n")
        
        
        time.sleep(0.05)
        
        input_state= True
        

input_state = prev_input
