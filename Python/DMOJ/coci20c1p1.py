getInfo = input().split()
r = int(getInfo[0])
s = int(getInfo[1])
sea = []
startX = None
startY = None
for i in range(r):
    row = input().split()
    sea.append(row)
def move(sea, curX, curY):
    while True:
        symbol = sea[curX]
