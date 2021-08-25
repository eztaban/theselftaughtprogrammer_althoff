"""
To check each element in a list, if it matches your search parameter
"""

def ss(number_list, n):
    idx=[]
    found = False
    for i in number_list:
        if i == n:
            found = True
            idx.append(number_list.index(i))
            break
    return found, idx

numbers = list(range(0,100))
s1 = ss(numbers, 2)
print(s1)

s2=ss(numbers, 202)
print(s2)
