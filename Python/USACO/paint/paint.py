import sys
sys.stdin = open('paint.in','r')
sys.stdout = open('paint.out','w')
a,b = map(int, input().split())
c,d = map(int, input().split())
x = (b-a) + (d-c) 
# total = x- intersection
points = {
    'a':a,
    'b':b,
    'c':c,
    'd':d
}
points = sorted(points.items(), key=lambda x:x[1])
if points[0][0] != 'a':
    if points[3][0] != 'b':
        intersection = min(a-b,0)
    else:
        intersection = min(a-d,0)
else:
    if points[3][0] != 'b':
        intersection = min(c-b,0)
    else:
        intersection = min(c-d,0)
print(x+intersection)