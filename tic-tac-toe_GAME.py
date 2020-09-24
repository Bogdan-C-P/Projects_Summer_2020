import random
board=[" " for x in range(10)]

def insertLetter(letter,pos):
    board[pos] =letter
def printBoard(board):
    print("-------------")
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+ " ")
    print("-------------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("-------------")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("-------------")

def spaceIsFree(pos):
    return board[pos] == ' '
def isBoardFull(board):
    if board.count(" ")>1:
        return False
    else:
        return True

def IsWinner(b,l):
    if b[1]==l and b[2]==l and b[3]==l:
        return True
    elif b[4]==l and b[5]==l and b[6]==l:
        return True
    elif b[7] == l and b[8] == l and b[9] == l:
        return True
    elif b[1] == l and b[4] == l and b[7] == l:
        return True
    elif b[2] == l and b[5] == l and b[8] == l:
        return True
    elif b[3] == l and b[6] == l and b[9] == l:
        return True
    elif b[1] == l and b[5] == l and b[9] == l:
        return True
    elif b[3] == l and b[5] == l and b[7] == l:
        return True
    else:
        return False

def userInput():
        while True:
            x=int(input("add the position you would like between 1 to 9: "))
            if x>=1 and x<=9:
                break
        if spaceIsFree(x):
            insertLetter("X",x)
        else:
            print("sorry this position is occupied")

def computerMove():
    possibleMoves=[x for x,letter in enumerate(board) if letter==" "and x!=0]
    move=0
    for let in ["O","X"]:
        for i in possibleMoves:
            boardCopy=board[:]
            boardCopy[i]=let
            if IsWinner(boardCopy,let):
                move=i
                return move
    cornersOpen=[]
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen)>0:
        move= random.choice(cornersOpen)
        return move
    if 5 in possibleMoves:
        return 5

    edgesOpen=[]
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen)>0:
        move=random.choice(edgesOpen)
        return move

def main():
    print("Welcome:")
    printBoard(board)
    while not(isBoardFull(board)):
        if not IsWinner(board,"O"):
            userInput()
            printBoard(board)
        else:
            print("sorry you lose")
            break
        if not IsWinner(board,"X"):
            move=computerMove()
            if move==0:
                print("Tie Game")
            else:
                insertLetter("O",move)
                print("computer placed an O on position",move,":")
                printBoard(board)
        else:
            print("You win")
            break


    if isBoardFull(board):
        print("Tie game")

while True:
    x=input("Do you want to play again? y/n: ")
    if x.lower()== "y":
        board=[" " for x in range(10)]
        print("--------------")
        main()
    else:
        break