from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calc_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return 3.14 * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calc_area(self):
        return self.side * self.side


new_circle = Circle(5)
print(new_circle.calc_area())
new_square = Square(4)
print(new_square.calc_area())
