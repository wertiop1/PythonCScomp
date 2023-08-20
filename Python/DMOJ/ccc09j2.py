from math import floor
troutPoints = int(input())
pikePoints = int(input())
pickerelPoints = int(input())
totalPoints = int(input())
options = 0
def maxFish(fishPoints, totalPoints):
    return floor(totalPoints/fishPoints) + 1
trout = 0
pike = 0
pickerel = 0
maxPickerel = maxFish(pickerelPoints, totalPoints)
maxTrout = maxFish(troutPoints, totalPoints)
maxPike = maxFish(pikePoints, totalPoints)
for i in range(maxTrout):
    trout = maxTrout-i-1
    if trout < 0:
        trout = 0
    j = 0
    for j in range(maxPike):
        pike = maxPike - j -1
        if pike < 0:
            pike = 0
        l = 0
        for l in range(maxPickerel):
            pickerel = maxPickerel - l -1
            if pickerel < 0:
                pickerel = 0
            if trout*troutPoints+pike*pikePoints+pickerel*pickerelPoints <= totalPoints:
                if trout == 0:
                    if pike == 0:
                        if pickerel == 0:
                            continue
                options += 1
                print(f'{trout!r} Brown Trout, {pike!r} Northern Pike, {pickerel!r} Yellow Pickerel')
print(f'Number of ways to catch fish: {options!r}')