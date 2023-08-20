import sys
ans =[]
t = int(sys.stdin.readline())
for _ in range(t):
    arrlen = int(sys.stdin.readline())
    arr = [int(i) for i in sys.stdin.readline().split()]
    blanks = [0]
    blank = 0
    for i in range(arrlen):
        if arr[i] == 0:
            blank += 1
        else:
            blanks.append(blank)
            blank = 0
    blanks.append(blank)
    ans.append(max(blanks))
for i in range(t):
    print(ans[i])