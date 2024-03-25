#FIBONACCI SERIES:

n=int(input("size of series : "))

def fib(n):
    if (n==0) or (n==1):
        return(1)
    else:
        return (fib(n-1)+fib(n-2))

a=fib(n)
print (a)

#FACTORIAL FUNCTION:

def fac(n):
    if n == 1:
        return 1
    else:
        return (n*int(fac(n-1)))

b= fac(n)
print (b)

#Example:

def addi(r):
    if (r<=0):
        return 0
    else:
        return (r + addi(r-1))

c = addi(n)
print (c)

#EUCLIDEAN'S ALGORITHM:

def gcd(p,q):
    if (q==0):
        return p
    else:
        return (gcd(q,p%q))

ans = gcd(40,42)
print (ans)

#POWER FUNCTION:

def power(b,p):
    if p==0:
        return 1
    else:
        return b*power(b,p-1)

a = int(input('Enter Base: '))
b = int(input('Enter Power: '))
c = power(a,b)
print(f'The {a} raised to the power {b} is: {c}')
