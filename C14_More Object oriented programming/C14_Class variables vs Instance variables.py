class Rectangle():
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("{} by {}".format(self.width, self.len))


r1 = Rectangle(10,24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)


"""
Notice that ".recs" is a variable of the class and not specific to any of the instances.
This is a class variable, where as the "self.width", "self.len" are instance variables.
Instance variables are called from the instance like so: """

print(r1.width)

"""
whereas ".recs" was called from the class.
It allows me to share data between all instances of the class w/o having global variables.
This way I could fx make a summary of all my isntances of this class simply by calling
the class.
"""

