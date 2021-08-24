class Square:
    square_list = []

    def __init__(self, sl):
        self.sidelength = sl
        #self.len = l
        self.square_list.append((self.sidelength))
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.sidelength,self.sidelength,self.sidelength,self.sidelength)

sq1=Square(10)
sq2=Square(25)

print(Square.square_list)
print(sq1)


def same(obj1, obj2):
    print(obj1 is obj2)

same(sq1, sq2)
same(sq1, sq1)
