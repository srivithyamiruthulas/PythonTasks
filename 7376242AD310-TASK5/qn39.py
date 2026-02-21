import datetime

class DateInfo:
    def get_info(self):
        today = datetime.date.today()
        return today.year, today.month


d = DateInfo()
year, month = d.get_info()
print("Year:", year)
print("Month:", month)