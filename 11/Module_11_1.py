import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import requests


# Библиотека request
# Делаем запрос на сайт
r = requests.get('https://adme.media/articles/60-fraz-s-samymi-nuzhnymi-anglijskimi-glagolami-1077610/')  
# Получаем код ответа
status_code = r.status_code
print(status_code)
# Получаем содержимое страницы
print(r.text)
# Получаем заголовки заданного типа
print(r.headers['content-type'])

# Библиотека matplotlib
# Строим график
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [25, 32, 34, 20, 25, 23, 21, 33, 19, 28]
plt.plot(x, y)
plt.show()
# Строим диаграмму
x = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
y = [2, 10, 3, 9, 7]
plt.bar(x,y)
plt.show()


# Библиотека pillow
# Открываем изображение
im = Image.open("mymy.jpg")
# Получаем размеры изображения и формат
print(im.format, im.size, im.mode)
# Преобразуем в черно-белое и сохраняем в другом файле
with Image.open("mymy.jpg") as im:
  im = im.convert("L")
  im.save("mymy1.jpg")


# Библиотека pandas
# Создание датафрейма из данных, введенных вручную
df = pd.DataFrame([[1,'Иван', 'Петров'], [2,'Айлар', 'Бердыева'], [3,'Джон', 'Доу']], columns=['id', 'name', 'job'])
# Вывод на печать
print(df)
# Создание датафрейма из файла
df = pd.read_csv('./Sheet1.csv')
# Вывод информации
print(df.info)
