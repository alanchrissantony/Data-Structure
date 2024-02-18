class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def remove(self, data):
        current=self.head
        if self.head.data == data:
            self.head = self.head.next
            return
        while current.next:
            if current.next.data == data:
                current.next=current.next.next
                return
            current=current.next