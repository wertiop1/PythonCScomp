import sys
q = int(sys.stdin.readline())
answers = []
for _ in range(q):
    n,t = [int(i) for i in sys.stdin.readline().split()]
    duration = [int(i) for i in sys.stdin.readline().split()]
    entertainment = [int(i) for i in sys.stdin.readline().split()]
    swiped = 0
    working = []
    second = []
    for i in range(n):
        if duration[i] + swiped == t:
            working.append(i)
        elif duration[i] + swiped < t:
            second.append(i)
        swiped += 1
    if len(working) == 0:
        if len(second) == 0:
            answers.append("-1")
            continue
    if len(working) != 0:
        ans = working[0]
        for i in range(1,len(working)):
            if entertainment[ans] < entertainment[working[i]]:
                ans = working[i]
    else:
        ans = max(second)
    answers.append(str(ans+1))
for i in range(len(answers)-1):
    sys.stdout.write(answers[i]+"\n")
sys.stdout.write(answers[-1])