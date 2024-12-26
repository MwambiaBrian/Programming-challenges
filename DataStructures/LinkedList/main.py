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
    

my_linkedlist =  LinkedList()
my_linkedlist.append(1)
my_linkedlist.append(2)
my_linkedlist.append(3)
my_linkedlist.append(4)
my_linkedlist.display()