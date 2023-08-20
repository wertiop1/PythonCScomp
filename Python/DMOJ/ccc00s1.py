quarters = int(input())
machine1 = int(input())
machine2 = int(input())
machine3 = int(input())
i = 1
rounds = 0
while True:
    if (machine1 + i)%35 == 0:
        quarters = quarters + 30
    if quarters - 1 == 0:
        rounds = rounds + 1
        break
    if (machine2 + (i+1))%100 == 0:
        quarters = quarters + 60
    if quarters - 2 == 0:
        rounds = rounds + 1
        break
    if (machine3 + (i + 2))%10 == 0:
        quarters = quarters + 9
    if quarters - 3 == 0:
        rounds = rounds + 1
        break
    else:
        quarters = quarters + 3
    i = i + 3
print("Martha plays " + str(rounds) + " times before going broke.")

