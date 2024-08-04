"""Задача "Потоковая запись в файлы":
Необходимо создать функцию wite_words(word_count, file_name), где word_count - количество записываемых слов, file_name -
название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после
записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>"."""

from threading import Thread
from time import sleep
from datetime import datetime

time_start = datetime.now()

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding="utf-8") as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


х1 = write_words(10, 'example1.txt')
х2 = write_words(30, 'example2.txt')
х3 = write_words(200, 'example3.txt')
x4 = write_words(100, 'example4.txt')

time_end = datetime.now()
print(f'Время работы программы: {time_end - time_start}\n')

time_start = datetime.now()


thr_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=write_words,args=(200, 'example7.txt'))
thr_4 = Thread(target=write_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time_end = datetime.now()
print(f'Время работы программы: {time_end - time_start}')
