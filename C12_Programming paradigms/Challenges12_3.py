class Triangle:
    def __init__(self, h, b):
        """
        :attr h: height in cm
        :attr b: length of baseline in cm
        """
        self.height = h
        self.baseline = b

    def area(self):
        return 0.5*self.height*self.baseline

triangle = Triangle(20, 15)

print(triangle.area())
