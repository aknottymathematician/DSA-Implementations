class Node:
    def __init__(self):
        self.val = None
        self.next = None

class linkedList:
    def __init__(self):
        self.head=None
    
    def insertStart(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def reverseList(self, head):
        itr = head
        dummy = None
        while itr:
            self.insertStart(itr)
        return head