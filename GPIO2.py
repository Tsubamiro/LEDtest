import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(15,GPIO.OUT)

for x in range(7):
	GPIO.output(15,True)
	sleep(0.5)
	GPIO.output(15,False)
	sleep(0.5)


GPIO.cleanup()
