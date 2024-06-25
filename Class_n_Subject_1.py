# Создайте новый класс Buiding с атрибутом total
# Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных объектов класса Building total
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print
# Полученный код напишите в ответ к домашнему заданию


class Building:
    total = 0

    def __init__(self):
        Building.total += 1


for i in range(40):
    building = Building()
    print(building)

print("Общее количество зданий:", Building.total)
