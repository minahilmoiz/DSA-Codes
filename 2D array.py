# Write a program to define a 2D array and store students’ marks of different subjects. Calculate the average marks of students and average marks of Subjects.

m =[]
sub = [' ', 'Maths', 'Urdu', 'Eng', 'Average Marks']
m.append(sub)
for i in range(3):
    std =[]
    n =  str(input('Student roll.no. : '))
    std.append(f'std {n}')
    tot = 0
    for j in sub[1:4]:
        mark = int (input(f'marks of {j} :'))
        std.append(mark) 
        tot += mark
    
    ave=int(tot/3)
    std.append(ave)
    m.append(std)
    print ( )
print (m)

for row in range(len(m)):
    for col in range(len(m[0])):
        print (m[row][col], end = '     ')
    print()
