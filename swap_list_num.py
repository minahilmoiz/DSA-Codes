# sorting the list and swapping first number with the last number in the list.

list = [200, 400, 900, 100, 300, 600, 500]
list.sort()
print (list)

first = list[0]
last = list[-1]
list[0] = last
list[-1] = first

print ('After swapping numbers: ')
print (list)