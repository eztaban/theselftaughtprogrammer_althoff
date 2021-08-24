"1"
fav_mus=["Jack Johnson",
         "Billie Eilish",
         "AURORA",
         "Johnny Cash",
         "Norah Jones"]

"2"
where_i_lived=[(55.380488, 10.447158),
               (55.364872, 10.472684),
               (55.357921, 10.508235),
               (55.297623, 10.518506),
               (55.342370, 10.420822),
               (55.149756, 10.456765),
               (55.373021, 10.580703)
               ]
"3"

me={"name":"Iason",
    "age":22,
    "height":"172cm",
    "haricolor":"Brown",
    "eyecolor":"Green",
    "origin country":"Denmark/Greece"
    }

"4"
prop=input("Enter a property you want to know about me: ")

if prop.lower() in me:
    propr=me[prop.lower()]
    print(propr)
else:
    print("We do not know this about Iason yet")

"5"
musical_dict={"Jack Johnson":["Losing Keys","Enemy","Traffic in the sky"],
              "Billie Eilish":["Bad guy", "Wish you were gay","You should see me in a crown"],
              "AURORA":["The seed","Animal","Appletree"]
              }
print(musical_dict["AURORA"])


"6"
"""
Sets are unordered and unindexed containers.
You can store multiple items in them, and store them in a single variable.
You cannot index into it and you cannot change items in them.
And you cannot have duplicates in them
the set:
my_set={"Apple", "Banana","Pear", "Apple"}
print(my_set)
>>>{"Apple", "Banana","Pear"}
You can however loop over a set - it is iterable.
You can add items
my_set.add("whatever")
my_set.remove("whatever")

and you can combine sets:
set3=my_set.union(set2)

Sets are much faster to do lookups on than lists
"""

