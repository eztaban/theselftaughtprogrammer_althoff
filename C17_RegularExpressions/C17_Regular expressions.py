import re
# Simple match
"""
're' is for regular expressions.
're' has a module '.findall'
We can pass it a string to search for in a file and it will return
all the matches in that file og variable or whatever
"""

l = "Beautiful is better than ugly."

matches = re.findall("Beautiful", l)
print(matches)

matches=re.findall("beautiful", l, re.IGNORECASE)
print(matches)

# Match beginning and end
"""
In bash, you can find patterns where the line begins with something with:
grep ^If zen.txt
It will then look for lines that begins with 'If' in the file 'zen.txt'.
To find lines that end with something:
grep idea.$ zen.txt
The '.$' looks for lines that end with that pattern

grep idea.$ zen.txt
grep idea.$ zen.txt
"""

zen = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

m = re.findall("^If", zen, re.MULTILINE)

print(m)
"""
Here i look for all instances of 'If' in 'zen'. I have to pass the parameter 're.MULTILINE' to make it look in multiple lines
"""

# Match multiple Characthers
"""
In bash: echo Two too. | grep -i t[ow]o
"""

string = "Two too"
m = re.findall("t[ow]o", string, re.IGNORECASE)

print(m)

# Match digits
"""
In bash: 34 hello. | grep [[:digit:]]
"""

line = "123?34 hello?"
m = re.findall("\d", line, re.IGNORECASE)
print(m)

# Repitition
"""
Adding an '*' will allow me to look for any number of charachters like so:
In bash: echo two twoo not too. | grep -o two*
This will look for 'tw' followed by any number of 'os'

A period matches any character and if i follow a period with an asterix, we look for any character any amount of times.
This is usefull to find something between two known characters like so:
In bash: echo __hello__there | grep -o __.*__
This looks for anything between '__' and '__'. In this case it will return '__hello__'

An asterix is greedy, meaning, if there are multiple matches, it will take them all:
in bash: echo __hi__bye__hi__there | grep -o __.*__
Returns: __hi__bye__hi__

In python we can make the asterix non-greedy by following it with a question mark. This cannot be done with grep
"""

t = "__one__ __two__ __three__"

found = re.findall("__.*?__", t)

for match in found:
    print(match)
print(found)
"As we see, it finds several matches, but they are seperated in a list"


# Escaping
"""
We can escape the meaning of a charachter to match it.
Characters like '$' has special meanings (look for a match at the end of a line),
but escaping it allows us to match it:
In bash: echo I love $ | grep \\$
Returns: I love $
with $ marked as a match
"""
line = "I love $"
m = re.findall("\\$", line, re.IGNORECASE)
print(m)

