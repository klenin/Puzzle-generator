import random

n=9

def baseBoard():
    board=[[(0) for i in range(n)] for j in range(n)]
    for i in range (n):
        for j in range (n):
            board[i][j]=int((i*(n**0.5) +i//(n**0.5) + j) % n + 1)

    return board
        
def transposed(board):
    board=[list(i) for i in zip(*board)]
    return board

def swapRowSmall(board):
    zone=random.randrange(n**0.5)
    rowFir=random.randrange(n**0.5)
    rowSec=random.randrange(n**0.5)

    while (rowFir==rowSec):
        rowSec=random.randrange(n**0.5)
        
    lineFir=int(zone*n**0.5+rowFir)
    lineSec=int(zone*n**0.5+rowSec)

    board[lineFir],board[lineSec]=board[lineSec],board[lineFir]
    return board

def swapColSmall(board):
    board=transposed(board)
    board=swapRowSmall(board)
    board=transposed(board)
    return board


def swapRowBig(board):
    zone=random.randrange(n**0.5)
    rowFir=random.randrange(n**0.5)
    rowSec=random.randrange(n**0.5)

    while (rowFir==rowSec):
        rowSec=random.randrange(n**0.5)
        
    for i in range (int(n**0.5)):
        x1=int(rowFir*n**0.5+i)
        x2=int(rowSec*n**0.5+i)
        board[x1],board[x2]=board[x2],board[x1]

    return board

def swapColBig(board):
    board=transposed(board)
    board=swapRowBig(board)
    board=transposed(board)
    return board

def mixing(board):
    variants=['board=transposed(board)',
              'board=swapRowSmall(board)',
              'board=swapColSmall(board)',
              'board=swapRowBig(board)',
              'board=swapColBig(board)']
    for i in range(n):
        func=random.randrange(len(variants))
        exec(variants[func])
        print(variants[func])
        for i in range(9):
            print(board[i])
        print()
    return board



firstBoard=baseBoard()
mixing(firstBoard)
