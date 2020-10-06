def prepareToPossibleValues(possibleValues):
    for i in range(9):
        for j in range(9):
            for k in range(1,10):
                possibleValues[i][j].append(k)
    return possibleValues

def checkAll(indexRow, indexColumn, puzzleSolved, possibleValues):
    for j in range(9):                                                                      #row
        if puzzleSolved[indexRow][j]!=0:
           try: possibleValues[indexRow][indexColumn].remove(puzzleSolved[indexRow][j])
           except ValueError:
                continue

    for i in range(9):                                                                      #column
        if puzzleSolved[i][indexColumn]!=0:
           try: possibleValues[indexRow][indexColumn].remove(puzzleSolved[i][indexColumn])
           except ValueError:
                continue

    firstIndexRow = 3*(indexRow//3)                                                         #block
    firstIndexColumn = 3*(indexColumn//3)
    for i in range(3):
        for j in range(3):
            if puzzleSolved[firstIndexRow+i][firstIndexColumn+j]!=0:
                try: possibleValues[indexRow][indexColumn].remove(puzzleSolved[firstIndexRow+i][firstIndexColumn+j])
                except ValueError:
                    continue
    return possibleValues

def removeAll(indexRow,indexColumn,possibleValues):
    for i in range(1,10):
        try: possibleValues[indexRow][indexColumn].remove(i)
        except ValueError:
            continue
    return possibleValues

def noChooseMethod(puzzleSolved,possibleValues):
    for j in range(9):
        for k in range(1,10):
            soughtNumber = k
            for i in range(9):
                if puzzleSolved[i][j]==k:
                    soughtNumber = 0
            if soughtNumber!=0:
                countPlace = 0
                for i in range(9):
                    if countPlace<2:
                        if soughtNumber in possibleValues[i][j]:
                            countPlace+=1
                            indexSoughtRow = i
                if countPlace==1:
                    puzzleSolved[indexSoughtRow][j] = k
    for i in range(9):
        for k in range(1,10):
            soughtNumber = k
            for j in range(9):
                if puzzleSolved[i][j]==k:
                    soughtNumber = 0
            if soughtNumber!=0:
                countPlace = 0
                for j in range(9):
                    if countPlace<2:
                        if soughtNumber in possibleValues[i][j]:
                            countPlace+=1
                            indexSoughtColumn = i
                if countPlace==1:
                    puzzleSolved[i][indexSoughtColumn] = k
    return puzzleSolved

#def noChooseMethodBlock(puzzleSolved,possibleValues):
#    for i in range(3):
#        for k in range(1,10):
#            soughtNumber = k
#            for j in range(3):
#                
#    return puzzleSolved

def lastHeroMethod(possibleValues,puzzleSolved):
    isSmhchanged = True
    while isSmhchanged:
        isSmhchanged = False
        for i in range(9):
            for j in range(9):
                if puzzleSolved[i][j]==0:
                    possibleValues = checkAll(i,j,puzzleSolved,possibleValues) #remove extra values from block
                    if len(possibleValues[i][j])==1:
                        puzzleSolved[i][j] = possibleValues[i][j][0]
                        isSmhchanged = True
                else:
                   possibleValues = removeAll(i,j,possibleValues)
    return puzzleSolved


def Solve(puzzleSolved):
    possibleValues = [[[],[],[],[],[],[],[],[],[]],
                      [[],[],[],[],[],[],[],[],[]],   
                      [[],[],[],[],[],[],[],[],[]],
                      [[],[],[],[],[],[],[],[],[]],
                      [[],[],[],[],[],[],[],[],[]],   
                      [[],[],[],[],[],[],[],[],[]],
                      [[],[],[],[],[],[],[],[],[]],
                      [[],[],[],[],[],[],[],[],[]],   
                      [[],[],[],[],[],[],[],[],[]]]
    possibleValues = prepareToPossibleValues(possibleValues) #fill in all values
    for c in range(3): #crutch, replace with while
        puzzleSolved = lastHeroMethod(possibleValues,puzzleSolved)
        puzzleSolved = noChooseMethod(puzzleSolved,possibleValues)
#        puzzleSolved = noChooseMethodBlock(puzzleSolved,possibleValues)
    return puzzleSolved


puzzle = [
    [ 2, 4, 0, 0, 7, 0, 0, 3, 8 ],
    [ 0, 0, 0, 0, 0, 6, 0, 7, 0 ],
    [ 3, 0, 0, 0, 4, 0, 6, 0, 0 ],
    [ 0, 0, 8, 0, 2, 0, 7, 0, 0 ],
    [ 1, 0, 0, 0, 0, 0, 0, 0, 6 ],
    [ 0, 0, 7, 0, 3, 0, 4, 0, 0 ],
    [ 0, 0, 4, 0, 8, 0, 0, 8, 9 ],
    [ 8, 6, 0, 4, 0, 0, 0, 0, 0 ],
    [ 9, 1, 0, 0, 6, 0, 0, 0, 2 ]
]

puzzleSolved=puzzle
puzzleSolved = Solve(puzzleSolved)
print(puzzleSolved)