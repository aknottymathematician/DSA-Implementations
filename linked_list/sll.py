class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        itr = self.head
        for i in range(0, index):
            itr = itr.next
        return itr.data
            
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        itr = self.head
        new_node = Node(val)

        if index <= 0:
            new_node.next = itr
            self.head = new_node
        else:
            for i in range(index-1):
                itr = itr.next
                
            new_node.next = itr.next
            itr.next = new_node
        self.size +=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index <0 or index>=self.size:
            return -1
        
        itr = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(0, index -1):
                itr = itr.next
            itr.next = itr.next.next
        self.size -=1
        
        
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)