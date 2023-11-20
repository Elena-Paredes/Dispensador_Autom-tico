# DisplayLED.py
class DisplayLED:
    def __init__(self, green_led_pin, yellow_led_pin, red_led_pin):
        self.green_led_pin = green_led_pin
        self.yellow_led_pin = yellow_led_pin
        self.red_led_pin = red_led_pin

        # Configuración de los pines GPIO
        # Asegúrate de utilizar el mismo modo (BOARD o BCM) que en tu otro código
        # y de ajustar los pines según tu configuración.
        # GPIO.setup(self.green_led_pin, GPIO.OUT)
        # GPIO.setup(self.yellow_led_pin, GPIO.OUT)
        # GPIO.setup(self.red_led_pin, GPIO.OUT)

    def show_message(self, message):
        # Aquí puedes implementar la lógica para mostrar el mensaje en la pantalla LED
        # Por ejemplo, encender el LED correspondiente y apagar los demás
        if message == "Lleno":
            self.turn_on_led("green")
        elif message == "Medio":
            self.turn_on_led("yellow")
        elif message == "Vacío":
            self.turn_on_led("red")

    def turn_on_led(self, color):
        # Lógica para encender el LED correspondiente
        pass

    def cleanup(self):
        # Puedes añadir código para limpiar los pines GPIO si es necesario
        pass
