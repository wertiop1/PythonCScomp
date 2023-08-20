import sys
from math import floor
n = int(sys.stdin.readline())
multof3 = floor(n/3)
multof5 = floor(n/5)
multof15 = floor(n/15)
moos = multof3+multof5-multof15
previousMoos = moos
i = n+moos
j = n
while j != i:
    j += 1
    if j%3 == 0 or j%5==0:
        multof3 = floor(j/3)
        multof5 = floor(j/5)
        multof15 = floor(j/15)
        moos = multof3+multof5-multof15
        i = i+moos-previousMoos
        previousMoos = moos
sys.stdout.write(str(i))
'''
1 2 moo 4 moo moo 7 8 moo moo 11 moo 13 14 moo 16 17 moo 19 moo moo 22 23
'''