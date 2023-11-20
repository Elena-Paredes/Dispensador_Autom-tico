# WeightSensor.py
class WeightSensor:
    def __init__(self, data_pin, threshold_weight=100):
        self.data_pin = data_pin
        self.threshold_weight = threshold_weight

        # Configura la inicialización del sensor de peso.
        # Asegúrate de utilizar el mismo modo (BOARD o BCM) que en tu otro código
        # y de ajustar los pines según tu configuración.
        # GPIO.setup(self.data_pin, GPIO.IN)

    def get_weight(self):
        # Aquí deberías implementar la lógica para leer el peso del sensor
        # y devolver el valor obtenido
        # Puedes utilizar bibliotecas específicas si estás usando un sensor de peso dedicado.

        # Ejemplo de implementación ficticia (usando valores predefinidos):
        weight = 120  # Peso simulado en gramos
        return weight

    def is_plate_empty(self):
        weight = self.get_weight()
        return weight < self.threshold_weight
