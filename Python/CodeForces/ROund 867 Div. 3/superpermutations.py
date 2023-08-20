import sys
answer = []
def printans():
    for i in range(len(answer)-1):
        sys.stdout.write(answer[i]+"\n")
    sys.stdout.write(answer[-1])
for _ in range(int(sys.stdin.readline())):
    pass