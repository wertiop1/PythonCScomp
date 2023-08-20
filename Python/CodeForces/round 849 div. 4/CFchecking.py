import sys
ans = []
char = []
for _ in range(int(sys.stdin.readline())):
    char.append(str(sys.stdin.readline().strip('\n')))
for i in range(len(char)):
    if char[i] in ['c','o','d','e','f','o','r','c','e','s']:
        print("yes")
    else:
        print("no")
'''
for _ in range(int(sys.stdin.readline())):
    char = sys.stdin.readline()
    if char in "codeforces":
        ans.append("yes")
    else:
        ans.append("no")
'''