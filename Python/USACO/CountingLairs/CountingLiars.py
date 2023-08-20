import sys
n = sys.stdin.readline()
LValues = []
GValues = []
for _ in range(n):
    gOrL, x = [i for i in sys.stdin.readline().split()]
    x = int(x)
    if gOrL == "G":
        GValues.append(x)
    else:
        LValues.append(x)
LValues.sort()
GValues.sort()



