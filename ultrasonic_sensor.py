# ultrasonic_sensor.py
#Si el sensor detecta una distancia de 2cm, el recipiente que almacena la comida está lleno.
#Si el sensor detecta una distancia de 5cm, el recipiente que almacena la comida está a nivel medio.
#Una distancia >5cm significa que el recipiente que almacena la comida está vacío.
import RPi.GPIO as GPIO
import time

class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def get_distance(self):
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, False)

        start_time = time.time()
        stop_time = time.time()

        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()

        while GPIO.input(self.echo_pin) == 1:
            stop_time = time.time()

        elapsed_time = stop_time - start_time
        distance = (elapsed_time * 34300) / 2  # Velocidad del sonido en el aire ~343 m/s

        return distance

    def detect_food_level(self):
        distance = self.get_distance()

        if distance < 2:
            return "Lleno"
        elif 2 <= distance < 5:
            return "Medio"
        else:
            return "Vacío"

    def cleanup(self):
        GPIO.cleanup()
