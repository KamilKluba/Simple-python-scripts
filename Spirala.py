import math

def spirala(matrix):
    size = len(matrix)
    data = [int(0) for i in range(size * size)]
    twistedArray = [[int(0) for i in range(size)]for j in range(size)]
    iterator = 0
    arrayBound = 0

    for i in range(size):
        for j in range(size):
            data[i * size + j] = matrix[i][j]

    while arrayBound < math.ceil(size / 2):
        for i in range(arrayBound, size - arrayBound, 1): #0 -> 7
            twistedArray[i][arrayBound] = data[iterator]  #[x][0]
         #   print("->" + str(iterator))
            iterator += 1
        for i in range(arrayBound + 1, size - arrayBound, 1):   #1 -> 7
            twistedArray[size - arrayBound - 1][i] = data[iterator]        #[0][x]
           # print("\/" + str(iterator))
            iterator += 1
        for i in range(size - arrayBound - 2, arrayBound - 1, -1):       #6 -> 0
            twistedArray[i][size - arrayBound - 1] = data[iterator]  #[x][0]
          #  print("<-" + str(iterator))
            iterator += 1
        for i in range(size - arrayBound - 2, arrayBound, -1):
            twistedArray[arrayBound][i] = data[iterator]
         #   print("/\\" + str(iterator))
            iterator += 1
        arrayBound += 1

    for i in range(size):
        printRow = ""
        for j in range(size):
            if twistedArray[j][i] < 10:
                printRow += str(twistedArray[j][i]) + "  "
            else:
                printRow += str(twistedArray[j][i]) + " "
        print(printRow)





'''
kwadrat = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
'''
'''
kwadrat = [[1, 2, 3, 4, 5, 6],
           [7, 8, 9, 10, 11, 12],
           [13, 14, 15, 16, 17, 18],
           [19, 20, 21, 22, 23, 24],
           [25, 26, 27, 28, 29, 30],
           [31, 32, 33, 34, 35, 36]]
'''

kwadrat = [[1, 2, 3, 4, 5, 6, 7, 8],
           [9, 10, 11, 12, 13, 14, 15, 16],
           [17, 18, 19, 20, 21, 22, 23, 24],
           [25, 26, 27, 28, 29, 30, 31, 32],
           [33, 34, 35, 36, 37, 38, 39, 40],
           [41, 42, 43, 44, 45, 46, 47, 48],
           [49, 50, 51, 52, 53, 54, 55, 56],
           [57, 58, 59, 60, 61, 62, 63, 64]]

spirala(kwadrat)
