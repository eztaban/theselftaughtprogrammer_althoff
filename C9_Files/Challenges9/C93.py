import csv

lists = [[ "Top gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"] , ["Training day", "Man on fire", "Flight"]]

with open("C93.csv", "w", newline='') as f:
    w=csv.writer(f, delimiter=",")
    w.writerow(lists[0])
    w.writerow(lists[1])
    w.writerow(lists[2])
"""
Indexing into nested lists are most easily done with numpy:
>>> data = np.array([ [0, 1], [2,3] ])
>>> data[:,0]
array([0, 2])

This takes the zoroeth element of all the lists and put them together in a lew array, resulting in an array with [0,2].

To access the number 1, for instance:
data[0,1]
This takes the zeroeth element ([0,1]) and then the first element (1).

Numpy is really good for working in wimensions like this, since the data could be shown as:
data:
[
[0,1],
[2,3]
]

meaning that the first entry in the numpy scheme is the line, and the next one is the element in that line

"""
