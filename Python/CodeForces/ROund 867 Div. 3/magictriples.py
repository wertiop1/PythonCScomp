import sys
answer = []
def printans():
    for i in range(len(answer)-1):
        sys.stdout.write(answer[i]+"\n")
    sys.stdout.write(answer[-1])
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    arr = [int(a) for a in sys.stdin.readline().split()]
    ans = 0
    for i in range(n-1):
        for j in range(i+1,n):
            ak  = arr[j]**2 / arr[i]
            if ak in arr:
                ans += 1
    answer.append(str(ans))
printans()