# COUNTING TOP 10 COMMON WORDS IN A TEXT FILE

handle = open ('./text.txt','r')

dict={}
for line in handle:
    words = line.split()
    for word in words:
        dict[word] = dict.get(word,0) +1

list=[]
for key, value in dict.items():
    tup = (value, key)
    list.append(tup)

list = sorted(list, reverse=True)
# the reverse in the above line of code sort the list to the descending order

for value, key in list[:10]:
    print (key, value)