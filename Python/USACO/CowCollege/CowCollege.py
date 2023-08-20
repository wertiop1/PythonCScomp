import sys
def findSum(price, cows, n):
    paying = cows-n
    return int(price)*paying
n = int(sys.stdin.readline())
CowTuition = sys.stdin.readline().split()
CowTuition.sort()
sum = findSum(CowTuition[0], n, 0)
Price = CowTuition[0]
for i in range(1, n-1):
    NewSum = findSum(CowTuition[i], n, i)
    if sum < NewSum:
        sum = NewSum
        Price = CowTuition[i]
    elif sum == NewSum:
        if int(Price) < int(CowTuition[i]):
            continue
        else:
            Price = CowTuition[i]
sys.stdout.write(str(sum) + " " + str(Price))

