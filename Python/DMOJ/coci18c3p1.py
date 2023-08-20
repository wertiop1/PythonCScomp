word = list(input())
H = 0
O = 0
N = 0
I = 0

for H in range(len(word)):
    if word[H] == "H":
        pass
    else:
        print(0)
        exit()
for O in range(len(word)):
    if word[O] == "O":
        pass
    else:
        print(0)
        exit()
for N in range(len(word)):
    if word[N] == "N":
        pass
    else:
        print(0)
        exit()
for I in range(len(word)):
    if word[I] == "I":
        pass
    else:
        print(0)
        exit()
for H in range(len(word)):
    H += H
    if word[H] == "H":
        break
    else:
        pass
for O in range(len(word)):
    O += O
    if word[O] == "O":
        break
    else:
        pass
for N in range(len(word)):
    N += N
    if word[N] == "N":
        break
    else:
        pass
for I in range(len(word)):
    I += I
    if word[I] == "I":
        break
    else:
        pass
if H+1 == O:
    if O + 1 == N:
        if N + 1 == I:
            honiBlocks = honiBlocks + 1
else:
    print(0)
    exit()