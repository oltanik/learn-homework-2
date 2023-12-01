"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

list_people = [
        {'name': 'Джони', 'age': 18, 'job': 'Analytic'},
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]



def main():
    with open('people_work.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        wtiter = csv.DictWriter(f, fields, delimiter=';')
        wtiter.writeheader()
        for user in list_people:
            wtiter.writerow(user)

if __name__ == "__main__":
    main()
