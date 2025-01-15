# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

class Node:
  def __init__(self,val=0):
    self.val=val
    self.next=None
class LinkedList:
  def __init__(self):
    self.head=None
    self.head1=None
    self.head3=None
  def addNode(self,val):
    newnode=Node(val)
    newnode.next=self.head
    self.head=newnode
  def printLi(self):
    temp = self.head
    while temp:
        print(temp.val, end="->")
        temp = temp.next
    print("None")
  def intform(self):
    temp=self.head
    x=0
    while temp:
      x=x*10+temp.val
      temp=temp.next
    return x
  def reversed(self):
    prev=None
    temp=self.head
    while temp:
      nextNode=temp.next
      temp.next=prev
      prev=temp
      temp=nextNode
    self.head=prev

      
ob1=LinkedList()
ob1.addNode(3)
ob1.addNode(4)
ob1.addNode(2)
ob1.printLi()
ob2=LinkedList()
ob2.addNode(4)
ob2.addNode(6)
ob2.addNode(5)
ob2.printLi()
ob3=LinkedList()
# ob3.add2Sum()
ob1.reversed()
ob2.reversed()
ob1.printLi()
ob2.printLi()
ob1.intform()
ob2.intform()
x=ob1.intform()+ob2.intform()
print(x)



