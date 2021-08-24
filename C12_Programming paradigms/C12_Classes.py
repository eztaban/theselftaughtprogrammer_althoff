class Orange:
    def __init__(self, w, c):
        """weights are in g"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        """
        days: days after being picked
        temp: avg temp during storage
        """
        self.mold = days*temp


    
or1 = Orange(200, "dark orange")

# print(or1)
print(or1.weight)
print(or1.color)

or1.weight = 300
or1.color = "light orange"

print(or1.weight)
print(or1.color)

"""
I can create multiple oranges with varying values for their charachtaristicas
"""

or2 = Orange(400, "light orange")
or3 = Orange(800, "dark orange")
or4 = Orange(140, "yellow")


"""Using the rot method"""
orange = Orange(300, "orange")
print("How molden is the orange?", orange.mold)
orange.rot(10, 4)
print("How molden is the orange?", orange.mold)

