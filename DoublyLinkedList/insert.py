class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, index, data):
        node=Node(data)
        current=self.head
        while current:
            if current.data == index:
                break
            current = current.next
        if current == None:
            if self.head == None:
                self.head = node
                self.tail = self.head
            else:
                self.tail.next = node
                node.previous = self.tail
                self.tail = node
            return
        elif self.head.data == index:
            node.next = self.head
            self.head.previous = node
            self.head = node
            return
        node.next = current
        node.previous = current.previous
        current.previous = node
        node.previous.next = node
