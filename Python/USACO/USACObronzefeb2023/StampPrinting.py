import sys
t = int(sys.stdin.readline())
tests = []
def rotate90(arr,n):
    newlist = []
    for j in range(n) :
        for i in range(n - 1, -1, -1) :
            newlist.append(arr[i][j])
    return newlist
for _ in range(t):
    n = int(sys.stdin.readline())
    painting = []
    brush = []
    possible = False
    for _ in range(n):
        painting.append([x for x in sys.stdin.readline().strip()])
    k = int(sys.stdin.readline())
    for _ in range(k):
        brush.append([x for x in sys.stdin.readline().strip()])
    for j in range(len(painting)/n):
        for i in range(len(painting[j]) - len(brush[j]) + 1):
            if painting[i: i + len(brush[j])] == brush[j]:
                loc = [i]
                
    if possible:
        sys.stdout.write("YES")
    else:
       sys.stdout.write("NO") 
'''
rules:
.>*
but other way around cannot happen
AB/CD>BD/AC>DC/BA>CA/DB
ABC/DEF/GHI>CFI/BEH/ADG
ABCD
EFGH
IJKL
MNOP

QRST

UVWXY
EJOTY
D
'''