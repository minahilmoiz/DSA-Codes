'''
A Program setting inputs as Player Name, Total Runs, Total match Played, and finding the average run scored using input.
Note :
(average <= 100 & => 80)-> grade A player -> salary above 1 LACK
(average < 80 & => 50)-> grade B player -> salary below 1 LACK & above 50K
(average <50)-> grade C player -> salary below 50K
'''
def ave(total_runs, matches):
    average = (total_runs)/(matches)
    print (average)
    
    if (average >= 80 ) and (average <= 100):
        print ('Grade A player')
        print ('Slary above 1 lack')
    
    elif (average < 80) and (average >= 50):
        print ('Grade B player')
        print ('Slary below 1 lack or above 50k')

    else: 
        print ('Grade C player ')
        print ("salary below 50k")

while True:
    player = input ("Enter player's name: ")
    total_runs = int(input (f"Enter Total runs {player} made: "))
    matches = int(input(f"Enter total matches {player} played: "))
    ave(total_runs, matches)
