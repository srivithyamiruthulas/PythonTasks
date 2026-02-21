import datetime

class CurrentTime:
    def show(self):
        return datetime.datetime.now()


c = CurrentTime()
print("Current Date and Time:", c.show())