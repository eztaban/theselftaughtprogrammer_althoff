# 1
print("Camus")

# 2
#a = input("Input noun: ")
#b = input("Input person: ")

#print("Yesterday I wrote a {a}. I sent it to {b}!".format(a=a, b=b))

def wordplay(a="nothing", b="no one"):
    """
    a = noun
    b = person
    """
    print("Yesterday I wrote a {a}. I sent it to {b}!".format(a=a, b=b))

wordplay("song", "my girlfriend")

# 3
Assignment="aldous Huxley was born in 1894".title()
print(Assignment)

# 4
s="Where now? Who now? When now?".split("?")
#l=s.split("?")
print(s)

# 5
fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
fox = fox[0: -2] + "."  # her er fox indtil næstsidste charachter valgt og der er tilføjet et punktum.
                        # Det er basically en ny string.
print(fox)

# 6
six="A screaming comes across the sky"
six=six.replace("s", "$")
print(six)

# 7
Hem="Hemingway".index("m")
print(Hem)

# 8
Quote1= "'Drink up, my fellows yo-ho' said Jack"
Quote2='"What", he saig angrily'
Quote3="He wanted to say \"Now that is stupidity\""
print(Quote1,"\n",
      Quote2,"\n",
      Quote3)

# 9
wert="t"+"h"+"r"+"e"+"e"
qwerty=(wert+" ")*3
print(qwerty)

# 10
asd="It was a bright cold day in April, and the clocks were striking thirteen."
print(asd.index(","))
print(asd[:33])
