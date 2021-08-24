x=2

def haha():
    #global x
    x=3
    print("This is from inside the function: ", x)
    
haha()
print("This is from outside the function, and should be different, i global is not used: ", x)
