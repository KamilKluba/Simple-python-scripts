def sudoku(matrix, tileWidth, tileHeight):
    size = len(matrix)
    finalValue = True
    fullSquareValue = [False for i in range(size)]
    tileValue = [False for i in range(tileHeight * tileWidth)]

    for i in range(size):
        fullSquareValue = [False for k in range(size)]
        for j in range(size):
            fullSquareValue[matrix[i][j] - 1] = True
        for j in range(size):
            if fullSquareValue[j] == False:
                finalValue = False

        fullSquareValue = [False for k in range(size)]
        for j in range(size):
            fullSquareValue[matrix[j][i] - 1] = True
        for j in range(size):
            if fullSquareValue[j] == False:
                finalValue = False

    for i in range(0, size, tileWidth):
        for j in range(0, size, tileHeight):
            for k in range(tileWidth):
                for l in range(tileHeight):
                    tileValue[matrix[j + l][i + k] - 1] = True
            for k in range(tileHeight * tileWidth):
                if tileValue[k] == False:
                    finalValue = False

    if finalValue:
        return "Sudoku jest poprawne!"
    else:
        return "Sudoku nie jest poprawne!"


kwadrat = [[6, 5, 0, 3, 4, 2],
           [4, 3, 2, 1, 6, 5],
           [2, 4, 6, 5, 1, 3],
           [5, 1, 3, 4, 2, 6],
           [1, 2, 5, 6, 3, 4],
           [3, 6, 4, 2, 5, 1]]
print(sudoku(kwadrat, 2, 3))


