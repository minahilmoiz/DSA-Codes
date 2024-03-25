class Node:   # Creating a Node
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(): 
    def __init__(self):     # startig linked list
        self.head = None

    def print_linked_list(self):    # Traversing a linked_list 
        cur_node = self.head
        while cur_node != None:
            print (f'{cur_node.data} --->', end=' ')
            cur_node = cur_node.next

    def insert_begin(self, data):
        new_node = Node(data) #     make a node to enter in list 
        new_node.next = self.head #     connect this node to the head of the list 
        self.head = new_node 
        
    def insert_end(self, data):
        new_node = Node(data) #  Make a new Node
        if self.head == None: #  if linked list is empty even from starting
            self.head = new_node #  set head node to the defined new node
            return
        curr_node = self.head   #   set current node to the last node of the list
        while curr_node.next != None: # until the nodes of list are not empty
            curr_node = curr_node.next #     set next space after the last space of the node
        curr_node.next = new_node #     put the value of new node to the space set last time 
    
    def delete(self, key):
        cur_node = self.head
        if (cur_node != None) and (cur_node.data == key):
            cur_node.next = self.head
            cur_node = None
            return 
        
        prev_node = None
        while (cur_node != None) and (cur_node.data != key ):
            prev_node = cur_node
            cur_node = cur_node.next 
        if cur_node == None:
            return 
        prev_node.next = cur_node.next 
        cur_node = None

    def search(self, key):
        cur_node= self.head
        while cur_node!=None:
            if cur_node.data == key:
                return True
            cur_node = cur_node.next
        return False

    def sort (self):
        cur_node = self.head
        if cur_node == None:
            return
        while cur_node !=None:
            index = cur_node.next
            while index != None:
                if cur_node.data > index.data:
                    cur_node.data , index.data = index.data , cur_node.data 
                index= index.next
            
            cur_node = cur_node.next 

linked_list = LinkedList()
linked_list.insert_end(230)
linked_list.insert_end(404)
linked_list.insert_begin(101)
linked_list.insert_end(670)
linked_list.insert_begin(301)
linked_list.print_linked_list()
print ()
print ('After deleting element')
linked_list.delete(404)
linked_list.print_linked_list()
print ()
print ('searching 998...')
print (linked_list.search (998))
print ('sorting...')
linked_list.sort()
linked_list.print_linked_list()

