import RPi.GPIO as GPIO
import Tkinter
import tkMessageBox
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
top = Tkinter.Tk()

def on():
	GPIO.output(24,True)
	tkMessageBox.showinfo( "status:lights on")

def off():
	GPIO.output(24,False)
	tkMessageBox.showinfo( "status:lights off")


B = Tkinter.Button(top, text ="LED ON", command = off)

B.pack()

B1 = Tkinter.Button(top, text ="LED OFF", command = on)

B1.pack()

top.mainloop()

