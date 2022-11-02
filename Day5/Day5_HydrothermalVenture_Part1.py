# Rain White
# Start: 10/29/2022
# Finish:

X = []
Y = []

with open("Day5_Test", "r") as inputFile:  # Grabs data from input file and creates "input" to store it
    input = []
    for i in inputFile.readlines():
        input.append(i[:-1].replace(' -> ', ' ').replace(',', ' '))
    inputFile.close()

for i in input:  # splits input into X1 and X2 as well as Y1 and Y2 : breaks input into usable data
    split = i.split()
    X.append((int(split[0]), int(split[2])))
    Y.append((int(split[1]), int(split[3])))

firstmaxxsort = list(map(max, X))
secondmaxxsort = max(firstmaxxsort)

firstmaxysort = list(map(max, Y))
secondmaxysort = max(firstmaxysort)

def fillgrid(L, W):  # fills "grid" with array of 0 [][]
    for x in range(L):
       grid.append([0 for element in range(W)])

def editgrid(x, y):
    grid

def main():
    print("X: ",X, "\nY: ",Y)


main()
