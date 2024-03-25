handle = open ('pftp2.txt' ,'r')

counts = {}
for line in handle:
    words =  line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
    
print ('Counts: ',counts)    

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword =word
        bigcount = count

print ('biggest Word is "',bigword,'"It occured', bigcount, 'times')