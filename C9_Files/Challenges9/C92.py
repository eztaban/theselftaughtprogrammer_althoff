answer=input("Please state your name: ")

with open("C92.txt", "w") as f:
    f.write("Your name is stated to be: "+ answer)
