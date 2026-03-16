from abc import ABC
class Shape(ABC):
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        print(3.14 * self.r * self.r)

c = Circle(5)
c.area()