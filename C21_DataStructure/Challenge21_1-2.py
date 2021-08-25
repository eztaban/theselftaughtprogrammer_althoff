class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        "returns True if stack is empty"
        return self.items == []

    def push(self, item):
        "appends item to self"
        self.items.append(item)

    def pop(self):
        "removes last item from self"
        return self.items.pop()

    def peek(self):
        "returns next to last item in self"
        last=len(self.items)-1
        return self.items[last]

    def size(self):
        "returns length"
        return len(self.items)
# 1
mystring = "yesterday"

toberev = Stack()
for i in mystring:
    toberev.push(i)

reverse = ""
for i in range(toberev.size()):
               reverse += toberev.pop()

print(reverse)

# 2
numlist = [0,1,2,3,4,5]
rnumlist = Stack()
for i in numlist:
    rnumlist.push(i)

revnumlist=[]
for i in range(rnumlist.size()):
               revnumlist.append(rnumlist.pop())

print(revnumlist)
