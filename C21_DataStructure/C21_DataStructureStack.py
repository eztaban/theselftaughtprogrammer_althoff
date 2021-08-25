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

stack = Stack()
stack.push(1)
item = stack.pop()
print(item)
print(stack.is_empty())

for i in range(0, 6):
    stack.push(i)

print(stack.peek())
print(stack.size())

"""
common interview problem.
reverse a string using a stack.
Add it to the stack, then remove it and it will come off in reverse
"""

string=Stack()
for c in "Hello":
    string.push(c)

reverse=""
for i in range(string.size()):
    reverse += string.pop()

print(reverse)
