# Rain White
# Start: 10/17/2022 12:35 AM
# Finish: 10/17/2022 2:08 AM

# 3 axis of travel: Up (decreases the depth by X units),
#                   Down (increases the depth by X units),
#                   Forward (increases the horizontal position by X units)

pos = 0
depth = 0
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
        case "up":
            depth -= unit
        case "down":
            depth += unit

print("Depth: {0} \nForward: {1}\nD * F: {2}".format(depth, pos, depth*pos))
