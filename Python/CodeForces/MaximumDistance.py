import sys
n = int(sys.stdin.readline())
x = [int(i) for i in sys.stdin.readline().split()]
y = [int(i) for i in sys.stdin.readline().split()]
max = (x[0]-x[1])**2+(y[0]-y[1])**2
for i in range(n):
    for j in range(n):
        temp = (x[i]-x[j])**2+(y[i]-y[j])**2
        if max < temp:
            max = temp
sys.stdout.write(str(max))
'''
x1-x2)^2+(y1-y2)^2

'''