
# 1
lst=["The Walking Dead", "Entourage", "The sopranos", "The vampire diaries"]

for show in lst:
    print(show)

# 2
for n in range(25,51):
    print(n)

# 3
idx=0
for show in lst:
    print(idx, show)
    idx+=1

# 4
n=1
while n==1:
    numlist=[1, 2, 5, 28, 55, 33, 27, 99]
    print('enter "q" to quit')
    name=input("Your name: ")
    n=2
    if name=="q":
        break
    while True:
        print('enter "q" to quit')
        a=input("Guess a number between 0 to 100: ")
        if a=="q":
            n=1
            break
        elif int(a) in numlist:
            print("You succeded!, Congratulations {}".format(name))
            b = input("Do you want to go again? y/n: ")
            if b=="n":
                break
            else:
                n=1
                continue


# 5
lst1=[8, 19, 148, 4]
lst2=[9 , 1, 33, 83]
rslt= []
for num in lst1:
    for numb in lst2:
        rslt.append(num*numb)
print(rslt)
