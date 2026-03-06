#adding the node at the beginning of the list
class Node:
    
    def __init__(self,data):
        
        self.data=data
        self.next=None
    
class Linkedlist:
    def __init__(self):
        self.head=None
    def add_first(self,data):
        new_node=Node(data)#creating a node
        new_node.next=self.head
        self.head=new_node
    def add_last(self,data):
        new_node=Node(data)#creating a #adding the node at the ending of the list
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node
    def display(self):#displaying
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next
    def deleted_first(self):#deleting at first
        if self.head is None:
            print("linked list is empty")
        else:
            self.head=self.head.next
    def delete_last(self):#deleting at last
        if self.head is None:
            print("Empty")
            return
        if self.head.next is None:
            self.head=None
            return
        current=self.head
        while current.next.next is not None:
            current=current.next
        current.next=None
    def size(self):#size
        count=0
        current=self.head
        while current is not None:
            count+=1
            current=current.next
        return count   
    def position(self,data):#deleting by value 
        
        if self.head is None:# list is checking empty 
            print("list is empty")
            return
        if data==self.head.data:#list containg only one node
            self.head=self.head.next
            return
        current=self.head
        while current.next is not None:#one less than the node T
            if data==current.next.data:#finding the actual node
                break
            current=current.next
        if current.next is None:
            print("out of bound")
        else:
            current.next=current.next.next
obj=Linkedlist()
obj.add_first(200)
obj.add_first(60)
obj.add_first(33)
obj.add_first(20)
obj.add_last(188)
obj.delete_last()
obj.deleted_first()
obj.display()
print(obj.size())
obj.position(60)
obj.display()
print(obj.size())

