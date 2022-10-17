# Rain White
# Start: 10/17/2022 2:22 AM
# Finish: 10/17/2022 3:08 AM

with open("Day3_Input", "r") as inputFile:  # Grabs data from input file and creates "lines" to store it
    lines = inputFile.readlines()
    lines = [line.rstrip() for line in lines]
    inputFile.close()

binLength = len(lines[0])  # Determines the length of a binary string
bStore = []  # Stores sum of 0 and 1, [[0_0,1_0], [0_1,1_1], [0_2,1_2]...]
E_G = ["", ""]  # ["01001","11100"]

for x in range(binLength):
    bStore.append([0, 0])

for x in range(binLength):  # Finds the least and most common bit for gamma and the least common bit for epsilon
    for i in lines:
        if int(i[x]) == 0:
            bStore[x][0] += 1
        elif int(i[x]) == 1:
            bStore[x][1] += 1

for x in range(binLength):
    if bStore[x][0] > bStore[x][1]:
        E_G[1] += "0"
        E_G[0] += "1"
    elif bStore[x][1] > bStore[x][0]:
        E_G[1] += "1"
        E_G[0] += "0"

print("Gamma rate: {0} {1}\nEpsilon rate: {2} {3}\nG * E: {4}"
      .format(E_G[1], int(E_G[1], 2), E_G[0], int(E_G[0], 2), int(E_G[0], 2)*int(E_G[1], 2)))
