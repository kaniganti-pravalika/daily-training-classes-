class Node:
    def __init__(self,data):#creating node
        self.data=data
        self.next=None
node1=Node(10)#object creation
node2=Node(20)
node3=Node(30)
node4=Node(40)
#connecting every nodes
node1.next=node2
node2.next=node3
node3.next=node4
#printing 
current=node1
#print(node1.data,node1.next.data,node1.next.next.data,node1.next.next.next.data)
#if we have the only fixed  number of  iterations.
for i in range (4):
    print(current.data)
    current=current.next
#if we donot know the size of the list
current=node1
while current:
    print(current.data)
    current=current.next