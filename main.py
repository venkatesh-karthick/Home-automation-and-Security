
import RPi.GPIO as GPIO
import Tkinter
import tkMessageBox
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)
GPIO.setup(24,GPIO.OUT)
top = Tkinter.Tk()


def on():

	GPIO.output(24,True)
	

def off():
	GPIO.output(24,False)

def start():
	t=True
	c=1
	while t:
		i=GPIO.input(21)
		if i==0:
			print "not detected"
			GPIO.output(24,True)
			time.sleep(.5)
			c+=1
			if c>20:
				off
				t=False

		elif i==1:
			print "Detected"
			GPIO.output(24,False)
			time.sleep(.5)
			c=1
	
	
top.geometry('240x240')
B = Tkinter.Button(top, text ="LED ON", command = off)

B.pack()

B1 = Tkinter.Button(top, text ="LED OFF", command = on)

B1.pack()

B2 = Tkinter.Button(top, text ="AUTOMATION", command = start)

B2.pack()

top.mainloop()


