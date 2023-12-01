"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as f, open('referat2.txt', 'w', encoding='utf-8') as new_f:
      content = f.read() # прочитал текст в переменную
      len_content = len(content) # посчитал длину получившегося текста
      count_row = len(content.split()) # посчитал количество слов
      for row in content: 
        row = row.replace('.', '!') # заменил точки на восклицательный знак
        new_f.write(row) # сохранил результат в файле referat2.txt

if __name__ == "__main__":
    main()
