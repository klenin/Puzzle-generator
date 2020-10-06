from pole1 import Solve


def FieldReading(name, k):
    data = []
    n = k
    for row in name:
        cols = row.split()
        if cols[0].isdigit():
            data.append(cols)
            puzzle[k-11] = cols
        else:
            fil2.write(cols[0])
            fil2.write("\n")
        k += 1
        if k % n == 0:
            break
    return data


fil = open('TestFields.txt', 'r')
fil2 = open('TestResults.txt', 'w')
k = 10
Nex = fil.readline()
puzzle = [[0] * 9 for i in range(9)]

for i in range(int(Nex)):
    res = FieldReading(fil, k)
    puzzleSolved = Solve(res)
    for row in puzzleSolved:
        for elem in row:
            fil2.write(elem + ' ')
        fil2.write("\n")
fil.close
fil2.close
#'Testing/TestFields.txt', 'r'
