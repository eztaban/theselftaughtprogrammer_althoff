class Lion:
    def __init__(self, name):
        self.name = name

lion = Lion("Dilbert")
print(lion)

"""
When printing a Lion object, Python calls a magic method ""__repr__"" it has inherited from "Object".
It prints whatever '__repr__' returns.
It can be overriden like so:
"""

class Elephant:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

elephant = Elephant("Dory")
print(elephant)

"""
Notice the difference on the output of calling 'print(lion)' and 'print(elephant)'.
Both instances i call the object and not an attribute of the object.
The first output is the normal one, the second one is modyfied to show the attribute 'self.name'.

All operators are also magic methods: '2+2' is actually '2 __add__ 2'
This can also be modyfied ie like shown:
"""

class AlwaysPositive:
    def __init__(self,number):
        self.n=number

    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)
print(x+y)

"""
I have changed the '__add__' method to return the absolute value of a number.
Note that x and y must be of the class 'AlwaysPositive' for this kind of addition to work.
Had they been normal numbers, normal addition would have taken place
"""
