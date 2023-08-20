import sys
t = int(sys.stdin.readline())
n = []
binlist = []
for _ in range(t):
    n.append(int(sys.stdin.readline()))
    binlist.append(sys.stdin.readline().strip(' \n'))
for i in range(t):
    binstr = [int(j) for j in binlist[i]]
    Done = False
    while Done is False:
        if len(binstr) == 0:
            print(0)
            Done = True
        else:
            if binstr[-1] == 0:
                if binstr[0] == 1:
                    binstr[-1]
                    del binstr[0]
                    del binstr[-1]
                else:
                    print(len(binstr))
                    Done = True
            elif binstr[0] == 0:
                if binstr[-1] == 1:
                    binstr[-1]
                    del binstr[0]
                    del binstr[-1]
                else:
                    print(len(binstr))
                    Done = True
            else:
                print(len(binstr))
                Done = True