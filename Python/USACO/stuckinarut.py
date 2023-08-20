import sys
import numpy as np
n = int(sys.stdin.readline())
nCows = []
eCows = []
for _ in range(n):
    dir, x, y = [i for i in sys.stdin.readline().split()]
    if dir == 'E':
        eCows.append((int(x),int(y)))
    if dir == 'N':
        nCows.append((int(x),int(y)))
nCows.sort()
eCows.sort(key=lambda loc:loc[1])


'''
xVctr = np.array(xList)
yVctr = np.array(yList)
'''