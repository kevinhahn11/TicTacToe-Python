# Tic Tac Toe Game in Python

board = [' ' for x in range(10)]

def gameMode(response):
    if response == "Y":
        multiplayerMode = True
    else:
        multiplayerMode = False
def insertLetter(letter, pos):
    board[pos]= letter
def spaceIsFree(pos):
    return board[pos] == ' '
def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)
def player2_move():
    run = True
    while run:
        move = input('Please select a position to place an \'O\' (1-9): ')
        if move == "q":
            import sys
            sys.exit()
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('O', move)
                else:
                    print('Sorry, this space is occupied!')
        except:
            print('Please type a number!')
def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        if move == "q":
            import sys
            sys.exit()
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
        except:
            print('Please type a number!')
def compMove():
    possibleMoves = [ x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    if 5 in possibleMoves:
        move = 5
        return move
    
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

    return move
    
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
def main():
    multiplayerMode = False
    print("Welcome to Tic-Tac-Toe!\nPress q at any time to terminate the program.\nWould you like to play multiplayer?")
    print("If yes, enter \'Y\'. Otherwise, enter \'N\': ")
    response = input()
    while(response != "Y" and response != "N"):
        print("Please enter either \'Y\' or \'N\'! ")
        response = input()
    
    if response == "Y":
        # multiplayer mode is true
        print("Player 1 is X and Player 2 is O\n")
        printBoard(board)
        unableToMakeMove = False
        while not(isBoardFull(board)):
            if not(isWinner(board, "O")): # check if player 2 has won
                playerMove() # player 1 makes their move
                printBoard(board)
            else:
                print("O\'s won this time! Player 2 wins")
                break

            if not(isWinner(board, "X")): # check if player 1 has won
                player2_move()
                printBoard(board)
            else:
                print("X\'s won this time! Player 1 wins")
                break;
                """      
                if move == 0:
                    # function was not able to make a move, i.e. the board was full
                    # or some other strange reason.
                    print('Tie game!')
                    unableToMakeMove = True
                else:
                    insertLetter('O', move) # player 2 makes their move
                    print('Player 2 placed an \'O\' in position ', move, ':')
                    printBoard(board)
                """
            
        if isBoardFull(board) and unableToMakeMove is False:
            print("Tie game!")
    else:
        printBoard(board)
        unableToMakeMove = False
        while not(isBoardFull(board)):
            if not(isWinner(board, "O")): # check if computer has won
                playerMove()
                printBoard(board)
            else:
                print("Sorry, O\'s won this time! ")
                break

            if not(isWinner(board, "X")): # check if player has won
                move = compMove()
                if move == 0:
                    # function was not able to make a move, i.e. the board was full
                    # or some other strange reason.
                    print('Tie game!')
                    unableToMakeMove = True
                else:
                    insertLetter('O', move)
                    print('Computer placed an \'O\' in position ', move, ':')
                    printBoard(board)
            else:
                print("Sorry, X\'s won this time! Good job!")
                break
            
        if isBoardFull(board) and unableToMakeMove is False:
            print("Tie game!")
        
main()
while True:
    print("Play again?\nType \'Yes\' or \'No\'")
    s = input()
    if s == "Yes":
        board = [' ' for x in range(10)]
        main()
    else:
        break
