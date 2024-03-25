# Write a python program to check of the given string is palindrome or not using stack.
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def is_palindrome(s):
    stack = Stack()
    for c in s:
        stack.push(c)

    rev_s = ''
    while not stack.is_empty():
        rev_s += stack.pop()

    if s == rev_s:
        print('The given string is palindrome ')
    else:
        print ('The given string is not palindrome')
    
is_palindrome('OPPO')  
is_palindrome('hello')    

# Write a python program to check of the given string is palindrome or not using deque.

from collections import deque

def is_palindrome(s):
    # Create an empty deque
    d = deque()

    # Add each character of the string to the deque
    for char in s:
        d.append(char)

    # Keep removing the first and last characters from the deque
    # and comparing them until the deque is empty or we find a mismatch
    while len(d) > 1:
        first_char = d.popleft()
        last_char = d.pop()
        if first_char != last_char:
            return False

    # If we haven't found a mismatch, the string is a palindrome
    return True

# Test the function
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
print(is_palindrome(""))  # Output: True

#   OBEJECT 3:

import random
import time
# Queue implementation using Python List
class QueueUsingList:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0

# Queue implementation using Python Deque
class QueueUsingDeque:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):  
        if not self.is_empty():
            return self.queue.popleft()
    
    def is_empty(self):
        return len(self.queue) == 0
    
# Function to measure time taken by Queue implementation with List
def measure_time_queue_list(M, N):
    start_time = time.time()
    for _ in range(M):
        queue = QueueUsingList()
        for _ in range(N):
            queue.enqueue(random.randint(1, 1000))
        for _ in range(N):
            queue.dequeue()
    end_time = time.time()
    return end_time - start_time


# Function to measure time taken by Queue implementation with Deque
def measure_time_queue_deque(M, N):
    start_time = time.time()
    for _ in range(M):
        queue = QueueUsingDeque()
        for _ in range(N):
            queue.enqueue(random.randint(1, 1000))
        for _ in range(N):
            queue.dequeue()
    end_time = time.time()
    return end_time - start_time

# Example usage:
M = 5 
N = 10000
time_taken_list = measure_time_queue_list(M, N)
time_taken_deque = measure_time_queue_deque(M, N)
print(f"Time taken with Queue using List: {time_taken_list} seconds")
print(f"Time taken with Queue using Deque: {time_taken_deque} seconds")

