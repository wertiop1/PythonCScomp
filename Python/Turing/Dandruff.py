import sys
n,m,q = [int(i) for i in sys.stdin.readline().split()]
a1 = []
b1 = []
a2 = []
b2 = []
hair = []
dandruff = []
for _ in range(n):
    dandruff.append(sys.stdin.readline().split())
print(dandruff)
for _ in range(n):
    hair.append(sys.stdin.readline().split())
for _ in range(q):
    list = [int(i) for i in sys.stdin.readline().split()]
    a1.append(list[0])
    b1.append(list[1])
    a2.append(list[2])
    b2.append(list[3])
for i in range(q):
    a1[i],