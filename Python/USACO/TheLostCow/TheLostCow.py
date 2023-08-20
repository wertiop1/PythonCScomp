inFile = open("lostcow.in",'r')
outFile = open('lostcow.out','w')
info = inFile.read().split()
x = int(info[0])
y = int(info[1])
var = 0
if y>x:
    while x+(2 ** var) < y:
        var += 2
else:
    while x-(2 ** var) > y:
        var += 2
totalDist = 1
if var != 0:
    totalDist = 1
    for i in range(1, var):
        totalDist += (2 ** i) + (2 ** (i - 1))
    totalDist += (2 ** (var - 1)) + abs(x - y)
outFile.write(str(totalDist))
outFile.close()