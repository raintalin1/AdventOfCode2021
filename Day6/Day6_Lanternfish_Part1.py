# Rain White
# Start: 11/2/2022
# Finish: 11/2/2022

FishList = []
FinalDay = 80
OUTPUT = 0

with open("Day6_Input", "r") as inputFile:
    INPUT = inputFile.readline()
    INPUT = INPUT.split(",")
    FishList = [eval(fish) for fish in INPUT]


for x in range(FinalDay):
    for x in range(len(FishList)):
        if FishList[x] == 0:
            FishList.append(8)
            FishList[x] = 7
        FishList[x] -= 1

print("Total of Lanternfish:", len(FishList))
