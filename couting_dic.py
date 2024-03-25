# Counting words in the statement you enter.

count={}
line = input('Enter a line to count word: ')
words = line.split()

print ('words', words)

print ('counting.....')
for word in words:
    count[word] = count.get(word,0) +1

print('Counts', count)