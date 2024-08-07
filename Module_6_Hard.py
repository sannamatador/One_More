import math


class Figure:
  sides_count = 0
  def __init__(self, sides, color):
    self.__sides = sides
    self.__color = color 
    self.filled = False
    if self.__sides != self.sides_count:
      self.__sides = [1]*self.sides_count

  def get_color(self):
    return self.__color

  def __is_valid_color(self, r, g, b):
    if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
      return True

  def set_color(self, r, g, b):
    if self.__is_valid_color(r, g, b):
      self.__color = [r, g, b]
  
      
  def get_sides(self):
    return self.sides

  

  def __is_valid_sides(self, sides):
    if sides > 0 and isinstance(sides, int) and sides == self.get_sides():
      return True
    
  def __len__(self, *sides):
    return sum(sides)
  
  def set_sides(self, *new_sides):
    if self.sides_count == len (new_sides):
      self.sides = list(new_sides)
      
  def get_perimeter(self):
   return sum(self.sides)   
  

class Circle(Figure):
  sides_count = 1
  def __init__(self, color, sides):
    super().__init__(sides, color)
    self.sides = sides
    self.__radius = self.sides / 3.14
 
  def get_square(self):
    return self.__radius**2*3.14

    
class Triangle(Figure):
  sides_count = 3
  def __init__(self,color,sides):
    super().__init__(sides, color)
    p = sides.sum() / 2
    self.sides = sides
    self.__height = (2*math.sqrt(p*(p-sides[0])*(p-sides[1])*(p-sides[2])))

  def get_square(self):
    return self.sides[0]*self.__height/2
     
  

class Cube(Figure):
  sides_count = 12
  def __init__(self, color, sides):
    super().__init__(sides, color)
    self.sides = [sides]*12

  def get_volume(self):
    return self.sides[0]**3
   

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(circle1.get_perimeter())

# Проверка объёма (куба):
print(cube1.get_volume())

print((cube1.get_perimeter()))
