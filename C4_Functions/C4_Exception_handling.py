
try:
    a = input("Input nominator, a: ")
    b=input("Input denominator, b: ")
    a=float(a)
    b=float(b)
    good=True
except ValueError:
    print("Your input has to be numbers")
    good=False
    
if good==True:
    try:
        print("a/b equals ", a/b)
    except ZeroDivisionError:
        print("The denominator cannot be zero")
        print("You screwed up... wow that's not good")
else:
    print("You screwed up")

