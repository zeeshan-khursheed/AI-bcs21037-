class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


q = Queue()
print("Is queue empty?", q.is_empty()) 

q.enqueue("Kamran")
q.enqueue("Age : 23")
q.enqueue(2000)
q.enqueue("Bussines profession")

print("Is queue empty?", q.is_empty()) 
print("Size of queue is:", q.size())
print("Peek of queue is:", q.peek())
print("Queue is:", q)

print("Dequeued : ",q.dequeue())
print("Dequeued : ",q.dequeue())

print("Peek of queue is:", q.peek())
print("Queue is:", q)

print("===============================================================================")
