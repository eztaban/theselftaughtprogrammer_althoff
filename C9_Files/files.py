import os

os.path.join("Users", "iason", "st.txt")
# Like this, I avoid the annoying part of slashes being different in unix and windows
# Help can be found at: https://theselftaughtprogrammer.io/filepaths

"""
"r" - opens the file for reading only
"w" - opens the file for writing only. Overwrites the file if it exists, creates it if it doesnt
"w+" - opens the file for read and write. Overwrites if existing, creates if not
"""

st = open("st.txt", "w")        # creates a file object (st) with open, and we want to write to it
st.write("Hi from Python!")     # we use the write method on the object. It accepts strings.
st.close()                      # We use close method to close the file properly


"""
A safer way is to use with statement, since it closes the file automatically
"""
with open("st1.txt", "w") as f:         # we assign the object st1.txt to the variable name f
    f.write("Hi again from Python!")    # we use the method write, which accpets a string, on f

                                        # it is closed automatically, since it is inside with, which we like!


with open("st1.txt", "r") as f:         # we open it the same way as before
    print(f.read())                     # now we use the method .read() on f and print it

"""
To save the content of a file, it has to be saved in a different variable if it is needed later
"""

my_list=list()                  #creates empty list

with open("st1.txt", "r") as f: # opens file, assigns it to f
    my_list.append(f.read())    # reads the content and appends it to my list
    
print(my_list)                  # we see it is now in the list for later use

