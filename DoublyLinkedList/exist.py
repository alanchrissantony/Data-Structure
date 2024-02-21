class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def exist(self, data):
        current = self.head
        while current:
            if current.data == data:
                print(True)
                return
            current = current.next
        print(False)
