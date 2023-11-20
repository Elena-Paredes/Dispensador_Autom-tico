# ServoMotor.py
import RPi.GPIO as GPIO
import time

class ServoMotor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.servo = GPIO.PWM(self.pin, 50)  # Configura el pin PWM a 50 Hz
        self.servo.start(0)

    def rotate(self, angle):
        duty_cycle = angle / 18 + 2
        self.servo.ChangeDutyCycle(duty_cycle)
        time.sleep(1)

    def cleanup(self):
        self.servo.stop()
        GPIO.cleanup()
