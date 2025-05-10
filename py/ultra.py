# implement a quque using an array


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def display(self):
        print(self.queue)


Q = Queue()  # create an instance of the Queue class
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
Q.display()
print(Q.dequeue())
print(Q.dequeue())
Q.display()
