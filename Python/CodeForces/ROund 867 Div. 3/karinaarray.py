import sys
answer = []
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    arr = [int(a) for a in sys.stdin.readline().split()]
    max = -1000000
    for i in range(n-1):
        for j in range(i+1,n):
            if max < arr[i]*arr[j]:
                max = arr[i]*arr[j]
    answer.append(str(max))
for i in range(len(answer)-1):
    sys.stdout.write(answer[i]+"\n")
sys.stdout.write(answer[-1])