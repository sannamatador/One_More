class Horse:
    x_distance = 0
    sound = 'Frrr'

    def __init__(self):
        self.dx = 0

    def run(self, dx):
        self.dx = dx
        self.x_distance += self.dx


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self):
        self.dy = 0

    def fly(self, dy):
        self.dy = dy
        self.y_distance += self.dy
      

class Pegasus(Eagle, Horse):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(super().sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
