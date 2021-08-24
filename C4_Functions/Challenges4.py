"1"
def square(x):
    return x**2

#r=square(4)
#print(r)



"2"
def print_statement(y):
    """
    :param y: str.
    :return: Prints the input
    """
    return print(y)

#print_statement("Iason")


"3"
def three_req(x,y,z, a=2, b=3):
    """
    :param x: int
    :param y: int
    :param z: int
    :param a: int - optional
    :param b: int - optional
    :return: x+y+z-(a+b)
    """
    tots=x+y+z
    return tots-(a+b)

#print("The result is: ", three_req(1,2,3))

"4"
def div_2(x):
    """
    :param x: int.
    :terurn: x/2
    """
    return x/2

def mult_4(x):
    """
    :param x: int.
    :return: x*4
    """
    return x*4
#r1=div_2(6)
#r2=mult_4(r1)
#print(r2)

"5"
def str_float(x):
    """
    :param x: int or float, but as str.
    :return: float(str)
    """
    try:
        print(float(x))
    except ValueError:
        print("Invalid error. Your input could not be converted to float")
#str_float("2,0")


