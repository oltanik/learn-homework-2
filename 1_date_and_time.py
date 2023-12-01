"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta

def print_days():
    dt_now = datetime.now()
    delta = timedelta(days=1)
    delta_month = timedelta(days=30)
    print(f'вчера {dt_now - delta}, сегдня {dt_now}, 30 дней назад {dt_now - delta_month}')


def str_2_datetime(date_string):
    date_f = datetime.strptime(date_string, '%d/%m/%y %I:%M:%S.%f')
    return date_f
    

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
