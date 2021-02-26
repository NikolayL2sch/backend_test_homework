# requires pytest, pip, pytest-html

# here should be the imports
import datetime as dt

# parent-class
class Calc:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record (self,Record):
        records.append(Record)

    def get_today_stats(self):
        date_now = dt.datetime.now().date()
        sum_date = sum([elem.amount for elem in self.records if elem.date = date_now])
        return sum_date
    
    def get_week_stats(self):
        date_now = dt.datetime.now().date()
        tmp = [date_now - dt.timedelta(days = i) for i in range (7)]
        sum_week = sum([elem.amount for elem in self.records if elem.date in tmp])
        return sum_week

class Record:
    def __init__(self, amount, comment, date = None):
        date_format = '%d/%m/%y'
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, date_format).date()

class CaloriesCalculator(Calc):
    def __init__(self, limit):
        super().__init__(limit)

    def add_record (self,Record):
        super().add_record(Record)
    
    def get_today_stats (self):
        super().get_today_stats(self)
    
    def get_week_stats (self):
        super().get_week_stats(self)

class CashCalculator(Calc):
    def __init__(self, limit):
        super().__init__(limit)

    def add_record (self,Record):
        super().add_record(Record)

    def get_today_stats (self):
        super().get_today_stats(self)
    
    def get_week_stats (self):
        super().get_week_stats(self)
    
    def get_today_cash_remained(currency):
        money_left = self.limit - get_today_stats()
        