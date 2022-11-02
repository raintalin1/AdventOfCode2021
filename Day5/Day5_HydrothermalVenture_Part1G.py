# Rain White
# Start: 10/29/2022
# Finish:

from graphics import *


sizeMulti = 1
X = []
Y = []

global grid
grid = []

with open("Day5_Test", "r") as inputFile:  # Grabs data from input file and creates "input" to store it
    input = []
    for i in inputFile.readlines():
        input.append(i[:-1].replace(' -> ', ' ').replace(',', ' '))
    inputFile.close()

for i in input:  # splits input into X1 and X2 as well as Y1 and Y2 : breaks input into usable data
    split = i.split()
    if(int(split[0]) == int(split[2]) or int(split[1]) == int(split[3])):
        X.append((int(split[0]), int(split[2])))
        Y.append((int(split[1]), int(split[3])))

firstmaxxsort = list(map(max, X))
secondmaxxsort = max(firstmaxxsort)

firstmaxysort = list(map(max, Y))
secondmaxysort = max(firstmaxysort)


def pause():
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

# def drawgrid(R, )

def fillgrid(L, W):  # fills "grid" with array of 0 [][]
    for x in range(L):
       grid.append([0 for element in range(W)])

def editgrid(x, y):
    grid

def drawline(stpt, endpt):
    print("start: {0}\nend: {1}".format(stpt, endpt))
    l = Line(stpt, endpt)
    l.draw(win)



def main():
    global win
    win = GraphWin("Day 5 HydroThermal Venture", (secondmaxxsort*sizeMulti)+50, (secondmaxysort*sizeMulti)+50)

    fillgrid(secondmaxxsort,secondmaxysort)

    for x in range(len(X)):
        drawline(Point(X[x][0]*sizeMulti, Y[x][0]*sizeMulti), Point(X[x][1]*sizeMulti, Y[x][1]*sizeMulti))

    pause()

main()
