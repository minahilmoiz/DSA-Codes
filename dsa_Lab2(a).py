def sum (array):
    s=0
    for i in array:
        s = s + i
    print ("The sum of all the elements of array: ", s) 

array= []
N = int(input("Enter the lenght of array you want: "))
for item in range(N):
    num = int(input("Enter the number for the array: "))
    array.append(num) 
sum (array)

#==============================================================

def Sum(N):
    i=0
    A=0
    while i<N:
        A += i
        i+=1 
    return A

N = int(input("Enter the limit: "))
print (f'The sum of first {N} numbers  is : {Sum(N)}')  