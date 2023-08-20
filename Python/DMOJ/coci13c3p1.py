k = int(input())
a = 1
b = 0
for i in range(k):
    a2 = b
    b2 = b+a
    a = a2
    b = b2
print(a, b)
