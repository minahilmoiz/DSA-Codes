# Design the algorithm to find out the largest element of an integer array of size 10
# // Input: int A[N], array of N=10 integers
# // Output:  Max value of array 

# Algo MaxArray(A, 10)
#     Max ← A(1)
#     For i ← 2 to 10
#         If A(i) > Max
#             Max ← A(i)
#         EndIf
#     EndFor
#     Output Max
# EndAlgo MaxArray

def max_array(A):
    max = A[0]
    for i in range(10):
        if A[i] > max:
            max = A[i]
    print ('Max Value of an array', max)

A = [1,4,6,2,3,8,11,0,7,9]
max_array(A)

#======================================================

# Design the algorithm to find out the largest element of an integer array of size N
# // Input: int A[N], array of N integers
# // Output:  Max value of array 

# Algo MaxArray (A, N)
#     Max ← A(1)
#     For i ← 2 to N
#         If A(i) > Max
#             Max ← A(i)
#         EndIf
#     EndFor
#     Output Max
# EndAlgo MaxArray

def max_arr(A):
    max = A[0]
    for i in range(N):
        if A[i] > max:
            max = A[i]
    print ('Max Value of an array is ', max)

N = int(input('Enter the lenght of an array: '))
B = []
for i in range(N):
    num = int(input("Enter integers: "))
    B.append(num)

print (B)
max_arr(B)


#=============================================================