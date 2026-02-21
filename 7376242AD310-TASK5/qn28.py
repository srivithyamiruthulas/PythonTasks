class Sensor:
    def read(self):
        pass

class Temperature(Sensor):
    def read(self):
        print("Temperature is 30°C")

class Humidity(Sensor):
    def read(self):
        print("Humidity is 60%")


s = Temperature()
s.read()