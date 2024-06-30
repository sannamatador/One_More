class Animal:
    alive = True
    fed = False
    name = str()

    def __init__(self, name):
        self.food = None
        self.name = name

    def eat(self, food):
        self.food = food
        if food.edible:
            print(self.name, "съел", food.name)
            self.fed = True
        else:
            print(self.name, "не стал есть", food.name)
            self.alive = False


class Plant:
    edible = False
    name = str()

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    name = str()


class Predator(Animal):
    name = str()


class Flower(Plant):
    name = str()


class Fruit(Plant):
    edible = True
    name = str()


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.


