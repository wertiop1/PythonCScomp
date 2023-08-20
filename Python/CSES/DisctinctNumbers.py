import sys
n = int(sys.stdin.readline())
x = set()
var = [i for i in sys.stdin.readline().split()]
x.update(var)
print(len(x))