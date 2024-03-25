# 2.Write a function which accepts a 2D array of integers and its size as arguments and displays the elements of middle row and the elements of middle column and their sum
# [Assuming the 2D Array to be a square matrix with odd dimensions i.e. 3x3, 5x5, 7x7 etc...]
# Example, if the array contents is 3 5 4
# 7 6 9

# 2 1 8

# Output through the function should be : 
# Middle Row : 7 6 9
# Middle column : 5 6 1 
# Middle Row Sum : 22
# Middle Column Sum :12


def matrix(a,b):
    global mat
    mat = []
    for i in range(a):
        row= []
        for j in range(b):
            n = int(input('Number: '))
            row.append(n)
        mat.append(row)
   
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            print (mat[r][c], end = ' ')
        print()

def mid_row(mat):
    md = int(len(mat)/2)
    mr = mat[md]
    print ('middle row = ', end='')
    for r in mr:
        print (r, end= ' ')
    print ()
    count = 0 
    for sr in mr:
        count += sr
    print ('sum of middle row =', count)


def mid_col(mat):
    print ('middle column = ', end='')
    count = 0 
    for r in range(len(mat)):
        md = int(len(mat[r])/2)
        mc = mat[r][md]
        print (mc, end= ' ') 
        count += mc
    print ()
    print ('sum of middle column =', count)

matrix(3,3)
mid_row(mat)
mid_col(mat)
