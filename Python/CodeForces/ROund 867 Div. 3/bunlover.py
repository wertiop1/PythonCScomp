import sys
answer = []
def solve(n):
    return (n+2)*(n-1)+n+4
for _ in range(int(sys.stdin.readline())):
    size = int(sys.stdin.readline())
    answer.append(str(solve(size)))
for i in range(len(answer)-1):
    sys.stdout.write(answer[i]+"\n")
sys.stdout.write(answer[-1])