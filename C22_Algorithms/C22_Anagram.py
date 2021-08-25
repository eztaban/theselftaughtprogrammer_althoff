"""
anagram: words are anagrams if they can be used to spell each other by rearranging their letters
Sorted sorts the elements of a string in alpabetical order.
"""
def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1)==sorted(w2)

print(anagram("iceman", "cinema"))
print(anagram("leaf", "tree"))
