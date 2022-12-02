#first function
def newBoard(n):
    board = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne += [0]
        board += [ligne]
    return board
#Procedure
def displayBoard(board,n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                print(".",end=" ")
            if board[i][j] == 1:
                print("X",end=" ")
            if board[i][j] == 2:
                print("O",end=" ")
        print()

def displayScore(score):
    print(score[0],"vs",score[1])

def possibleSquare(board,n,i,j):
    if i <n and j < n:
        if i >= 0 and j >= 0:
            if board[i][j] == 0:
                return True
    return False

#square

def selectSquare(board,n):
    x = int(input("entrer une ligne:"))
    y = int(input("entrer une colonne:"))
    while possibleSquare(board,n,x-1,y-1)==False:
        x = int(input("entrer une ligne:"))
        y = int(input("entrer une colonne:"))
    return x-1,y-1

def updateBoard(board,player,i,j):
    board[i][j]=player

def updateScore(board,n,player,score,i,j):
    countstart = None
    if (i != n-1 or j != 0) and (i != 0 or j != n-1):
        x=i
        y=j
        while x>0 and y>0:
            x-=1
            y-=1
        compteurscore=0
        compteurcasevide=0
        while x <= n-1 and y <= n-1:
            if x != i and y != j:
                if board[x][y] == player:
                    compteurscore+=1
            if board[x][y] == 0:
                compteurcasevide+=1
            x+= 1
            y+=1
        if compteurcasevide==0:
            score[player-1]+=compteurscore+1
            countstart = True
        else:
            countstart = False


    #diagonal 2
    if (i != 0 or j != 0) and (i != n - 1 or j != n - 1):
        x = i
        y = j
        while x < n-1 and y > 0:
            x +=1
            y -= 1
        compteurscore = 0
        compteurcasevide = 0
        while x >= 0 and y <= n-1:
            if x != i and y != j:
                if board[x][y] == player:
                    compteurscore += 1
            if board[x][y] == 0:
                compteurcasevide += 1
            x -= 1
            y += 1
        if compteurcasevide == 0:
            score[player - 1] += compteurscore
            if countstart == False:
                score[player-1]+= 1

def again(board,n):
    for i in range(n):
        if 0 in board[i]:
            return True
    return False
def win(score):
    if score[0]>score[1]:
        return "Player1 Won"
    elif score[1]>score[0]:
        return "Player2 Won"
    else:
        return "Draw"

def diagonal(n):
    board = newBoard(n)
    player = 1
    score = [0, 0]
    displayBoard(board,n)
    while again(board,n):
        x,y = selectSquare(board,n)
        updateBoard(board,player,x,y)
        updateScore(board,n,player,score,x,y)
        displayBoard(board,n)
        displayScore(score)
        if player==1:
            player=2
        else:
            player=1
    print(win(score))

diagonal(5)