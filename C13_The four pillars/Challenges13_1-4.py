class Shape():
    def __init__(self):
        pass
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimiter(self):
        print(self.width*2+self.len*2)

class Square(Shape):
    def __init__(self, sl):
        self.sidelen = sl

    def calculate_perimiter(self):
        print(self.sidelen*4)

    def change_size(self, n):
        self.sidelen = self.sidelen + n




rec = Rectangle(2, 3)
sqr = Square(4)

rec.what_am_i()
sqr.what_am_i()

class Rider():
    def __init__(self, name):
        self.name = name
        
class Horse():
    def __init__(self, name, breed, height, rider):
        self.name = name
        self.breed = breed
        self.height = height
        self.rider = rider

ray = Rider("Rachel Langford")

vordis = Horse("Vordis", "Icelandic", 140, ray)

print(vordis.rider.name)
print(vordis.name)
print(vordis.breed)
print(vordis.height)

