def magicznyKwadrat(matrix):
    size = len(kwadrat)
    finalValue = 0
    value = 0
    isMagicSquare = True;
    for i in range(size):
        finalValue += matrix[0][i]

    for i in range(size):
        value = 0
        for j in range(size):
            value += matrix[i][j]
        if value != finalValue:
            isMagicSquare = False
            break

    value = 0
    for i in range(size):
        value += matrix[i][i]
    if finalValue != value:
        isMagicSquare = False

    if isMagicSquare:
        return "Tablica jest magicznym kwadratem!"
    else:
        return "Tablica nie jest magicznym kwadratem!"


kwadrat = [[2, 7, 6],
           [9, 5, 1],
           [4, 3, 8]]
print(magicznyKwadrat(kwadrat))