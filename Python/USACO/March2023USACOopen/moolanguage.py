import sys
t = int(sys.stdin.readline())
for _ in range(t):
    fjDict = {}
    n,commas,periods = [int(i) for i in sys.stdin.readline().split()]
    for _ in range(n):
        word, Pos = [i for i in sys.stdin.readline().split()]
        fjDict[word] = Pos
    conjunction = [i for i in fjDict if fjDict[i] == "conjuction"]
    noun = [i for i in fjDict if fjDict[i] == "noun"]
    transitive = [i for i in fjDict if fjDict[i] == "transitive-verb"]
    intransitive = [i for i in fjDict if fjDict[i] == "intransitive-verb"]
    
    '''
    sentence structures:
    S1 = noun + intransitive
    S2 = noun + transitive + noun, noun, noun ...
    S3 = S + conjunction + S
    '''