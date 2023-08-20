for dataset in range(10):
    info = input().split()
    t = int(info[0])
    n = int(info[1])
    time = 0
    for i in range(n):
        day = input()
        if day == 'B':
            time = time + t - 1
        else:
            if time > 0:
                time = time - 1
    print(time)