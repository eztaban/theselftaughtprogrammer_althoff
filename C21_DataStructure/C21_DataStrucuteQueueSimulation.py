# Ticket Queue
import time
import random

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

    def simulate_line(self, till_show,max_time):
        """
        :param till_show: seconds til show start
        :param max_time: maximum amount of time to buy ticket
        """
        pq = Queue() # empty queue
        tix_sold = [] # empty list of sold tickets
        for i in range(100):
            pq.enqueue("Person"+str(i)) # customers
        t_end = time.time() + till_show
        now = time.time() # current time since epoch
        while now < t_end and not pq.is_empty():
            now = time.time() # updates time
            r = random.randint(0, max_time)
            time.sleep(r) # pauses time for r time
            person = pq.dequeue()
            print(person)
            tix_sold.append(person)
        return tix_sold

queue = Queue()
sold = queue.simulate_line(5, 1)
print(sold)
