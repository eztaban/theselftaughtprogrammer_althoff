class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        "returns True if Queue is empty"
        return self.items == []

    def enqueue(self, item):
        "inserts item in items at pos 0"
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

a_queue = Queue()
print(a_queue.is_empty())

for i in range(5):
    a_queue.enqueue(i)
print(a_queue.size())

for i in range(5):
    print(a_queue.dequeue())
print("\n", a_queue.size())
