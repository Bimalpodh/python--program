# class Node:
#   def __init__(self,data):
#     self.data=data
#     self.next=None


# def MergLinkedList(N,M):
#   temp=N
#   temp1=M
  
#   while temp or temp1:
#     if temp1.data<=temp.data:
#       temp1.next.data,temp1.data=temp1.data,temp.next.data
#     temp=temp.next
#     temp1=temp1.next
    
# def merg(N,M):
#   temp=N
#   prev=M.next
#   while temp:
#     if temp is None:
#       temp=prev
    
    

# class LinkedList:
#   def __init__(self):
#     self.head=None
    
#   def addNode(self,data):
#     new_Node=Node(data)
#     new_Node.next=self.head
#     self.head=new_Node
  
#   def printNode(self):
#     temp=self.head
#     while temp:
#       print(temp.data,end="->")
#       temp=temp.next
#     print()
      
#   def reverseNode(self):
#     temp=self.head
#     prev=None
#     while temp:
#       nextNode=temp.next
#       temp.next=prev
#       prev=temp
#       temp=nextNode
#     self.head=prev      
  

# N=LinkedList()
# N.addNode(1)
# N.addNode(2)
# N.addNode(4)
# N.printNode()
# # N.reverseNode()

# M=LinkedList()
# M.addNode(1)
# M.addNode(3)
# M.addNode(4)
# M.printNode()



# MergLinkedList(N,M)
# print("merge Linked List")
# print(merg(N,M))




# Here the chat gpt code

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, data):
        new_Node = Node(data)
        new_Node.next = self.head
        self.head = new_Node

    def printNode(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def reverseNode(self):
        temp = self.head
        prev = None
        while temp:
            nextNode = temp.next
            temp.next = prev
            prev = temp
            temp = nextNode
        self.head = prev


def mergeLinkedLists(L1, L2):
    dummy = Node(0)  # A dummy node to start the merged list
    tail = dummy

    temp1 = L1.head
    temp2 = L2.head

    # Merge while both lists have nodes
    while temp1 and temp2:
        if temp1.data <= temp2.data:
            tail.next = temp1
            temp1 = temp1.next
        else:
            tail.next = temp2
            temp2 = temp2.next
        tail = tail.next

    # Append remaining nodes of either list
    if temp1:
        tail.next = temp1
    if temp2:
        tail.next = temp2

    # Return the merged linked list starting from dummy.next
    mergedList = LinkedList()
    mergedList.head = dummy.next
    return mergedList


# Test the implementation
L1 = LinkedList()
L1.addNode(4)
L1.addNode(2)
L1.addNode(1)
print("L1:")
L1.printNode()

L2 = LinkedList()
L2.addNode(4)
L2.addNode(3)
L2.addNode(1)
print("L2:")
L2.printNode()

mergedList = mergeLinkedLists(L1, L2)
print("Merged Linked List:")
mergedList.printNode()
