# Rain White
# Start: 10/23/2022
# Finish:

import sys

bingoBoards = []  # BingoBoards[board][row][number]
numsDrawn = []  # The nums that will be drawn in "random" order, front to back
highDrawn = ''  # Highest num, that will be drawn
output = 0

with open("Day4_Test", "r") as inputFile:  # Grabs data from input file and creates "lines" to store it
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

bkey = len(bingoBoards)


def bingodump(B, D):  # (Board) : Sorts winning board and outputs sum of (unmarked nums * last drawn num)
    dump = []
    out = 0
    for r in B:
        for n in r:
            dump.append(int(n))

    dump.sort()
    dump = dump[0:dump.index(int(highDrawn)+1)]  # cuts off marked nums
    print(dump)

    for x in dump:
        out += x
    out = out * int(D)

    return out


def bingocheck(D, output=0):  # (Recent drawn, 0) : Checks the rows and colums for bingos, outputs sum of unmarked nums * recent draw
    coless = []
    global bkey, board
    for boardC in range(len(bingoBoards)):  # board: 1 space
        for row in range(5):  # row: 2 space

            colum = []
            # Debug VVV
            # print("First: {0} {1} {2}\nSecond: {3} {4} {5}\nDrawn: {6}".format(
            #     bingoBoards[boardC][row] == [highDrawn + 1] * 5,
            #     bingoBoards[boardC][row], [highDrawn + 1] * 5,
            #     colum == [highDrawn + 1] * 5, colum,
            #     [highDrawn + 1] * 5, D))

            for columx in range(5):  # makes colum
                colum.append(bingoBoards[boardC][columx][row])


            if (bingoBoards[boardC][row] == [highDrawn + 1] * 5) & (bkey != 1):  # checks row for bingo : removes if winning
                bingoBoards.pop(boardC)
                bkey -= 1
                board = boardC = bkey

            if (colum == [highDrawn + 1] * 5) & (bkey != 1):  # checks colum for bingo : removes if winning
                bingoBoards.pop(boardC)
                bkey -= 1
                board = boardC = bkey

            if bkey == 1:  # Checks for last board in list
                x = bingodump(bingoBoards[boardC], int(numsDrawn[drawn]))
                print("Board sum * Recent draw: {0}\n{1}".format(x, drawn))
                sys.exit(bingoBoards[boardC])



for drawn in range(len(numsDrawn)):                          # drawn: 1 space
    print(bkey)
    board=bkey
    while board > 0:                                # board: 2 space
        print("board")
        for row in range(len(bingoBoards[board])):           # row: 3 space
            print("row")
            for num in range(len(bingoBoards[board][row])):  # num: 4 space
                print("beep")
                if int(bingoBoards[board][row][num]) == int(numsDrawn[drawn]):  # bingo check
                    print("hit")
                    bingoBoards[board][row][num] = highDrawn + 1  # marks numbers with the highest possible draw+1
                print("out")
                bingocheck(int(numsDrawn[drawn]), 0)
