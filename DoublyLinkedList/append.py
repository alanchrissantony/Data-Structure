class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node=Node(data)
        if self.head == None:
            self.head = node
            self.tail = self.head
            return
        current=self.head
        while current.next:
            current = current.next
        current.next = node
        node.previous = current
        self.tail = current.next
        self.tail.previous = current
