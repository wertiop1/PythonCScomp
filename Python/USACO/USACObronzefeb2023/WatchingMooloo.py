import sys
n,k = map(int,sys.stdin.readline().split())
d = [int(i) for i in sys.stdin.readline().split()]
last = 0
ans = 0
for j in range(1,len(d)):
    if d[j]-d[j-1] > k:
        ans += (d[j-1]-d[last])+k+1
        last = j
ans += d[j]-d[last]+k+1
print(ans)
#COMPLETE 1ST TRY