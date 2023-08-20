import sys
t = int(sys.stdin.readline())
ans = []
for _ in range(t):
    n = int(sys.stdin.readline())
    s = [i for i in sys.stdin.readline()]
    prev = s[0]
    answer = []
    switch = False
    for i in range(1,n):
        if s[i] == prev:
            answer.append(s[i])
            switch = True
        elif switch is True:
            prev = s[i]
            switch = False
    ans.append("".join(answer))
for i in range(t):
    print(ans[i])