class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete(self, node):
        if self.head is None or node is None:
            return
        if self.head == node:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next

    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        print(nodes)


# Example usage:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.prepend(0)
dll.display()  # Output: [0, 1, 2]
dll.delete(dll.head.next)
dll.display()  # Output: [0, 2]
