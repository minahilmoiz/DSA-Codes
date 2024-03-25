class Node:
    def __init__ (self, data):
        self.data = data 
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self):
        if self.is_empty():
            return None
        print (self.head.data)

    def display(self):
        if self.is_empty():
            return None
        cur_node = self.head
        while cur_node!= None:
            print (f'{cur_node.data} --->', end=' ')
            cur_node = cur_node.next

m_stack = Stack()
m_stack.push(1)
m_stack.push(2)
m_stack.push(3)
m_stack.display()
print()
m_stack.pop()
m_stack.display()
print ()
m_stack.peek()