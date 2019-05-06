def warcaby(matrix, gracz):
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    retValue = ""
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == 1:
                if i + 1 <= 6 and j + 1 <= 6:
                    if matrix[i + 1][j + 1] == 2 and matrix[i + 2][j + 2] == 0:
                        retValue += "Biale maja bicie z " + rows[i] + str(j + 1) + " na " + rows[i + 1] + str(j + 2) + "\n"
                if i + 1 <= 6 and j - 1 >= 1:
                    if matrix[i + 1][j - 1] == 2 and matrix[i + 2][j - 2] == 0:
                        retValue += "Biale maja bicie z " + rows[i] + str(j + 1) + " na " + rows[i + 1] + str(j) + "\n"
                if i - 1 >= 1 and j - 1 >= 1:
                    if matrix[i - 1][j - 1] == 2 and matrix[i - 2][j - 2] == 0:
                        retValue += "Biale maja bicie z " + rows[i] + str(j + 1) + " na " + rows[i - 1] + str(j) + "\n"
                if i - 1 >= 1 and j + 1 <= 6:
                    if matrix[i - 1][j + 1] == 2 and matrix[i - 2][j + 2] == 0:
                        retValue += "Biale maja bicie z " + rows[i] + str(j + 1) + " na " + rows[i - 1] + str(j + 2) + "\n"

            if matrix[i][j] == 2:
                if i + 1 <= 6 and j + 1 <= 6:
                    if matrix[i + 1][j + 1] == 1 and matrix[i + 2][j + 2] == 0:
                        retValue += "Czarne maja bicie z " + rows[i] + str(j + 1) + " na " + rows[i + 1] + str(j + 2) + "\n"
                if i + 1 <= 6 and j - 1 >= 1:
                    if matrix[i + 1][j - 1] == 1 and matrix[i + 2][j - 2] == 0:
                        retValue += "Czarne maja bicie z " + rows[i] + str(j + 1) + " na " + rows[i + 1] + str(j) + "\n"
                if i - 1 >= 1 and j - 1 >= 1:
                    if matrix[i - 1][j - 1] == 1 and matrix[i - 2][j - 2] == 0:
                        retValue += "Czarne maja bicie z " + rows[i] + str(j + 1) + " na " + rows[i - 1] + str(j) + "\n"
                if i - 1 >= 1 and j + 1 <= 6:
                    if matrix[i - 1][j + 1] == 1 and matrix[i - 2][j + 2] == 0:
                        retValue += "Czarne maja bicie z " + rows[i] + str(j + 1) + " na " + rows[i - 1] + str(j + 2) + "\n"

    return retValue


szachownica = [[int(0) for j in range(8)] for i in range(8)]

szachownica[0][0] = 1;
szachownica[1][1] = 2;
#szachownica[2][2] = 1;

print(warcaby(szachownica, 1))