import math
class Circle:
    def __init__(self, r):
        """
        :attr r: is radius in cm
        """
        self.radius = r

    def area(self):
        return round(math.pi*self.radius**2, 2)

circle = Circle(6)
print(circle.area())
