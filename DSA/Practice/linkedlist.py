class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Set the new node's next to the current head
        self.head = new_node        # Move the head to point to the new node
    
    def printData(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("none")
    def reversed(self):
        prev=None
        temp=self.head
        while temp:
            nextNode=temp.next
            temp.next=prev
            prev=temp
            temp=nextNode
        self.head=prev
    def findMid(self):
        temp=self.head
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        if slow:
            print(slow.data)
        else:
            print(slow.next.data)
        
            

n = linkedList()
n.add(7)
n.add(8)
n.add(18)
n.add(12)
n.add(12)
n.add(67)
n.printData()
print("reversed of the linkesd list")
n.reversed()
n.printData()
n.findMid()


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
    
# class LinkedList:
#     def __init__(self):
#         self.head=None
        
#     nod1=Node(10)
#     nod2=Node(20)
#     nod1.next=nod2
#     def addNode(self,data):
#         newNode=Node(data)
#         newNode.next=self.head
#         self.head=newNode
        
        
        
        
        
# l=LinkedList()
# print(l.nod1.data)
# print(l.nod2.data)