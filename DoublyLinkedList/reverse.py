class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def reverse(self):
        current=self.tail
        while current:
            print(current.data)
            current = current.previous
  