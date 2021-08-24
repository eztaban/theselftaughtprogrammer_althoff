"""
Composition is about relations between two objects ie. a dog and the owner.
I create a class for the dog and the owner, and then one attribute of the dog
is its owner, which will then be the person-object
"""

class Dog():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self, name):
        self.name = name

iason = Person("Iason Gram")
blue = Dog("Blue", "Husky", iason)

print(blue.owner.name)

"""
Notice, that the dogs owner is a variable and not a string.
When printing the dogs owners name i call the 'owner'-attribute of the dog.
This attribute is the variable 'iason', which has its own attribute 'name'.
So i call an attribute of an attribute.
"""
