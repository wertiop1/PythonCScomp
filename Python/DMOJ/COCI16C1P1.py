X = int(input())
N = int(input())
totalMegabytes = (N+1)*(X)
for I in range(N):
    P = int(input())
    totalMegabytes = totalMegabytes - P
    I = I + 1
print(totalMegabytes)
