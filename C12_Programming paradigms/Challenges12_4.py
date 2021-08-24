import math
class Hexagon:
    def __init__(self, sl):
        """
        :attr sl: length of side in cm
        """
        self.sidelength = sl

    def perimiter(self):
        return 6*self.sidelength
    def area(self):
        return round((3*math.sqrt(3))/2*self.sidelength**2, 2)

hexagon = Hexagon(12)
print("The perimiter of the hexagon is: ", hexagon.perimiter(), "cm")
print("The area of the hexacon os: ", hexagon.area(), "cm^2")
    
