# implementn a linked list in python


class Node:
    def __init__(self, data):  # Constructor method
        self.data = data  # Assign the data to the node
        self.next = None  # Initialize the next pointer to None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def reverse(self):
        prev = None  # Initialize the previous pointer to None
        current = self.head
        while current:  # Iterate over the linked list
            next = current.next  # Store the next pointer
            current.next = prev  # Reverse the link
            prev = current  # Move the pointers one position ahead
            current = next  # Move the pointers one position ahead
        self.head = prev  # Update the head pointer to the new head

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


L1 = LinkedList()
L1.insert(10)
L1.insert(20)
L1.insert(30)
L1.insert(40)
L1.insert(50)
L1.display()
L1.reverse()
L1.display()
print(L1.search(30))
print(L1.search(60))
