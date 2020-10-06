
#from pole1 import Solve
import importlib


def FieldReading(name, k):
    data = []
    n = k

    for row in name:
        if row[0].isdigit():
            cols = list(map(int, row.split()))
            data.append(cols)
            puzzle[k-11] = cols
        else:
            fil2.write(row)
        k += 1
        if k % n == 0:
            break
    return data


fil = open('testing/TestFields.txt', 'r')
fil2 = open('testing/TestResults.txt', 'w')
k = 10
Nex = fil.readline()
puzzle = [[0] * 9 for i in range(9)]
module_name = 'pole1'
module = importlib.import_module(module_name)


for i in range(int(Nex)):
    res = FieldReading(fil, k)
    puzzleSolved = module.Solve(res)
    for row in puzzleSolved:
        for elem in row:
            fil2.write(str(elem) + ' ')
        fil2.write("\n")
fil.close
fil2.close
#'Testing/TestFields.txt', 'r'
