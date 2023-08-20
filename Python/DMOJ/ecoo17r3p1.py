for i in range(10):
    stuff = input().split()
    franchise = int(stuff[0])
    days = int(stuff[1])
    totalInfo = []
    bonus = 0
    for y in range(days):
        info = input().split()
        for x in range(franchise):
            info[x] = int(info[x])
        totalInfo.append(info)
