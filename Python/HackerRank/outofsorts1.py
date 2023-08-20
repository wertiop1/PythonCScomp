import sys
n = int(sys.stdin.readline())
a = []
def bessieFunc(A):
    moo = 0
    sorted = False 
    while (not sorted): 
        sorted = True 
        moo += 1 
        for i in range(len(A)-1): 
            if A[i+1] < A[i]: 
                A[i], A[i+1] = A[i+1],A[i] 
                sorted = False
    return moo
for i in range(n):
    a.append(int(sys.stdin.readline()))
sys.stdout.write(str(bessieFunc(a)))