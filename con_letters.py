# Program to count total number of words in a file.
file = open('pftp2.txt','r')
arr = []
for line in file:
    line = line.rstrip()
    words = line.split()
    for word in words:
        arr.append(word)


print (arr)
count = 0
for i in range(len(arr)):
    count += 1

print ('Total number of letters occuring in the text file: ', count)