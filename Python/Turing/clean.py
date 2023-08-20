import sys
n, q = [int(i) for i in sys.stdin.readline().split()]
a =[]
k = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))
for _ in range(q):
    k.append(int(sys.stdin.readline()))
def add(start, list, size):
    total = 0
    for i in range(start, size+start):
        total = total + list[i]
    return total
for j in range(q):
    pos = []
    for i in range(n-(k[j]-1)):
        pos.append(add(i,a,k[j]))
    sys.stdout.write(str(min(pos)) + "\n")
