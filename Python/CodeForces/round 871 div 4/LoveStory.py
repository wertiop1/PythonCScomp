import sys
t = int(sys.stdin.readline())
Cstring = ['c','o','d','e','f','o','r','c','e','s']
ans = []
for _ in range(t):
    indice = 0
    TimurString = [i for i in sys.stdin.readline()]
    for i in range(10):
        if TimurString[i] != Cstring[i]:
            indice += 1
    ans.append(indice)
for i in range(t):
    print(ans[i])