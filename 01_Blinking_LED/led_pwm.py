from Rpi.GPIO import GPIO 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18 , GPIO.OUTPUT )

pwm_led = GPIO.PWM(18 , 500)
pwm_led.start(100)
while True :
    duty_s = input("Enter Brightness (0-100) : ")
    duty = int(duty_s)
    pwm_led.ChangDutyCycle(duty)
