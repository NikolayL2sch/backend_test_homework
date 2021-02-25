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

class Record:
    def __init__(self, amount, comment, date = None):
        date_format = '%d/%m/%y'
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, date_format).date()

class CalorieCalc(Calc):
    
