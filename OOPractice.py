class addition:
    answer=0

    def __init__(self,f,s):
        self.first = f
        self.second = s

    def calculates(self):
        self.answer = int(self.first) + int(self.second)

    def display(self):
        print (f'Answer = {self.answer}')

a = input('First Number=  ')
b = input('Second Number=  ')
obj = addition (a,b)
obj.calculates()
obj.display()

#===========================================================

class student:

	def __init__(self):
		self.name = "Minahil"
		self.age = '20'

	def show (self):
		print (f"I'm {self.name}, I'm {self.age} years old.")

data = student()
data.show()

#===========================================================

class employee:

	def __init__(self,name,salary):
		self.name = name 
		self.salary = salary

	def show(self):
		print (f"Employee {self.name}'s salary is {self.salary}")

e1 = employee('Henna', 20000)
e2 = employee('Emma', 30000)
e1.show()
e2.show()

#==========================================================

'''
Make a class called Restaurant. The __init__() method for Restaurant should store two 
attributes: a restaurant_name and a cuisine_type. Make a method 
called describe_restaurant() that prints these two pieces of information, and a method 
called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then 
call both methods.
'''
class Restraunt:

    def __init__(self, res_name, cuisine_type):
        self.res_name = res_name
        self.cuisine_type = cuisine_type

    def describe_restraunt(self):
        print (self.res_name,'offers best',self.cuisine_type)

    def open_restraunt(self):
        print ('THE RSTRAUNT IS OPEN')

restraunt = Restraunt('ABC','pizza')
print (restraunt.res_name)
print (restraunt.cuisine_type)
restraunt.describe_restraunt()
restraunt.open_restraunt()

#==============================================================

