parkedSpots = int(input())
dayF = list(input())
dayS = list(input())
countVar = 0
I = 1

for I in range(parkedSpots):
    if dayF[I-1] == 'C':
        if dayF[I-1] == dayS[I-1]:
            countVar = countVar + 1
        else:
            pass
    else:
        pass
    I = I+1
print(countVar)