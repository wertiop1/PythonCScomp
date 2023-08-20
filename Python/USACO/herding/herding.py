import sys
sys.stdin = open('herding.in','r')
sys.stdout = open('herding.out','w')
b,e,m = map(int, input().split())
if m == b + 2:
    print(0)
elif e == b+1 or m == e+1 or m == e+2:
    print(1)
else:
    print(2)
print(max(e-b,m-e)-1)