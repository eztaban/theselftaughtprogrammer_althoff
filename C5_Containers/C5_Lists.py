"""
"Lists"
"------------------------------"
fruit=["Apple","Orange","Pear"]
print(fruit)
fruit.append("Banana")
fruit.append("Peach")
print(fruit)
fruit[2] #This allows you to acces elements in a given index position
fruit[1]="Blue" #assigning new value
print(fruit)


last=fruit.pop() #remove last item
print(last)
print(fruit)
fruit2=["Peach"]
fruit=fruit+fruit2 #put together two separate lists
print(fruit)

#Check if item is in a list (here I print the output)
print("Peach" in fruit)
print("Peach" not in fruit)

print("The length of the list 'fruit' is: ",len(fruit))

colors = ["purple", "orange", "green"]
guess=input("Guess a color: ")

if guess.lower() in colors:
    print("You guessed correctly")
else:
    print("Wrong, try again!")

"Tuples"
"---------------------------------"
#Tuples must have commas between the elements, and always after the first - even if it is alone.
#This way Python knows it is not a number in a parenthesis like (9)+1.

dys=("1984","Brave New World","Fahrenheit 451")
print(dys[2])
print("1984" in dys)
#good for values that will not change, and shouldnt be changed by accident by the program


"Dictionaries"
"--------------------------------"
fruits={"Apple":"Red",
        "Banana":"Yellow"}
#"Key":"Value"
print(fruits)
fruits["Pear"]="Green" #Lets you add key:value pair
print(fruits["Pear"])  #Lets you see the value related to that key
#Note, dicts has no order - here, the key is used as index
#String or tuple can be a key, but a list or dictionary cannot.
print("Is 'Apple' in fruits? ","Apple" in fruits)
del fruits["Apple"]
print(fruits)


rhymes = {"1":"Fun",
          "2":"Blue",
          "3": "Free",
          "4":"Four",
          "5":"Jive"
          }
n=input("Type a number: ")
if n in rhymes:
    rhyme=rhymes[n]
    print(rhyme)
else:
    print("Not found, try a different number")

"""

"Containers in containers"
"-------------------------------------------"
"Lists in lists"
lists=[]
rap=["Kanye West",
     "Jay Z",
     "Eminem",
     "Nas"]
rock=["Bob Dylan",
      "The Beatles",
      "Led Zeppelin"]
djs=["Zeds Dead",
     "Tiesto"]
lists.append(rap)
lists.append(rock)
lists.append(djs)
print(lists)
print(lists[0]) #acces the first elements in lists - here that is the list with rappers
rap.append("Kendrick Lamar")
print(lists)
#You can store tuples in lists, lists in tuples, dicts in lists or tuples.

print(lists[0][0]) #How to access lowe level lists elements.
#Had there been a list inside, then that would have been lists[0][0][0]























