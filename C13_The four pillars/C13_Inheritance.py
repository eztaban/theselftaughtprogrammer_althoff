class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

class Square(Shape):
    pass

a_square = Square(20,20)
a_square.print_size()


"""
A class, Shape, has been made with attributes.
The class Square, then inherits all the methods and attributes from Shape.
This means I won't have to write as much code, which is easier to maintain

I can still define methods in the child class w/o affecting the parent class.

If I make a method in the child class w/ the same name as in the parent class,
it is called method overriding and does not affect the parent class
"""

class Square2(Shape):
    def area(self):
        print(self.width*self.len)
    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))
    
a_square = Square2(20,20)
a_square.area()
a_square.print_size()

"""
In Square2 i inherit from Shape, add the method "area" and override with the method "print_size", all w/o
affecting the parent class, Shape

This means, that a more generic version of a class can be made, and a lot more specific classes
can inherite attributes and methods from that and then be further specialized.
This removes a lot of repetitive writing
"""
