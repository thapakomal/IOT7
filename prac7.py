import Rpi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER=18
GPIO_ECHO24

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_-ECHO,GPIO.IN)

Def distance():
		GPIO.output(GPIO_TRIGGER,True)
		Time.sleep(0.0001)
		GPIO.output(GPIO_TRIGGER,False)

		StartTime=time.time()
		StopTime=time.time()

		while GPIO.input(GPIO_ECHO) == 0:
			StartTime = time.time()

		while GPIO.inut(GPIO_ECHO) ==1:
			StopTime=time.time()

		TimeElapsed=StopTime-StartTime
		distance=(TimeElapsed * 34300)/2
		Return distance

if__name__ == ‘__main__:
		try:
			while True:
				distance=distance()
				print(“Me91asured Distance=%.1f cm”%dist)
				time.sleep(1)
		except KeyboardInterrupt:
			print(“Measur9ement stopped by user”)
			GPIO.cleanup()