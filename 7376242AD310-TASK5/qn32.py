class RoundValue:
    def __init__(self, value):
        self.value = value

    def round_number(self):
        return round(self.value, 2)


value = float(input("Enter value: "))
r = RoundValue(value)
print("Rounded value:", r.round_number())