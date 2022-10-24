# Rain White
# Start: 10/17/2022
# Finish: 10/23/2022

import sys

bingoBoards = []  # BingoBoards[board][row][number]
numsDrawn = []  # The nums that will be drawn in "random" order, front to back
highDrawn = ''  # Highest num, that will be drawn
output = 0

with open("Day4_Input", "r") as inputFile:  # Grabs data from input file and creates "lines" to store it
    numsDrawn = inputFile.readline().split(',')
    highDrawn = len(numsDrawn)-1

    bingoBoardsUnform = inputFile.readlines()
    for x in range(int((len(bingoBoardsUnform))/6)):
        bingoBoards.append([bingoBoardsUnform[(x * 6)+1][:-1].replace('  ', ' ').strip().split(),
                            bingoBoardsUnform[(x * 6)+2][:-1].replace('  ', ' ').strip().split(),
                            bingoBoardsUnform[(x * 6)+3][:-1].replace('  ', ' ').strip().split(),
                            bingoBoardsUnform[(x * 6)+4][:-1].replace('  ', ' ').strip().split(),
                            bingoBoardsUnform[(x * 6)+5][:-1].replace('  ', ' ').strip().split()])
    inputFile.close()


def bingodump(B, D):  # (Board) : Sorts winning board and outputs sum of (unmarked nums * last drawn num)
    dump = []
    out = 0
    for r in B:
        for n in r:
            dump.append(int(n))

    dump.sort()
    dump = dump[0:dump.index(int(highDrawn)+1)]  # cuts off marked nums

    for x in dump:
        out += x
    out = out * int(D)

    return out

def bingocheck(D, output=0):  # (Recent drawn num) : Checks the rows and colums for bingos, outputs sum of unmarked nums * recent draw
    coless = []
    for board in range(len(bingoBoards)):  # board: 1 space
        for row in range(5):  # row: 2 space

            colum = []
            for columx in range(5):  # makes colum
                colum.append(bingoBoards[board][columx][row])

            # Debug VVV
            # print("First: {0} {1} {2}\nSecond: {3} {4} {5}\nDrawn: {6}".format(bingoBoards[board][row] == [highDrawn + 1] * 5, bingoBoards[board][row], [highDrawn + 1] * 5, colum == [highDrawn + 1] * 5, colum, [highDrawn + 1] * 5, D))

            if bingoBoards[board][row] == [highDrawn + 1] * 5:  # checks row for bingo
                coless = bingodump(bingoBoards[board], D)
                print("Board sum * Recent draw: {0}".format(coless))
                sys.exit(2)

            if colum == [highDrawn + 1] * 5:
                coless = bingodump(bingoBoards[board], D)  # checks colum for bingo
                print("Board sum * Recent draw: {0}".format(coless))
                sys.exit(2)


for drawn in range(len(numsDrawn)):                          # drawn: 1 space
    for board in range(len(bingoBoards)):                    # board: 2 space
        for row in range(len(bingoBoards[board])):           # row: 3 space
            for num in range(len(bingoBoards[board][row])):  # num: 4 space
                if int(bingoBoards[board][row][num]) == int(numsDrawn[drawn]):  # bingo check
                    bingoBoards[board][row][num] = highDrawn + 1  # marks numbers with the highest possible draw+1
                    bingocheck(numsDrawn[drawn], 0)
