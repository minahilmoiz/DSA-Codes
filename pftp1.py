'''
Write a python program to input 5 subject marks and calculate total marks,
percentage and grade based on following criteria
i. percentage less than 50 (Grade C)
ii. percentage equal to 50 and less than 80 (Grade B)
iii. percentage equal to 80 and more than 80 (Grade A)
'''
def inputmarks():
    i=1
    global total
    total = 0
    while (i<=5):
        num = int(input(f'Enter the marks of subject {i}: '))
        total += num
        i+=1
    print ('Total Marks = ', total)

def calpercentage(total):
    global percentage
    percentage = (total/500)*100
    print ('Percentage of five subjects: ',percentage)

def grading():
    if (percentage >= 80) :
        print ('Grade A')
    elif (percentage == 50 or percentage < 80):
        print ('Grade B')
    else:
        print ('Grade C')


inputmarks()
calpercentage(total)
grading()