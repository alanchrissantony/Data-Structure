class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self, index, data):
        node=Node(data)
        if self.head==None:
            self.head=node
            return
        elif self.head.data == index:
            node.next=self.head
            self.head=node
            return
        current=self.head
        while current.next:
            if current.next.data == index:
                node.next=current.next
                current.next=node
                return
            current=current.next
        current.next=node