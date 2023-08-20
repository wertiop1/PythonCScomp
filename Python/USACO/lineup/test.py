from itertools import chain
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
lists = [[0, 7], [1], [2, 5], [2, 6], [3], [4], [5, 2, 6]]
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
print(lists)
for i in range(len(lists)):
    print(str({j for j in cows if cows[j] == lists[i]}).strip("{'}"))
