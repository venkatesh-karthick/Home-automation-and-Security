import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
try:
	while True:
		GPIO.output(24,True)
		time.sleep(5)
		GPIO.output(24,False)
		time.sleep(2)

except:
	KeyboardInterrupt()
	GPIO.cleanup()
