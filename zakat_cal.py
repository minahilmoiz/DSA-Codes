def calculation ():
    print ('------Enter Savings of last one year-----')
    g = int(input ('Gold in gms: '))
    sl = int(input ('Silver in gms: '))
    bb = int(input('Bank Balance: '))
    hc = int (input('Hand Cash: '))
    p = int(input ('Property: '))
    gd_sl = int(input('Amount a/c to the current Rate of gold and silver: '))

    total = bb + hc + p + gd_sl
    
    if (g >= 87.5) or (sl >= 612.4):
        zakat = total * 0.025
    
    print (f'Total Asset = {total}')
    print (f'Zakat Amount = {zakat}')

calculation()

