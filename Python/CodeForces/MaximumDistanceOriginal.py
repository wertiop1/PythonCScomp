import sys
n = int(sys.stdin.readline())
def distance(x1,y1,x2,y2):
    return ((x2-x1)**2)+((y2-y1)**2)
x = [int(i) for i in sys.stdin.readline().split()]
y = [int(i) for i in sys.stdin.readline().split()]
greatest = 0
for i in range(n):
    for j in range(n): 
        if greatest < distance(x[i],y[i],x[j],y[j]):
            greatest = distance(x[i],y[i],x[j],y[j])
sys.stdout.write(str(greatest))