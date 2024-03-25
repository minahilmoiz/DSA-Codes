def f(n):
    if (n==0):
        return 0
    else:
        count = n
        print (count)
        return f(n-1)

print (f(5))

#FACTORIAL FUNCTION:

def fac(n):
    if n == 1:
        return 1
    else:
        return (n*int(fac(n-1)))
a = 5
b= fac(a)
print (f'factorial of {a} is: ',b)

#FIBONACCI SERIES:

def fib(n):
    if (n==0):
        return(0)
    elif  (n==1):
        return (1)
    else:
        return (fib(n-1)+fib(n-2))

a=6
fib(a)
print("Fibonacci series: ")
for i in range(a):
       print(fib(i))

# REVERSE AN ARRAY BY SWAPPING AND RECURSION

def reverse_array(A, start, end):
    if end < start:
        return (A)
    else:
        A[start], A[end] = A[end], A[start]
        return (reverse_array(A, start+1, end-1))
    

A = [1,2,3,4,5,6,7,8,9]
i = 0
j= len(A)-1
reverse_array(A,i, j)
print (A)

#SUM:

def add(n):
    if n == 1:
        return 1
    else:
        return (n + add(n-1))

print ('Sum: ',add(4))

#MAX ELEMENT OF ARRAY:

def max_array(A,n):
    if n == 1:
        return A[0]
    else:
        return max(A[n-1],max_array(A,n-1))

A = [1,4,6,2,3,8,11,0,7,9]
n = len(A)
print (max_array(A,n))

# Towers Of Hanoi

def towers_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    towers_of_hanoi(n-1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    towers_of_hanoi(n-1, auxiliary, destination, source)

# Example usage
towers_of_hanoi(3, 'A', 'C', 'B')
