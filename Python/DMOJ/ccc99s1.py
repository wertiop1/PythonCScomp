cardNumber = 52
def noHigh(info):
    if 'jack' in info:
        return False
    elif 'queen' in info:
        return False
    elif 'king' in info:
        return False
    elif 'ace' in info:
        return False
    return True
deck = []
for i in range(cardNumber):
    deck.append(input())
scoreA= 0
scoreB = 0
player = 'A'
for i in range(cardNumber):
    card = deck[i]
    points = 0
    remaining = cardNumber - i - 1
    if card == 'jack' and remaining >= 1 and noHigh(deck[i+1:i+2]):
        points = 1
    elif card == 'queen' and remaining >= 2 and noHigh(deck[i+1:i+3]):
        points = 2
    elif card == 'king' and remaining >= 3 and noHigh(deck[i+1:i+4]):
        points = 3
    elif card == 'ace' and remaining >= 4 and noHigh(deck[i+1:i+5]):
        points = 4
    if points > 0:
        print(f'Player {player} scores {points} point(s).')
    if player == 'A':
        scoreA = scoreA + points
        player = 'B'
    else:
        scoreB = scoreB + points
        player = 'A'

print('Player A: '+str(scoreA)+' point(s).')
print('Player B: ' +str(scoreB)+ ' point(s).')