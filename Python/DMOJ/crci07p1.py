n = int(input())
platforms = []
platformCords = []
yCords = []
xCords = []
def overlap(plat1Max,plat2Min):
    if plat2Min - plat1Max <= 0:
        False
    else:
        True
def pillar_from(platforms, plat1Max, plat2Min, height):
    bottom = 0
    for platform in platforms:
        if (platform[0] < height and platform[0] > bottom and covers(plat1Max, plat2Min)):
            bottom = platform[0]
    return height - bottom
total = 0
for i in range(n):
    platformCords = input().split()
    for j in range(len(platformCords)):
        platformCords[j] = int(platformCords[j])
    platforms.append(platformCords)
    yCords.append(platformCords[0])
    xCords.append(platformCords[1])
    xCords.append(platformCords[2])

for platformCords in platforms 
    if overlap(min(xCords[2*i-3],xCords[2*i-2]),max(xCords[2*i-1],xCords[2*i])) is True and platform:
        total
print(total)