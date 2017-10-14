def checkIfWon(playString):
    if len(playString) < 3:
        return -1
    if 'G' in playString and 'H' in playString and 'I' in playString:
        return 6
    elif 'G' in playString and 'E' in playString and 'C' in playString:
        return 7
    elif 'D' in playString and 'E' in playString and 'F' in playString:
        return 5
    elif 'C' in playString and 'F' in playString and 'I' in playString:
        return 4
    elif 'B' in playString and 'E' in playString and 'H' in playString:
        return 3
    elif 'A' in playString and 'D' in playString and 'G' in playString:
        return 1
    elif 'A' in playString and 'B' in playString and 'C' in playString:
        return 0
    elif 'A' in playString and 'E' in playString and 'I' in playString:
        return 2
    else:
        return -1
    
    
options = {0: ['A', 'B', 'C'], 1: ['A', 'D', 'G'], 2: ['A', 'E', 'I'], 3: ['B', 'E', 'H'], 4: ['C', 'F', 'I'], 5: ['D', 'E', 'F'], 6: ['G', 'H', 'I'], 7: ['G', 'E', 'C']}
convToSquare = {"1 1": 'A', "1 2": 'B', "1 3": 'C', "2 1": 'D', "2 2": 'E', "2 3": 'F', "3 1": 'G', "3 2": 'H', "3 3": 'I'}
convToMove = {'A': "1 1", 'B': "1 2", 'C': "1 3", 'D': "2 1", 'E': "2 2", 'F': "2 3", 'G': "3 1", 'H': "3 2", 'I': "3 3"}

def findMovesForResult(result, x):
    
    noPlayOptions = options[result]
    play = []
    for y in range(1, x):
        if pref[y] not in noPlayOptions:
            play.append(pref[y])
            
    return [x-len(play), play]


pref = []
for x in range(9):
    pref.append(convToSquare[input()])

playedString = pref[0]
possibleWinning = []
bestResultSize = 11

x = 1
while x < 9:
    playedString += pref[x]
    result = checkIfWon(playedString)
    if result != -1:
        bestCheck = findMovesForResult(result, x)
        if bestCheck[0] <= bestResultSize:
            bestResultSize = bestCheck[0]
            possibleWinning.append([result, x, bestCheck[1]])
    x += 1

#Now find which of the possible winning is best.
bestIndex = 0
for x in range(1, len(possibleWinning)):
    play = possibleWinning[x][2]
    if play[0] < possibleWinning[bestIndex][2][0]:
        bestIndex = x

play = possibleWinning[bestIndex][2]
result = possibleWinning[bestIndex][0]
movesReq = possibleWinning[bestIndex][1] - len(play)

#then fill out the rest of play with legit characters, starting at the smallest.

while len(play) < movesReq:
    if 'A' not in play:
        play.append('A')
    elif 'B' not in play:
        play.append('B')
    elif 'C' not in play:
        play.append('C')
    elif 'D' not in play:
        play.append('D')
    elif 'E' not in play:
        play.append('E')
    elif 'F' not in play:
        play.append('F')
    elif 'G' not in play:
        play.append('G')
    elif 'H' not in play:
        play.append('H')
    else:
        play.append('I')

for x in play:
    print(convToMove[x])
