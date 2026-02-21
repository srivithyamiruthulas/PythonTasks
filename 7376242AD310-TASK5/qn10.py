class Device:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = "OFF"

    def turn_on(self):
        self.status = "ON"
        print(self.device_id, "is ON")

    def turn_off(self):
        self.status = "OFF"
        print(self.device_id, "is OFF")


d = Device("Light01")
d.turn_on()
d.turn_off()