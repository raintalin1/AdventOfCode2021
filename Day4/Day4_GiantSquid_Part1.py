# Rain White
# Start: 10/17/2022
# Finish:

bingoBoards = []  # BingoBoards[board][row][number]
numsDrawn = []  # The nums that will be drawn in "random" order, front to back
highDrawn = ''  # Highest num, that will be drawn
output = []

with open("Day4_test", "r") as inputFile:  # Grabs data from input file and creates "lines" to store it
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


def bingocheck():
    for board in range(len(bingoBoards)):  # board: 1 space
        for row in range(5):  # row: 2 space

            colum = []
            for columx in range(5):
                colum.append(bingoBoards[board][columx][row])

            if bingoBoards[board][row] == [[highDrawn + 1] * 5]:
                output =


bingocheck()

# for drawn in range(len(numsDrawn)):                          # drawn: 1 space
#     for board in range(len(bingoBoards)):                    # board: 2 space
#         for row in range(len(bingoBoards[board])):           # row: 3 space
#             for num in range(len(bingoBoards[board][row])):  # num: 4 space
#                 if int(bingoBoards[board][row][num]) == int(numsDrawn[drawn]):  # bingo check
#                     bingoBoards[board][row][num] = highDrawn + 1
