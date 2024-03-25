li = [ [3,4,5,2], [7,8,5,1], [5,2,5,7] ]
row = len(li)
col = len(li[0])
for i in range (row):
    for j in range(col):
        print ('%8.2f'%li[i][j],end = '')
    print()

#===================================

def matrixtranspose(a):
    t = []
    for i in range(len(a[0])):
        r = []
        for j in range(len(a)):
            b = a[j][i]
            r.append(b)
        t.append(r)
    return t
a = [[2, 3, 6, 2], [3, 5, 3, 2], [3 , 6, 4, 2]]
at = matrixtranspose(a)
print(at)

#===========================================

class Matrix:
    def __init__(self,m):
        self.m = m
    def display(self,m):
        print()
        for i in m:
            for j in i:
                print('%10.3f'%j,end=' ')
            print()
        print()
        def __add__(self,other):
            if len(self.m) == len(other.m) and len(self.m[0]) == len(other.m[0]):
                addmat = []
                for i in range(len(self.m)):
                    r = []
                    for j in range(len(self.m[0])):
                        s = self.m[i][j] + other.m[i][j]
                        r.append(s)
                    addmat.append(r)
                return self.display(addmat)
            else:
                return print('Addition is Not Possible')
a = [[1,2,5],[4,5,4]]
b = [[5,6,2],[6,8,1]]
m1 = Matrix(a)
m2 = Matrix(b)

