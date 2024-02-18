class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def reverse(self):
        current=self.head
        previous=None
        while current:
            nxt=current.next
            current.next=previous
            previous=current
            current=nxt
        self.head=previous