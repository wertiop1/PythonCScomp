import sys
sys.stdin = open('sleepy.in','r')
sys.stdout = open('sleepy.out','w')
n = int(input())
cowOrder = [int(i) for i in input().split()]
for i in range(n-1,0,-1):
    if cowOrder[i] < cowOrder[i-1]:
        ans = i
        break
print(ans)
