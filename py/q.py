# how to implement a queue using a linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.display()
print(queue.dequeue())  # 1
print(queue.dequeue())  # 2
queue.display()


# The above code snippet is used to implement a queue using a linked list.
# What is a quque?
# A queue is a linear data structure that follows the First In First Out (FIFO) principle.
# The elements are inserted at the rear end and deleted from the front end.
# The operations on a queue are:
# Enqueue: Insert an element at the rear end of the queue.
# Dequeue: Delete an element from the front end of the queue.
# Peek: Get the element at the front end of the queue without deleting it.
# IsEmpty: Check if the queue is empty.
# The above code snippet defines a class Node to represent a node in the linked list.
