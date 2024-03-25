array=[]
for i in range(10):
    char = str(input(f'{i+1} Character in a string: ').lower())
    array.append(char)

vowels=['a', 'e', 'i', 'o', 'u']
vow =[]
for character in array:
    character.lower()
    
    if character in vowels:
        vow.append(character)
      
print (vow)   
count = 0
for elem in vow:
    count += 1

print (count)