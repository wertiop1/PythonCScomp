inFile = open('censor.in', 'r')
outFile = open('censor.out', 'w')
s = inFile.readline()
t = inFile.readline()
notdone = True
while notdone:
    s = s.replace(t,'')
    if s.__contains__(t) is False:
        notdone = False
outFile.write(s)