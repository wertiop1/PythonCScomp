import sys
n = int(sys.stdin.readline())
s = [char for char in sys.stdin.readline()]
s = list(map(lambda x: x.replace('S', 'F'), s))
excitement = 0
extra = 0
level = []
previous = 0
for i in range(n-1):
    if s[i] == s[i+1] and s[i] != 'F':
        excitement += 1
    elif s[i+1] == 'F':
        if previous == i+1:
            extra -= 1
            excitement += 1
        else:
            extra += 1
            previous = i+1
    elif s[i] == 'F':
        if s[i+1] == 'F':
            if i == 0:
                for j in range[i, s-i]:
                    if s[j] != 'F':
                        a = j
                        
            else:

            i = 
        else:
            extra += 1
for i in range(extra+1):
    level.append(excitement+i)
sys.stdout.write(str(len(level)) + '\n')
for i in range(len(level)):
    sys.stdout.write(str(level[i])+ '\n')