# Single Linked List with 3 Nodes using OOP

# Node class
class Node:
    def __init__(self, ele):
        self.prev = None
        self.data = ele
        self.next = None


# Create 3 nodes
f= Node(10)
s= Node(20)
t= Node(30)
f.prev=None
f.next=s
s.prev=t
s.next=t
t.prev=s
t.next=None
print("element forward")
ptr=f
while ptr.next!=None:
    print(ptr.data)
    ptr=ptr.next
print(ptr.data)
print("element backward")
while ptr!=None:
    print(ptr.data)
    ptr=ptr.prev