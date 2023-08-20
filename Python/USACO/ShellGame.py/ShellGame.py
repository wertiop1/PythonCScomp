In = open('shell.in', 'r')
Out = open('shell.out', 'w')
n = int(In.readline())
shellPos = [i for i in range(3)]
score = [0 for _ in range(3)]
for _ in range(n):
    a, b, g = [int(i) - 1 for i in In.readline().split()]
    shellPos[a], shellPos[b] = shellPos[b], shellPos[a]
    score[shellPos[g]] += 1
Out.write(str(max(score)))

