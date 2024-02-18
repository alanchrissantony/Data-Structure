class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def exist(self, data):
        current=self.head
        while current:
            if current.data == data:
                return True
            current=current.next
        return False

