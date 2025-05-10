# how to use fast and slow pointers


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
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

    # finding the middle element
    def findmiddle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def display(self):
        current = self.head
        while current:
            print(current.data, " -> ", end=" ")
            current = current.next
        print()


linked_list = List()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)
linked_list.insert(6)
linked_list.display()
print(linked_list.findmiddle().data)  # middle element
