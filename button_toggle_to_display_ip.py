import RPi.GPIO as GPIO
import time,os  
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(20,GPIO.IN,GPIO.PUD_UP)
while 1:
	if  (GPIO.input(21)) and (not GPIO.input(20)):
		os.system("cat /home/pi/IP-Displayer/ip.txt | xargs sudo python /home/pi/IP-Displayer/ip-displayer.py")
	elif (GPIO.input(20)):
		GPIO.cleanup()
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(21,GPIO.IN,GPIO.PUD_UP)
		GPIO.setup(20,GPIO.IN,GPIO.PUD_UP)
	time.sleep(1)
