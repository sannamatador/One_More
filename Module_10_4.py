import threading
import random
from queue import Queue
import time



class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        a = random.randint(3, 10)
        time.sleep(a)


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            table_assigned = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    guest.start()
                    table_assigned = True
                    break

            if not table_assigned:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty():
            flag = False
            for table in self.tables:
                if table.guest is not None and table.guest.is_alive():
                    flag = True
                    break
            for table in self.tables:
                guest = table.guest
                if guest is not None and not guest.is_alive():
                    print(f"{guest.name} покушал(-а) и ушел(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

                if self.queue.empty():
                    continue

                if guest is None:
                    next_guest = self.queue.get()
                    table.guest = next_guest
                    print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    next_guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
print("Все гости закончили есть и ушли")
