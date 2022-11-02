# Rain White
# Start: 10/29/2022
# Finish:

X = []
Y = []

global grid
grid = []

with open("Day5_Test", "r") as inputFile:  # Grabs data from input file and creates "input" to store it
    input = []
    for i in inputFile.readlines():
        input.append(i[:-1].replace(' -> ', ' ').replace(',', ' '))
    inputFile.close()

for i in input:  # Splits input into X1 and X2 as well as Y1 and Y2 : breaks input into usable data
    split = i.split()
    if (int(split[0]) == int(split[2]) or int(split[1]) == int(
            split[3])):  # Formats lines so no diagonal lines go through
        X.append((int(split[0]), int(split[2])))
        Y.append((int(split[1]), int(split[3])))

firstmaxxsort = list(map(max, X))
secondmaxxsort = max(firstmaxxsort)  # Gets max num that'll be used : X

firstmaxysort = list(map(max, Y))
secondmaxysort = max(firstmaxysort)  # Gets max num that'll be used : Y


def fillgrid(L, W):  # Fills "grid" with array of 0 [][]
    for x in range(L):
        grid.append([0 for element in range(W)])


def IncreaseNum(x, y):  # Increases grid[x][y] number by one until number hits 2
    if grid[y][x] < 2:
        grid[y][x] += 1

def Linez(x1, x2, y1, y2, P):  # X1, X2, Y1, Y2, Pointer
    print(x1, x2, y1, y2, range(y1, y2), range(x1, x2))
    if x1 == x2:
        if y1 > y2:
            for y in range(y1, y2, -1):
                print(y)
                IncreaseNum(x1, y)
        elif y1 < y2:
            for y in range(y1, y2):
                print(y)
                IncreaseNum(x1, y)

    elif y1 == y2:
        if x1 > x2:
            for x in range(x1, x2, -1):
                print(x)
                IncreaseNum(x, y1)
        elif x1 < x2:
            for x in range(x1, x2):
                print(x)
                IncreaseNum(x, y1)

    elif (x1 == x2)&(y1 == y2):
        print("owo")



def main():
    fillgrid(secondmaxxsort+1, secondmaxysort+1)
    for x in range(len(X)):
        print(x)
        Linez(X[x][0], X[x][1], Y[x][0], Y[x][1], x)

    for x in range(len(grid)):
        print(grid[x])

    print()


main()
