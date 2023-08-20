import sys
sys.stdin = open('cownomics.in','r')
sys.stdout = open('cownomics.out','w')
n, m = [int(i) for i in input().split()]

for _ in range(n):
   pass 
'''
(here, A or G means spotty and C means plain; T is irrelevant since it does not appear in any of Farmer John's cows at position 2

Positions:    1 2 3 4 5 6 7 ... M

Spotty Cow 1: A A T C C C A ... T
Spotty Cow 2: G A T T G C A ... A
Spotty Cow 3: G G T C G C A ... A

Plain Cow 1:  A C T C C C A ... G
Plain Cow 2:  A C T C G C A ... T
Plain Cow 3:  A C T T C C A ... T
'''
