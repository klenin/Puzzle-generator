

def prepareToPossibleValues(possibleValues):
    for i in range(9):
        for j in range(9):
            for k in range(1, 10):
                possibleValues[i][j].append(k)
    return possibleValues


def removeAll(indexRow, indexColumn, possibleValues):
    for i in range(1, 10):
        try:
            possibleValues[indexRow][indexColumn].remove(i)
        except ValueError:
            continue
    return possibleValues


def deleteExtraValues(puzzleSolved, possibleValues):

    for i in range(9):
        for j in range(9):
            if puzzleSolved[i][j] != 0:
                possibleValues = removeAll(i, j, possibleValues)
                for chv in range(9):
                    try:
                        possibleValues[i][chv].remove(puzzleSolved[i][j])
                        possibleValues[chv][j].remove(puzzleSolved[i][j])
                    except ValueError:
                        continue
                firstIndexRow = 3*(i//3)  # block
                firstIndexColumn = 3*(j//3)
                for chvr in range(3):
                    for chvc in range(3):
                        try:
                            possibleValues[firstIndexRow+chvr][firstIndexColumn +
                                                               chvc].remove(puzzleSolved[i][j])
                        except ValueError:
                            continue
    return possibleValues


def noChooseMethod(puzzleSolved, possibleValues):
    for j in range(9):
        for k in range(1, 10):
            soughtNumber = k
            for i in range(9):
                if puzzleSolved[i][j] == k:
                    soughtNumber = 0
            if soughtNumber != 0:
                countPlace = 0
                for i in range(9):
                    if countPlace < 2:
                        if soughtNumber in possibleValues[i][j]:
                            countPlace += 1
                            indexSoughtRow = i
                if countPlace == 1:
                    puzzleSolved[indexSoughtRow][j] = k
                    possibleValues = deleteExtraValues(
                        puzzleSolved, possibleValues)

    for i in range(9):
        for k in range(1, 10):
            soughtNumber = k
            for j in range(9):
                if puzzleSolved[i][j] == k:
                    soughtNumber = 0
            if soughtNumber != 0:
                countPlace = 0
                for j in range(9):
                    if countPlace < 2:
                        if soughtNumber in possibleValues[i][j]:
                            countPlace += 1
                            indexSoughtColumn = j
                if countPlace == 1:
                    puzzleSolved[i][indexSoughtColumn] = k
                    possibleValues = deleteExtraValues(
                        puzzleSolved, possibleValues)

    return puzzleSolved


def noChooseMethodBlock(puzzleSolved, possibleValues):
    for counBlock in range(9):
        for k in range(1, 10):
            for i in range(3):
                for j in range(3):
                    m = 0
    return puzzleSolved


def lastHeroMethod(possibleValues, puzzleSolved):
    isSmhchanged = True
    while isSmhchanged:
        isSmhchanged = False
        for i in range(9):
            for j in range(9):
                if puzzleSolved[i][j] == 0:
                    if len(possibleValues[i][j]) == 1:
                        puzzleSolved[i][j] = possibleValues[i][j][0]
                        possibleValues = deleteExtraValues(
                            puzzleSolved, possibleValues)
                        isSmhchanged = True

    return puzzleSolved


def Solve(puzzleSolved):
    possibleValues = [[[], [], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], [], []],
                      [[], [], [], [], [], [], [], [], []]]
    possibleValues = prepareToPossibleValues(
        possibleValues)  # fill in all values
    possibleValues = deleteExtraValues(puzzleSolved, possibleValues)
    for chcr in range(2):
        puzzleSolved = lastHeroMethod(possibleValues, puzzleSolved)
        puzzleSolved = noChooseMethod(puzzleSolved, possibleValues)

    return puzzleSolved


# easy
'''
puzzle = [
    [5, 1, 0, 0, 8, 3, 0, 0, 0],
    [3, 0, 0, 2, 0, 5, 1, 6, 0],
    [9, 7, 0, 4, 0, 0, 0, 0, 3],
    [0, 0, 7, 0, 0, 8, 9, 3, 6],
    [0, 0, 0, 0, 6, 2, 8, 0, 0],
    [6, 8, 0, 0, 0, 0, 2, 1, 7],
    [7, 6, 1, 0, 0, 0, 0, 9, 0],
    [4, 3, 9, 0, 0, 0, 7, 2, 0],
    [0, 0, 0, 0, 0, 0, 6, 4, 1]
]
'''
# middle
'''
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
'''

'''
for i in puzzleSolved:
    print(i)

for row in puzzleSolved:
    for elem in row:
        print(elem, end=' ')
    print()
'''
