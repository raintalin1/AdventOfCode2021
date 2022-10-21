# Rain White
# Start: 10/17/2022 10:35 AM
# Finish: never

with open("Day3_Test", "r") as inputFile:  # Grabs data from input file and creates "lines" to store it
    lines = inputFile.readlines()
    lines = [line.rstrip() for line in lines]
    inputFile.close()

binLength = len(lines[0])
listLength = len(lines)
bStore = []  # Stores sum of 0 and 1, [[0_0,1_0], [0_1,1_1], [0_2,1_2]...]

o_Co = ["", ""]  # ["01001","11100"]


for x in range(binLength):
    bStore.append([0, 0])

print(lines)

for x in range(listLength):

    popStore = []

    for i in lines:
        if int(i[x]) == 0:
            bStore[x][0] += 1
        elif int(i[x]) == 1:
            bStore[x][1] += 1

    if bStore[x][0] > bStore[x][1]:

        for i in lines:
            if i[x] == "1":
                popStore.append(x)
                listLength -= 1
                print("{0} {1} {2} {3} {4} a".format(bStore[x], listLength, x, i, popStore))

    elif bStore[x][0] < bStore[x][1]:
        for i in lines:
            if i[x] == "0":
                popStore.append(x)
                listLength -= 1
                print("{0} {1} {2} {3} {4} b".format(bStore[x], listLength, x, i, popStore))

    for i in popStore:
        lines.pop(int(i))

    print(lines)


print(bStore)

for x in range(binLength):
    if bStore[x][0] > bStore[x][1]:
        o_Co[1] += "0"
        o_Co[0] += "1"
    elif bStore[x][1] > bStore[x][0]:
        o_Co[1] += "1"
        o_Co[0] += "0"

# print("Gamma rate: {0} {1}\nEpsilon rate: {2} {3}\nG * E: {4}"
#      .format(o_Co[1], int(o_Co[1], 2), o_Co[0], int(o_Co[0], 2), int(o_Co[0], 2)*int(o_Co[1], 2)))
