subs = int(input())
i = 1
while True:
    leftover = 10**i - subs
    if leftover <= 0:
        i += 1
        continue
    else:
        print(leftover)
        break