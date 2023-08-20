firstHalf = 1440
firstHalfPoints = 0
a = int(input())
aTime = []
for i in range(a):
    As = int(input())
    aTime.append(As)
b = int(input())
bTime = []
for i in range(b):
    Bs = int(input())
    bTime.append(Bs)
for i in range(a):
    if aTime[i] <= firstHalf:
        firstHalfPoints = firstHalfPoints + 1
for i in range(b):
    if bTime[i] <= firstHalf:
        firstHalfPoints += 1
print(firstHalfPoints)
pointsPerTurnA = [0]
x = 0
for second in range(1, firstHalf * 2 + 1):
    if x < len(aTime) and aTime[x] == second:
        pointsPerTurnA.append(pointsPerTurnA[second - 1] + 1)
        x = x + 1
    else:
        pointsPerTurnA.append(pointsPerTurnA[second - 1])
pointsPerTurnB = [0]
x = 0
for seconds in range(1, firstHalf*2+1):
    if x < len(bTime) and bTime[x] == seconds:
        pointsPerTurnB.append(pointsPerTurnB[seconds-1]+1)
        x = x + 1
    else:
        pointsPerTurnB.append(pointsPerTurnB[seconds - 1])
turnArounds = 0
winning = ''
for i in range(firstHalf * 2):
    if winning != 'a' and pointsPerTurnA[i] > pointsPerTurnB[i]:
        winning = 'a'
        turnArounds +=1
    elif winning != 'b' and pointsPerTurnB[i] > pointsPerTurnA[i]:
        winning = 'b'
        turnArounds += 1
print(turnArounds-1)