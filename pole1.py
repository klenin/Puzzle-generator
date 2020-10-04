def prepareToPossibleValues(possibleValues):
    for i in range(9):
        for j in range(9):
            for k in range(1,10):
                possibleValues[i][j].append(k)
    return possibleValues

def checkRow(indexRow, indexColumn, puzzle, possibleValues):
    for j in range(9):
        if puzzle[indexRow][j]!=0:
           try: possibleValues[indexRow][indexColumn].remove(puzzle[indexRow][j])
           except ValueError:
                continue
    return possibleValues

def checkColumn(indexRow, indexColumn, puzzle, possibleValues):
    for i in range(9):
        if puzzle[i][indexColumn]!=0:
           try: possibleValues[indexRow][indexColumn].remove(puzzle[i][indexColumn])
           except ValueError:
                continue
    return possibleValues

def checkBlock(indexRow, indexColumn, puzzle, possibleValues):
    firstIndexRow = 3*(indexRow//3)
    firstIndexColumn = 3*(indexColumn//3)
    for i in range(3):
        for j in range(3):
            if puzzle[firstIndexRow+i][firstIndexColumn+j]!=0:
                try: possibleValues[indexRow][indexColumn].remove(puzzle[firstIndexRow+i][firstIndexColumn+j])
                except ValueError:
                    continue
    return possibleValues



def Solve(puzzle):
    puzzleSolved = puzzle
    possibleValues = [[[],[],[],[],[],[],[],[],[]],
                      [[],[],[],[],[],[],[],[],[]],   
                      [[],[],[],[],[],[],[],[],[]],
                      [[],[],[],[],[],[],[],[],[]],
                      [[],[],[],[],[],[],[],[],[]],   
                      [[],[],[],[],[],[],[],[],[]],
                      [[],[],[],[],[],[],[],[],[]],
                      [[],[],[],[],[],[],[],[],[]],   
                      [[],[],[],[],[],[],[],[],[]]]
    possibleValues = prepareToPossibleValues(possibleValues) #все варианты значений на каждую ячейку
    isSmhchanged = True
    while isSmhchanged:
        isSmhchanged = False
        for i in range(9):
            for j in range(9):
                if puzzleSolved[i][j]==0:
                    possibleValues = checkRow(i,j,puzzleSolved,possibleValues) #удалает лишние варианты заполнений ячейки из строки
                    possibleValues = checkColumn(i,j,puzzleSolved,possibleValues) #удалает лишние варианты заполнений ячейки из столбца
                    possibleValues = checkBlock(i,j,puzzleSolved,possibleValues) #удалает лишние варианты заполнений ячейки из квадрата
                    if len(possibleValues[i][j])==1:
                        puzzleSolved[i][j] = possibleValues[i][j][0]
                        isSmhchanged = True
    return puzzleSolved



puzzle = [
    [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
]

puzzleSolved = Solve(puzzle)
for i in puzzleSolved:
    print(i)

