import sys
n,x,y = [int(i) for i in sys.stdin.readline().split()]
a = []
b =[]
for _ in range(n):
    list = [int(i) for i in sys.stdin.readline().split()]
    a.append(list[0])
    b.append(list[1])
def game(a,b):
    win = False
    bessie = [x,y]
    opponent = [a,b]
    while 1:
        bessie.sort()
        opponent.sort()
        opponent[1] += bessie[1]
        if opponent[1] > 2:
            opponent[1] = 0
        if opponent[0] == 0 and opponent[1] == 0:
            win = True
            return win
        bessie.sort()
        opponent.sort()
        bessie[1] += opponent[1]
        if bessie[1] > 2:
            bessie[1] = 0
        if bessie[0] == 0 and bessie[1] == 0:
            win = False
            return win
    
for i in range(n):
    if game(a[i],b[i]) is True:
        print("W")
    else:
        print("L")
    