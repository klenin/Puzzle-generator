def prepareToPossibleValues(possibleValues):
    for i in range(9):
        for j in range(9):
            for k in range(1,10):
                possibleValues[i][j].append(k)
    return possibleValues

def removeAll(indexRow,indexColumn,possibleValues):
    for i in range(1,10):
        try: possibleValues[indexRow][indexColumn].remove(i)
        except ValueError:
            continue
    return possibleValues

def deleteExtraValues(puzzleSolved, possibleValues):
    for i in range(9):
        for j in range(9):
            if puzzleSolved[i][j]!=0:
                possibleValues = removeAll(i,j,possibleValues)
                for chv in range(9):
                    try: 
                        possibleValues[i][chv].remove(puzzleSolved[i][j])
                        possibleValues[chv][j].remove(puzzleSolved[i][j])
                    except ValueError:
                        continue
                firstIndexRow = 3*(i//3)                                                         #block
                firstIndexColumn = 3*(j//3)
                for chvr in range(3):
                    for chvc in range(3):
                        try: 
                            possibleValues[firstIndexRow+chvr][firstIndexColumn+chvc].remove(puzzleSolved[i][j])
                        except ValueError:
                           continue
#    for i in possibleValues:
#        print(i)
#    print("fff")
#    print(possibleValues[7][7])
    

#    for j in range(9):                                                                      #row
#        if puzzleSolved[indexRow][j]!=0:
#           try: possibleValues[indexRow][indexColumn].remove(puzzleSolved[indexRow][j])
#           except ValueError:
#                continue
#
#    for i in range(9):                                                                      #column
#        if puzzleSolved[i][indexColumn]!=0:
#           try: possibleValues[indexRow][indexColumn].remove(puzzleSolved[i][indexColumn])
#           except ValueError:
#                continue
#
#    firstIndexRow = 3*(indexRow//3)                                                         #block
#    firstIndexColumn = 3*(indexColumn//3)
#    for i in range(3):
#        for j in range(3):
#            if puzzleSolved[firstIndexRow+i][firstIndexColumn+j]!=0:
#                try: possibleValues[indexRow][indexColumn].remove(puzzleSolved[firstIndexRow+i][firstIndexColumn+j])
#                except ValueError:
#                    continue 
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
                    possibleValues = deleteExtraValues(puzzleSolved,possibleValues)
                    
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
                            indexSoughtColumn = j
                if countPlace==1:
                    puzzleSolved[i][indexSoughtColumn] = k
                    possibleValues = deleteExtraValues(puzzleSolved,possibleValues)
                    
    return puzzleSolved

def noChooseMethodBlock(puzzleSolved,possibleValues):
    for counBlock in range(9):
        for k in range(1,10):
            for i in range(3):
                for j in range(3):
                    m=0
    return puzzleSolved

def lastHeroMethod(possibleValues,puzzleSolved):
    isSmhchanged = True
    while isSmhchanged:
        isSmhchanged = False
        for i in range(9):
            for j in range(9):
                if puzzleSolved[i][j]==0:
                    if len(possibleValues[i][j])==1:
                        puzzleSolved[i][j] = possibleValues[i][j][0]
                        possibleValues = deleteExtraValues(puzzleSolved,possibleValues)
                        isSmhchanged = True
#                else:
#                   possibleValues = removeAll(i,j,possibleValues)

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
    possibleValues = deleteExtraValues(puzzleSolved,possibleValues)
    for chcr in range(2):
        puzzleSolved = lastHeroMethod(possibleValues,puzzleSolved)
        puzzleSolved = noChooseMethod(puzzleSolved,possibleValues)
        #puzzleSolved = noChooseMethodBlock(puzzleSolved,possibleValues)
    return puzzleSolved


puzzle = [
[0, 0, 5, 1, 0, 6, 0, 0, 0],
[0, 0, 0, 0, 9, 0, 0, 0, 7],
[0, 1, 0, 0, 0, 4, 3, 0, 2],
[0, 8, 0, 0, 0, 0, 0, 6, 4],
[0, 0, 0, 0, 0, 0, 2, 3, 0],
[0, 0, 0, 0, 7, 0, 0, 0, 0],
[0, 0, 0, 6, 0, 9, 0, 0, 0],
[4, 7, 0, 0, 0, 0, 0, 0, 0],
[5, 0, 3, 0, 0, 0, 9, 2, 0]
]

puzzleSolved=puzzle
puzzleSolved = Solve(puzzleSolved)
for i in puzzleSolved:
    print(i)