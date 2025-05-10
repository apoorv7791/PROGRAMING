# uses of classes and objects


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            print("Key not found")
            return
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next


# Example usage
l1 = LinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.append(50)
l1.display()
l1.delete(20)
l1.display()
