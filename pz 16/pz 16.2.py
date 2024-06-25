# Создание базового класса "Фигура" и его наследование для создания классов "Квадрат", "Прямоугольник" и "Круг".
# Класс "Фигура" будет иметь общие методы, такие как вычисление площади и периметра,
# а классы-наследники будут иметь специфичные методы и свойства.

class Figure:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError


class Square(Figure):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius


square = Square(6)
print(f"Площадь квадрата: {square.area()}")
print(f"Периметр квадрата: {square.perimeter()} \n")

rectangle = Rectangle(8, 6)
print(f"Площадь треугольнка: {rectangle.area()}")
print(f"Периметр треугольника: {rectangle.perimeter()} \n")

circle = Circle(3)
print(f"Площадь круга: {circle.area()}")
print(f"Периметр круга: {circle.perimeter()}")