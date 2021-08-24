n=1
while n==1:
    numlist=[1, 2, 5, 28, 55, 33, 27, 99]
    print('enter "q" to quit')
    name=input("Your name: ").upper()
    n=2
    if name=="Q":
        break
    while True:
        print('enter "q" to quit')
        a=input("Guess a number between 0 to 100: ")
        if a=="q":
            n=1
            break
        elif int(a) in numlist:
            print("\nYOU SUCCEDED!, CONGRATULATIONS {}\n".format(name))
            b = input("Do you want to go again? y/n: ")
            if b=="n":
                break
            else:
                n=1
                continue
