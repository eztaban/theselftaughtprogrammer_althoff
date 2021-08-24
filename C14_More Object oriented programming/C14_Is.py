class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob=bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)

"""
the keyword 'is' returns 'True' if two objects are the same objects and 'False' if not.
When comparing 'bob' and 'same_bob' it returned 'True' since they both pointed back
'Person-object'.
When comparing 'bob' and 'another_bob', they pointed to two different 'Person-objects'
and so it returned 'False'
"""

x = 10
if x is None:
    print("x is None :( ")
else:
    print("x is not None")

x = None
if x is None:
    print("x is None :( ")
else:
    print("x is not None")

