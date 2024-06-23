# Создайте новый класс Buiding с атрибутом total
# Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных объектов класса Building total
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print
# Полученный код напишите в ответ к домашнему заданию

class Building:
    total_ = 20

    def __init__(self, total_):
        total_ = 40
        self.total_ = int(total_)
        for i in range(0, self.total_):
            # a = Building(i)
            print("Объект Building ", i + 1)


a = Building(5)
