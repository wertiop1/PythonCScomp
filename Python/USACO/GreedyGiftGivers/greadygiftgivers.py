"""
ID: derekyi2
LANG: PYTHON3
TASK: gift1
"""

with open("gift1.in", "r") as fin:
    NP = int(fin.readline().strip())
    for i in range(NP):                
        name = fin.readline().strip() 