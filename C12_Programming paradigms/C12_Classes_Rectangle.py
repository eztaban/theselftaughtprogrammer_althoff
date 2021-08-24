class Rectangle():
    def __init__(self, w, l):
        """
        naming the methods and assigning them the values
        """
        self.width = w
        self.len = l

    def area(self):
        """
        calculates the area
        I dont have to pass w or l in here, since it passes self.
        """
        return self.width*self.len

    def change_size(self, w, l):
        """
        a method that allows to change the size
        Now I have to pass new values for w and l, so these must be entered
        """
        self.width = w
        self.len = l

rectangle = Rectangle(10,20)

print(rectangle.area())
rectangle.change_size(20,40)
print(rectangle.area())
