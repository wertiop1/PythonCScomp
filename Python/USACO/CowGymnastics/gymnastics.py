def func(grid, cow1, cow2):
    booln = True
    i = 0
    while i < len(grid) and booln:
        if grid[i].index(cow1) > grid[i].index(cow2):
            booln = False
        else:
            i = i + 1
    return booln
inFile = open('gymnastics.in', 'r')
outFile = open('gymnastics.out', 'w')
lst = inFile.readline().split()
k = int(lst[0])
n = int(lst[1])
grid = []
for i in range(k):
    row = inFile.readline().split()
    for j in range(n):
        row[j] = int(row[j])
    grid.append(row)
consistentPairs = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j and func(grid, i, j):
            consistentPairs += 1
outFile.write(f'{consistentPairs}\n')
inFile.close()
outFile.close()
