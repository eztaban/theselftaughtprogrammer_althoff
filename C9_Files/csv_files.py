import csv

with open("st.csv", "w", newline='') as f:      # we open the file as f
    w=csv.writer(f, delimiter=",")              # csv has a method - writer - which accepts a file object and a delimiter (seperator). This csv object containing the file f, is saved in the variable w
    w.writerow(["one","two","three"])           # we write a row containing 3 cells seperated by ","
    w.writerow(["four", "five","six"])          # next row. Rows a seperated by a space " " as stated in the open statement

with open("st.csv", "r", newline='') as f:      # reading the file is the same but...
    r=csv.reader(f, delimiter=",")
    for row in r:                               # we iterate over each line to see them in console
        print(",".join(row))
"""
We open the file and convert it to a csv object with the reader method.
It is saved in the variable r.
I then iterate over the file in the loop and use the .join method on a comma, to add a comma between each
piece of data in the file and print the content to make it appear like it does in the file.
"""
