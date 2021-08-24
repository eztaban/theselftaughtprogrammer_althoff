print("---------------------------------------------------------------------------------")
print("FOR LOOP")
tv1 = ["GOT", "Narcos", "Vice"]

# the way i knew to iterate
i = 0
for show in tv1:
    new = tv1[i]
    new=new.upper()
    tv1[i]=new
    i+=1

print(tv1)

# build in method to iterate with an index

tv2 = ["GOT", "Narcos", "Vice"]

for i, show in enumerate(tv2):
    new = tv2[i]
    new = new.upper()
    tv2[i]= new

print(tv2)


tv = ["GOT", "Narcos", "Vice"]
coms = ["Arrested Development", "Friends", "Always sunny"]
all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)

print("---------------------------------------------------------------------------------")
print("RANGE")
for i in range(1, 11):
    print(i)


print("---------------------------------------------------------------------------------")
print("WHILE LOOPS")

x=10
while x>0:
    print("{}".format(x))
    x-=1
print("Happy New Year!")

print("---------------------------------------------------------------------------------")
print("BREAK")

for i in range(1,101):
    print(i)
    break   # will only run once like this

qs=["What is your name?\nYour input: ",
    "What is your favorite colour?\nYour input: ",
    "What is your quest?\nYour input: "]

n=0
"""
while True:
    print("Type 'q' to quit")
    a = input(qs[n])
    if a=="q":
        break
    n=(n+1)%3
# This program will run forever if i never press "q" as input, which will quit the program.
# Using %3 keeps n from 0-3, since it will keep the remainder (modulo) as n
"""

print("---------------------------------------------------------------------------------")
print("CONTINUE")

for i in range(1,11):
    if i == 3 or i == 6 or i== 9:
        continue
    print(i)

# Here i use continue to skip a step in the iteration based on specified criteria.
# With above criteria, I could have done like:

for i in range(1,11):
    if i%3==0:
        continue
    print(i)
# But I can set any criteria to skip a certain step in the iteration

i=1
while i<=5:
    if i==3:
        i+=1
        continue
    print(i)
    i+=1


print("---------------------------------------------------------------------------------")
print("NESTED LOOPS")
# Remember the inner loop will iterate fully for each iteration of the outer loop

for i in range(1,3):
    print(i)
    for letter in ["a","b","c"]:
        print(letter)


list1=[1, 2, 3, 4]
list2=[5, 6, 7, 8]
added=[]
for i in list1:
    for j in list2:
        added.append(i+j)
print(added)
print("\n")

while input("y or n? ") != "n":
            for i in range(1,6):
                print(i)




































