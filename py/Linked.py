# implement a basic linked list in Python
# A Linked list is a linear data strucutre that consist of nodes which are pointing to the address of the next ni


class Node:
    def __init__(self):
        self.data = None
        self.next = None


# A node has a data field and a next field


class LinkedList:
    def __init__(self):
        self.head = None

    # A linked list has a head field

    def insert(self, data):
        new_node = Node()
        new_node.data = data
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # we are adding a new node to the end of the linked list

    def Reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def delete(self, data):
        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            return
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print()


l1 = LinkedList()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)
l1.insert(5)
l1.display()  # print in sequence 1, 2, 3, 4, 5


l1.delete(3)
l1.Reverse()
l1.display()  # print in sequence 5, 4, 3, 2, 1

# Explanation of the code
# The LinkedList class is defined with two attributes: head and tail. The head attribute is used to store the first node
# of the linked list, while the tail attribute is used to store the last node of the linked list.
# The insert method is used to add a new node to the end of the linked list. It takes one argument, data, which is the
# data to be stored in the new node. The method creates a new node, sets its data attribute to the value of the data
# argument, and sets its next attribute to None. If the head attribute is None, the new node becomes the head of the
# linked list. Otherwise, the new node is added to the end of the linked list by setting the next attribute of the
# current tail node to the new node.
# The delete method is used to remove a node from the linked list. It takes one argument, data, which is the data to
# be removed from the linked list. The method iterates through the linked list until it finds a node with the
# specified data. If the node is found, it is removed from the linked list by setting the next attribute of the
# previous node to the next attribute of the node to be removed. If the node is the head of the linked list, the head
# attribute is set to the next attribute of the node to be removed. If the node is the tail of the linked list, the
# tail attribute is set to the previous node.
# The display method is used to print the data of each node in the linked list. It iterates through the linked list
# and prints the data of each node.
