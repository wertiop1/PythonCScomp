import sys
n,k,t = [int(i) for i in sys.stdin.readline().split()]
a = [int(i) for i in sys.stdin.readline().split()]
tempa = []
cows = [int(i) for i in range(n)]
for _ in range(t):
    c = []
    for i in range(len(a)):
        c.append(cows[a[i]])
    tempa = c[-1:] + c[:-1]
    for i in range(len(a)):
        cows[a[i]] = tempa[i]
    for i in range(len(a)):
        if a[i]+1 == n:
            a[i] = 0
        else:
            a[i] += 1

for i in range(n-1):
    sys.stdout.write(str(cows[i]) + ' ')
sys.stdout.write(str(cows[n-1]))