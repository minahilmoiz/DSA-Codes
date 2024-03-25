file = open ('pftp2.txt','r')
for line in file:
    line = line.rstrip()
    if not line.startswith('Email '): continue
    imp_line = line.split()
    print (imp_line)
    Email = imp_line[2]
    print (Email)

