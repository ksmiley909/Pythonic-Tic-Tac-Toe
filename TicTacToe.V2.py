#Tic Tac Toe Written in Python
                                   
board = [' ' for x in range (10)]


def insertLetter (letter, pos):
    board [pos] = letter

def spaceIsFree (pos):
    return board [pos] == ' ' 

def printBoard(board):
    print( '     |        | ')
    print( '   '  + board[1] +  ' |    '  + board [2] +  '   |   ' +board[3])
    print( '     |        | ')
    print('----------------------')
    print( '     |        | ')
    print( '   '  + board[4] +  ' |    '  + board [5] +  '   |   ' +board[6])
    print( '     |        | ')
    print('----------------------')
    print( '     |        | ')
    print( '  '  + board[7] +   '  |    '  + board [8] +  '   |   ' +board[9])
    print( '     |        | ')

    
def isWinner (bo, le):
    return ((bo[7] == le and bo [8] == le and bo [9] ==  le) or(bo [4] == le and bo [5] == le and bo [6] == le) or(bo [1] == le and bo [2] == le and bo [3] == le) or(bo [1] == le and bo [4] == le and bo [7] == le) or(bo [2] == le and bo [5] == le and bo [8] == le) or(bo [3] == le and bo [6] == le and bo [6] == le) or(bo [1] == le and bo [5] == le and bo [9] == le) or(bo [3] == le and bo [5] == le and bo [7] == le)) 

def playerMove():
    run = True
    while run:
        move = input ('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print ('Sorry, this space is occupied!') 
            else:
                 print('Please type a number within the range!')
        except:
            print ('Please type a number!') 

def compMove():
    possibleMoves = [x for x, letter in enumerate (board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board [:]
            boardCopy [i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
            if i in [1,3,7,9]:
                cornersOpen.append(i)
            if len (cornersOpen) > 0:
                move = selectRandom (cornersOpen)
                return move

            if 5 in possibleMoves:
                move = 5
                return move
            
    edgesOpen = []
    for i in possibleMoves:
            if i in [2,4,6,8]:
                edgesOpen.append(i)
                return (move)

    if len (edgesOpen) > 0 :
            move = selectRandom (edgesOpen)
            return (move)
            
    return (move)  #Tech_With_Tim code altered. Option for tie game error fix.
                   #w/o this return statement functions do not end returning "none" result.

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange (0,ln)
    return li [r]

def isBoardFull (board):
    if board.count (' ') != 0 :  #Tech_With Tim Code altered.  Was --> if board.count (' ') > 1: 
        return False
    else:
        return True

def restart(board):             #V2 Addition.  Restart prompt after game is completed.  Nested and looped in the main functions. 
    user_input = input("Play Again?: [Press Enter to Continue]")
    

def clearBoard(board):          #v2 Update.  Funtion nested and looped inside the main function. 
    for x in range (1,10): 
        insertLetter (' ', x)
         
    
    
while True: #v2 Add. Main function looped for continuous restarts. 
    def main():
        print ('Welcome to Tic Tac Toe! ')
        clearBoard(board) #* clearBoard function call.  Initiates fresh board. 
        printBoard(board)
         

    #print(isBoardFull(board) == False)

        while [(isBoardFull (board) == False)]:
            if not (isWinner (board, 'O')):
                playerMove()
                printBoard(board)
            else:
                print('Sorry, O\'s win this time!')
                break

            if not (isWinner (board, 'X')):
                move = compMove()
                if move == 0:    # Tech_With_Tim code altered: one option to fix tie error: move == none instead of move == 0.
                             #Missing return statement was not ending compMove function calls.
                    print ('Tie Game')
                else:
                    insertLetter( 'O', move)
                    print('Computer placed an \'O\' in position', move, ':')
                    printBoard(board)
                      
            else:
                print('X\'s win!  Well Done!')
                break
        

            if (isBoardFull (board) == True): 
                print ('Tie Game!')
        

            
                    
    main()
    restart(board)  #restart function call.  Initiates "Play Again?" prompt.  
     
    


