# Rain White
# Start: 11/5/2022
# Finish:

from collections import Counter

with open("Day7_Test", "r") as inputFile:
    INPUT = inputFile.readline()
    INPUT = INPUT.split(",")
    CrabPos = [eval(i) for i in INPUT]

C = Counter(CrabPos)
Fuel = 0

for x in range(len(CrabPos)):
    temp = CrabPos[x] - C.most_common(1)[0][0]
    if CrabPos[x] - C.most_common(1)[0][0] > 0:
        Fuel += CrabPos[x] - C.most_common(1)[0][0]
        print(temp)
    elif (CrabPos[x] - C.most_common(1)[0][0]) != 0:
        Fuel += C.most_common(1)[0][0] - CrabPos[x]
        print(C.most_common(1)[0][0] - CrabPos[x])
    else:
        print(0)



print(max(CrabPos), min(CrabPos), C)


print(CrabPos)

print(Fuel)