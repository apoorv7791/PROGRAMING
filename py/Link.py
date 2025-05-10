# implementation of linked list in python

# create a node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# create a linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    # insert a new node
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, "->", end=" ")
            current = current.next
        print("null")

    # reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


# creating the objects
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)
linked_list.display()
linked_list.reverse()
linked_list.display()
