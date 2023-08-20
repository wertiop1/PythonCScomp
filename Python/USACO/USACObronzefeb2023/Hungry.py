import sys
n,t = map(int, sys.stdin.readline().split())
haybales = 0
imports = []
day = []
#time = 0
#hay = 0
gaps = 0
hayb = 0
for _ in range(n):
    d,b = map(int, sys.stdin.readline().split())
    day.append(d)#-1
    imports.append(b)
for i in range(n):
    x = imports[i]-day[i+1]
    if x < 0:
        gaps += x
    
    
'''
'''

'''
for i in range(t):
    if time >= len(day):
        pass
    elif i == day[time]:
        haybales += imports[time]
        time += 1
    if haybales > 0:
        hay += 1
        haybales -= 1
'''
hay = t-gaps
sys.stdout.write(str(hay))