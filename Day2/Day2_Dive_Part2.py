# Rain White
# Start: 10/17/2022 2:10 AM
# Finish: 10/17/2022 2:16 AM

# 3 axis of travel: Up (decreases the aim by X units),
#                   Down (increases the aim by X units),
#                   Forward (increases the horizontal position by X units AND increases the depth by aim*X)


pos = 0
depth = 0
aim = 0
splitList = []

with open("Day2_Input", "r") as inputFile:  # Grabs data from input file and creates "lines" to store it
    lines = inputFile.readlines()
    lines = [line.rstrip() for line in lines]
    inputFile.close()

for i in lines:
    splitList.append(i.split())

for i in splitList:  # i[0]: direction, i[1]: unit
    unit = int(i[1])
    match i[0]:
        case "forward":
            pos += unit
            depth += (aim*unit)
        case "up":
            aim -= unit
        case "down":
            aim += unit

print("Forward: {0}\nDepth: {1}\nD * F: {2}".format(pos, depth, depth*pos))
