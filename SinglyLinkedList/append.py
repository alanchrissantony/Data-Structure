class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self, data):
        node=Node(data)
        if self.head==None:
            self.head=node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=node

    