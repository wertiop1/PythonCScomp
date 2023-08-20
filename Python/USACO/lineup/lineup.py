import sys
from itertools import chain
sys.stdin = open('lineup.in','r')
sys.stdout = open('lineup.out','w')
n = int(input())
cows = {
    'Beatrice':0,
    'Belinda':1, 
    'Bella':2, 
    'Bessie':3, 
    'Betsy':4, 
    'Blue':5, 
    'Buttercup':6, 
    'Sue':7
}
nodes = {
    0:[],
    1:[],
    2:[],
    3:[],
    4:[],
    5:[],
    6:[],
    7:[]
}
order = []
lists = []
for _ in range(n):
    temp = input().split()
    nodes[cows[temp[0]]].append(cows[temp[5]])
    nodes[cows[temp[5]]].append(cows[temp[0]])
for i in range(8):
    nodes[i].sort()
    if len(nodes[i]) == 2:
        temp = [nodes[i][0],i, nodes[i][1]]
        lists.append(temp)
    elif len(nodes[i]) == 0:
        lists.append([i])
    else:
        temp = sorted([i,nodes[i][0]])
        if temp not in lists:
            lists.append(temp)
lists.sort(key=lambda l: l[0])
for i in range(len(lists)):
    try:
        for j in range(len(lists[i])):
            for x in range(len(lists)):
                try:
                    for y in range(len(lists[x])):
                        try:
                            if x != i and j != y:
                                if lists[i][j] == lists[x][y]:
                                    if len(lists[i]) >= len(lists[x]):
                                        lists.remove(lists[x])
                                    else:
                                        lists.remove(lists[i])
                        except:
                            pass
                except:
                    pass
    except:
        pass
lists = list(chain(*lists))
for i in range(len(lists)):
    print(str({j for j in cows if cows[j] == lists[i]}).strip("{'}"))