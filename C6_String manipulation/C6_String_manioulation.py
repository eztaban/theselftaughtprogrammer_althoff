concatinated_string="cat "+"in "+"the "+"hat"
print(concatinated_string)


multiplied_string="lawyer "*3
print(multiplied_string)

upper_string="We hold these folks accountable... ".upper()
print(upper_string)

lower_string="...OR SOMETHING".lower()
print(lower_string)

capitalize_string="only small letters".capitalize()
print(capitalize_string)


format_string="Iason {}".format("Gram")
print(format_string)

lastname="Gram"
format_string2="Iason {}".format(lastname)
print(format_string2)

first_name="Iason"
lastname="Gram"
format_string3="{} hedder {} til efternavn".format(first_name, lastname)
print(format_string3)

"""----------------------
n1=input("Enter a person: ")
v=input("Enter a verb: ")
adj=input("Enter an adjective: ")
n2=input("Enter a second nound: ")
r="""#The {} {} the {} {}    #remove the # to the left
#    """.format(n1, v, adj, n2)
#print(r)
#-------------------------"""


split_string="Hello.Iason!".split(".")
print(split_string)

words=["The", "fox", "jumped", "over", "the", "fence."]
join_string=" ".join(words)
print(join_string)

stripped_string="        The        "
s=stripped_string.strip()
print(stripped_string)
print(s)


replace_string="All living beings are equal"
rep=replace_string.lower().replace("a","@")
print(rep)
# Replace all "a" with "@". Here i added .lower() to also swap "A" for "@"


idex_m="animals".index("m")
print(idex_m)
# ValueError if there is no match

#"animals".index("z")
# above line will return the valueerror

try:
    "animals".index("z")
except:
    print("Not found.")


test="Cat" in "Cat in the hat"
print(test)

test2="Bat" in "Cat in the hat"
print(test2)

test3="Potter" not in "Harry"
print(test3)


# To keep quotes inside string, preface " with \, like "She said \"Surely\""
# It is not needed to excape single quotes inside double qoutes.  "  'Something'  " 
# Neither is it needed to escape doubles inside singles.  '  "Something"  '

print("Line1\nLine2\nLine3")

# Slicing list & string
fict = ["Tolstoy", "Camus", "Orwell", "Huxley", "Austin"]
sliced=fict[0:3]
print(fict)
print(sliced)

Ivan="In place of death, there was light."
sliced1=Ivan[:19]
Sliced2=Ivan[19:]
print(Ivan,"\n",sliced1,"\n", Sliced2)

