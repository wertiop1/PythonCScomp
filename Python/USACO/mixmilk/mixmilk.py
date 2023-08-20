
clist = [0 for _ in range(3)]
mlist = [0 for _ in range(3)]
with open("mixmilk.in") as read:
	for i in range(3):
		clist[i], mlist[i] = map(int, read.readline().split())
for i in range(100):
    b1 = i%3
    b2 = (i+1)%3
    milkswap = min(mlist[b1], clist[b2]-mlist[b2])
    mlist[b1] -= milkswap
    mlist[b2] += milkswap
for m in mlist:
    print(m)
with open("mixmilk.out",'w') as out:
    for m in mlist:
        print(m, file=out)

