import random

holder = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def printScreen():
    print(f'      |      |      ')
    print('  ' + holder[0] + '   |  ' + holder[1] + '   |  ' + holder[2] + '   ')
    print(f'      |      |      ')
    print(f'--------------------')
    print(f'      |      |      ')
    print('  ' + holder[3] + '   |  ' + holder[4] + '   |  ' + holder[5] + '   ')
    print(f'      |      |      ')
    print(f'--------------------')
    print(f'      |      |      ')
    print('  ' + holder[6] + '   |  ' + holder[7] + '   |  ' + holder[8] + '   ')
    print(f'      |      |      ')

def placeTile(letter, pos):
    holder[pos] = letter

def isFree(pos):
    return holder[pos] == ' '

def randomOpponent(compLetter):
    g = 0
    while g < 1:
        x = random.random()
        compPos = round((x*8))
        if isFree(compPos):
            placeTile(compLetter, compPos)
            g = 1

def aiComp():
    best_score = -1000 #this needs to be a really low number
    best_move = 0 #this changes over time, but it is here to initialize

    for i in range(len(holder)):
        if isFree(i):
            placeTile(compLetter, i)
            score = miniMax(holder, 0, False)
            holder[i] = ' ' #the tile was filled but then emptied after the miniMax function
            if score > best_score: #this basically checks the best score. When it is found then keys are changed
                best_score = score
                best_move = i

    placeTile(compLetter, best_move)
    return

def miniMax(board, depth, isMaximizing):
    if isWinner(compLetter):
        return 100 - depth # subtract depth to prefer winning sooner rather than later
    elif isWinner(letter):
        return -100 + depth # add depth to prefer losing later rather than sooner
    elif isBoardFull():
        return 0

    if isMaximizing:
        best_score = -1000
        for i in range(len(board)):
            if isFree(i):
                board[i] = compLetter
                score = miniMax(board, depth+1, False)
                board[i] = ' '
                best_score = max(best_score, score)

        return best_score
    else:
        best_score = 1000
        for i in range(len(board)):
            if isFree(i):
                board[i] = letter
                score = miniMax(board, depth+1, True)
                board[i] = ' '
                best_score = min(best_score, score)

        return best_score


def isWinner(letter):
    if (holder[0] == letter and holder[1] == letter and holder[2] == letter) or (holder[3] == letter and holder[4] == letter and holder[5] == letter) \
    or (holder[6] == letter and holder[7] == letter and holder[8] == letter) or (holder[0] == letter and holder[4] == letter and holder[8] == letter) \
    or (holder[6] == letter and holder[4] == letter and holder[2] == letter) or (holder[0] == letter and holder[3] == letter and holder[6] == letter) \
    or (holder[1] == letter and holder[4] == letter and holder[7] == letter) or (holder[2] == letter and holder[5] == letter and holder[8] == letter):
        return True
    else:
        return False

def isBoardFull():
    c = 0
    for i in range(len(holder)):
        if holder[i] == "X" or holder[i] == "O":
            c += 1
    if c == 9:
        return True
    else:
        return False

letter = input("What letter do you want to be (X/O)?: ").upper()
while not(letter == "X" or letter == "O"):
    letter = input("You didn't input the right character, Retry: ").upper()

if letter == "X":
    compLetter = "O"
else:
    compLetter = "X"

while not (isBoardFull()):
    printScreen()
    pos = int(input("Place a tile (1-9): "))

    while pos < 1 or pos > 9:
        pos = int(input(f'Tile {str(pos)} doesn\'t exist, pick a proper position: '))

    new_pos = pos - 1

    while not isFree(new_pos) :
        new_pos = int(input(f'Tile {str(pos)} is taken, place a different one: ')) - 1

    placeTile(letter, new_pos)
    if isWinner(letter) or isWinner(compLetter):
        break
    aiComp()
    if isWinner(letter) or isWinner(compLetter):
        break

printScreen()
if isWinner(letter):
    print(f'{letter}\'s Win!')
elif isWinner(compLetter):
    print(f'{compLetter}\'s Win!')