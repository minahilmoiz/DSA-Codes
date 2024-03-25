#*************************************HASHTABLE****************************************

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashTable = [None] * self.capacity

    def checkPrime(self, n):
        if n == 1 or n == 0:
            return False

        for i in range(2, n//2):
            if n % i == 0:
                return False

        return True

    def getPrime(self, n):
        if n % 2 == 0:
            n = n + 1

        while not self.checkPrime(n):
            n += 2

        return n

    def hashFunction(self, key):
        return key % self.capacity

    def insertData(self,key, data):
        index = self.hashFunction(key)
        self.hashTable[index] = [key, data]


    def removeData(self,key):
        index = self.hashFunction(key)
        self.hashTable[index] = None

    def printHashTable(self):
        for i in range(self.capacity):
            print (self.hashTable[i])
            
            
hashTable = HashTable(10)
n = 'y'
while (n=='y'):
    a = int(input('Enter key: '))
    b =  str(input('Enter value: '))
    hashTable.insertData(a, b)
    n = str(input ('\n Another key:value? y/n: '))
    print ()

hashTable.printHashTable()
print ('\n')

m = str(input('Want to remove value? (y/n) :'))
while (m=='y'):
    c = int(input("Enter key of the value to be removed: "))
    hashTable.removeData(c)
    m = str(input('Want to remove another value? (y/n) :'))
    print ( )
    
hashTable.printHashTable()

# #***********************************LINEAR PROBING***********************************
# class HashTable:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.hashTable = [None] * self.capacity

#     def checkPrime(self, n):
#         if n == 1 or n == 0:
#             return False

#         for i in range(2, n//2):
#             if n % i == 0:
#                 return False

#         return True

#     def getPrime(self, n):
#         if n % 2 == 0:
#             n = n + 1

#         while not self.checkPrime(n):
#             n += 2

#         return n

#     def hashFunction(self, key):
#         return key % self.capacity

#     def insertData(self, key, data):
#         index = self.hashFunction(key)
#         if not self.hashTable[index]:
#             self.hashTable[index] = [key, data]
#         else:
#             # colli12sion occurred, probe linearly until empty slot is found
#             i = 1
#             while True:
#                 new_index = (index + i) % len(self.hashTable)
#                 if not self.hashTable[new_index] :
#                     self.hashTable[new_index] = [key, data]
#                     break
#                 i += 1

    
#     def removeData(self, key):
#         index = self.hashFunction(key)
#         if self.hashTable[index][0] == key:
#             self.hashTable[index] = None
#         else:
#             # key not found at computed index, probe linearly until found
#             i = 1
#             while True:
#                 new_index = (index + i) % len(self.hashTable)
#                 if self.hashTable[new_index][0] == key:
#                     self.hashTable[new_index] = None
#                     break
#                 i += 1

#     def printHashTable(self):
#         for i in range(self.capacity):
#             print (self.hashTable[i])
            
            
# hashTable = HashTable(10)
# n = 'y'
# while (n=='y'):
#     a = int(input('Enter key: '))
#     b =  str(input('Enter value: '))
#     hashTable.insertData(a, b)
#     n = str(input ('\n Another key:value? y/n: '))
#     print ()

# hashTable.printHashTable()
# print ('\n')

# m = str(input('Want to remove value? (y/n) :'))
# while (m=='y'):
#     c = int(input("Enter key of the value to be removed: "))
#     hashTable.removeData(c)
#     m = str(input('Want to remove another value? (y/n) :'))
#     print ( )
    
# hashTable.printHashTable()

#***********************************QUADRATIC PROBING***********************************
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashTable = [None] * self.capacity

    def checkPrime(self, n):
        if n == 1 or n == 0:
            return False

        for i in range(2, n//2):
            if n % i == 0:
                return False

        return True

    def getPrime(self, n):
        if n % 2 == 0:
            n = n + 1

        while not self.checkPrime(n):
            n += 2

        return n

    def hashFunction(self, key):
        return key % self.capacity

    def insertData(self, key, data):
        index = self.hashFunction(key)
        if not self.hashTable[index]:
            self.hashTable[index] = [key, data]
        else:
            # colli1sion occurred, probe quadratically until empty slot is found
            i = 1
            while True:
                new_index = (index + i*i) % len(self.hashTable)
                if not self.hashTable[new_index] :
                    self.hashTable[new_index] = [key, data]
                    break
                i += 1

    
    def removeData(self, key):
        index = self.hashFunction(key)
        if self.hashTable[index][0] == key:
            self.hashTable[index] = None
        else:
            # key not found at computed index, probe quadratically until found
            i = 1
            while True:
                new_index = (index + i*i) % len(self.hashTable)
                if self.hashTable[new_index][0] == key:
                    self.hashTable[new_index] = None
                    break
                i += 1

    def printHashTable(self):
        for i in range(self.capacity):
            print (self.hashTable[i])
            
            
hashTable = HashTable(10)
n = 'y'
while (n=='y'):
    a = int(input('Enter key: '))
    b =  str(input('Enter value: '))
    hashTable.insertData(a, b)
    n = str(input ('\n Another key:value? y/n: '))
    print ()

hashTable.printHashTable()
print ('\n')

m = str(input('Want to remove value? (y/n) :'))
while (m=='y'):
    c = int(input("Enter key of the value to be removed: "))
    hashTable.removeData(c)
    m = str(input('Want to remove another value? (y/n) :'))
    print ( )
    
hashTable.printHashTable()

# # ********************************** BY SEPARATE CHAINING***********************************

# class Node:
#     def __init__(self, key, data):
#         self.key = key
#         self.data = data
#         self.next = None

# class HashTable:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.hashTable = [None] * self.capacity

#     def checkPrime(self, n):
#         if n == 1 or n == 0:
#             return False

#         for i in range(2, n//2):
#             if n % i == 0:
#                 return False

#         return True

#     def getPrime(self, n):
#         if n % 2 == 0:
#             n = n + 1

#         while not self.checkPrime(n):
#             n += 2

#         return n

#     def hashFunction(self, key):
#         return key % self.capacity

#     def insertData(self, key, data):
#         index = self.hashFunction(key)  # compute the index for the key

#         if not self.hashTable[index]:  # if the index is empty
#             self.hashTable[index] = Node(key, data)  # create a new node with the key-value pair and store it at the index
#         else:
#             curr = self.hashTable[index]  # start at the head of the linked list
#             while curr.next:  # iterate through the linked list until the last node
#                 curr = curr.next
#             curr.next = Node(key, data)  # create a new node with the key-value pair and append it to the linked list

#     def removeData(self, key):
#         index = self.hashFunction(key)

#         if not self.hashTable[index]:
#             return

#         if self.hashTable[index].key == key:
#             self.hashTable[index] = self.hashTable[index].next
#             return

#         curr = self.hashTable[index]
#         while curr.next:
#             if curr.next.key == key:
#                 curr.next = curr.next.next
#                 return
#             curr = curr.next

#     def printHashTable(self):
#         for i in range(self.capacity):
#             print(f'Index {i}: ', end =' ')
#             curr = self.hashTable[i]
#             while curr:
#                 print(f'({curr.key}, {curr.data}) -> ', end='')
#                 curr = curr.next
#             print('None')

# hashTable = HashTable(10)
# n = 'y'
# while (n=='y'):
#     a = int(input('Enter key: '))
#     b =  str(input('Enter value: '))
#     hashTable.insertData(a, b)
#     n = str(input ('\n Another key:value? y/n: '))
#     print ()

# hashTable.printHashTable()
# print ('\n')

#  m = str(input('Want to remove value? (y/n) :'))
# while (m=='y'):
#     c = int(input("Enter key of the value to be removed: "))
#     hashTable.removeData(c)
#     m = str(input('Want to remove value? (y/n) :'))
#     print ( )
    
# hashTable.printHashTable()
