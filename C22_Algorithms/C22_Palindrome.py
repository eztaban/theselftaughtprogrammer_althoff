"""
Palindrome: words that are written the same forwards and backwards
"""

def palindrome(word):
    word = word.lower()
    return word[::-1] == word

print(palindrome("Mother"))
print(palindrome("Mom"))

"""
[::-1]
is pythons way of returning a slice of an iterable in reverse
"""
