import sys
t = int(sys.stdin.readline())
ans = []
for _ in range(t):
    books = int(sys.stdin.readline())
    minRead = []
    skillBin = []
    for _ in range(books):
        temp = sys.stdin.readline().split()
        if temp[1] == '00':
            continue
        minRead.append(int(temp[0]))
        skillBin.append(int(temp[1]))
    twoSkill = []
    oneSkill = []
    threeSkill = []
    for i in range(len(minRead)):
        if skillBin[i] == 1:
            oneSkill.append(minRead[i])
        elif skillBin[i] == 10:
            twoSkill.append(minRead[i])
        else:
            threeSkill.append(minRead[i])
    if len(threeSkill) != 0:
        minimum = min(threeSkill)
        if len(twoSkill) != 0 and len(oneSkill) != 0:
            minimum = min([min(twoSkill)+min(oneSkill),minimum])
    elif len(twoSkill) != 0 and len(oneSkill) != 0:
        minimum = min(twoSkill)+min(oneSkill)
    else:
        minimum = -1
    ans.append(minimum)
for i in range(t):
    print(ans[i])