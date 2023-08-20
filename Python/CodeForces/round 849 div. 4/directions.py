import sys
t = int(sys.stdin.readline())
n = []
CSequence = []
def CInterpretor(command,startpos):
    if command == "U":
        startpos[1] += 1
    if command == "D":
        startpos[1] -= 1
    if command == "R":
        startpos[0] += 1
    if command == "L":
        startpos[0] -= 1
    return startpos

for _ in range(t):
    n.append(int(sys.stdin.readline()))
    CSequence.append(sys.stdin.readline().strip('\n'))
for i in range(t):
    startpos = [0,0]
    csequence = [i for i in CSequence[i]]
    APos = CInterpretor(csequence[0],startpos)
    if APos == [1,1]:
        print('YES')
        continue
    for j in range(1,n[i]):
        APos = CInterpretor(csequence[j],APos)
        if APos == [1, 1]:
            break
    if APos == [1,1]:
        print('YES')
        continue
    else:
        print('NO')
