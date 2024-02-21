class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove(self, data):
        current = self.head
        if current and current.data == data:
            self.head = self.head.next
            self.head.previous = None
            return
        elif self.tail.data == data:
            self.tail = self.tail.previous
            self.tail.next = None
            return
        while current:
            if current.data == data:
                break
            current = current.next
        current.previous.next = current.next
        current.next.previous = current.previous     