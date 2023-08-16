import RPi.GPIO as GPIO 
import time 

buzzer_pin = 18 
GPIO.setmode(GPIO.BCM)
GPIO.setup( buzzer_pin , GPIO.OUT , intial = GPIO.LOW)

def buzz(pitch , duration ):
    period = 1.0 / pitch 
    delay = period / 2
    cycles = int(duration * pitch)
    for i in range(cycles):
        GPIO.output( buzzer_pin , True )
        time.sleep(delay)
        GPIO.output( buzzer_pin , False)
        time.sleep(delay)

while True :
    pitch = int(input("Enter the pitch (200 to 2000): "))
    duration = int(input("enter the duration (seconds)"))
    buzz(pitch , duration )
    