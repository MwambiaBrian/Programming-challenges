class Node:
    def __init__(self, data=None):
        self.data = data  # Store the data
        self.next=None   # Initialize the next pointer as None
        
class LinkedList:
    def __init__(self):
        self.head=None #Initialize the head of the linked list as None
        
    def append(self, data):
        new_node=Node(data)
        if self.head == None:
            self.head=new_node
            return
        current= self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def display(self):
        if self.head is None:
            print("The Linke List is empty")
            return
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end="->")
            cur_node = cur_node.next
        print("None")
    
    def length(self):
        if self.head is None:
            print(0)
            return
        cur_node = self.head
        total=0
        while cur_node:
            total+=1
            cur_node=cur_node.next
        print(total)
        return total
        
    def get(self,index):
        if index >= self.length():
            print("ERROR: 'Get' index out of range" )
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.data
            cur_idx +=1
        
        
    def delete(self,key):
        current= self.head
        if current and current.data == key:
            self.head = current.next
            current= None
            return
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        if current is None:
            print(f"Value {key} not found in the linked list.")
            return
        previous.next= current.next
        current = None
        
my_linkedlist =  LinkedList()
my_linkedlist.append(1)
my_linkedlist.append(2)
my_linkedlist.append(3)
my_linkedlist.append(4)
my_linkedlist.append(6)
my_linkedlist.get(3)
#my_linkedlist.delete(4)
my_linkedlist.display()
my_linkedlist.length()