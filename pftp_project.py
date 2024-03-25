import random
number =random.randint(0,100)
guess = None
score = 100

def lower(guess):
    print("This is lower than the actual number. Try Again! ")
    global score
    score -= 5
    
def greater(guess):
    print("This is greater than the actual number. Try Again! ")
    global score
    score -= 5

def multiple(guess):
	if (number%guess == 0):
		global score
		score -= 5
		print ("The actual number is the multiple of your guess. Try Again! ")		

print ('===============NUMBER GUESSING GAME================')
while guess!= number and score!=0 :
	guess = int(input("Input any number between 0 and 100: "))

	if guess<number:
		lower(guess)
		multiple(guess)
       
	elif guess>number:
		greater(guess)
		multiple(guess)
	else:
		print("This is the correct number")
		print (f'Your Total Score is:{score}')

	if score == 0:
		print ('YOU LOSS!! YOUR SCORE IS 0')
		break
