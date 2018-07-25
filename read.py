import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)
GPIO.setup(24,GPIO.OUT)
try:
	while True:
		i=GPIO.input(21)
		if i==0:
			print "not detected"
			GPIO.output(24,True)
			time.sleep(.5)

		elif i==1:
			print "Detected"
			GPIO.output(24,False)
			time.sleep(.5)
except:
	KeyboardInterrupt()
	GPIO.cleanup()