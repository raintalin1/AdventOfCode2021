# Rain White
# Start:
# Finish:

with open("Day7_Test", "r") as inputFile:
    INPUT = inputFile.readline()
    INPUT = INPUT.split(",")
    List = [eval(i) for i in INPUT]

Length = len(List)
mean = 0

for x in range (Length):
    mean += List[x]

print(mean/Length)


print(List)