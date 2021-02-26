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
        sum_date = sum([elem.amount for elem in self.records if elem.date == date_now])
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

    def get_calories_remained():
        calories_left = self.limit - get_today_stats()
        if calories_left > 0:
            print(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories_left} кКал')
        else:
            print('Хватит есть!')

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
        USD_RATE = 74.36
        EURO_RATE = 90.29
        if currency == 'usd':
            money_left = round(money_left/USD_RATE,2)
            currency = 'USD'
        elif currency == 'euro':
            money_left = round(money_left/EURO_RATE,2)
            currency = 'Euro'
        else:
            money_left = round(money_left,2)
            currency = 'руб'
        if money_left > 0:
            print(f'На сегодня осталось {money_left} {currency}')
        elif money_left == 0:
            print('Денег нет, держись')
        else:
            print(f'Денег нет, держись: твой долг - {abs(money_left)} {currency}')