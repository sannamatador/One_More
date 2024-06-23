# Создайте новый класс Building
# Создайте инициализатор для класса Building, который будет задавать целочисленный атрибут этажности self. и строковый атрибут self.buildingType
# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
# Полученный код напишите в ответ к домашнему заданию
#
class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


b1 = Building(10, 'M20')
b2 = Building(20, 'M3')
b3 = Building(5, 'M3')
b4 = Building(10, 'M20')

print(b1 == b2)
print(b1 == b3)
print(b1 == b4)
print(b2 == b3)
