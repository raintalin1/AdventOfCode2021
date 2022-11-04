# Rain White
# Start: 11/3/2022
# Finish: 11/4/2022

TotalDays = 256
OUTPUT = 0

with open("Day6_Input", "r") as inputFile:
    INPUT = inputFile.readline()
    INPUT = INPUT.split(",")
    FishList = [eval(fish) for fish in INPUT]

days = [0] * 9

for fish in FishList:
    days[fish] += 1

for i in range(TotalDays):
    today = i % len(days)
    days[(today + 7) % len(days)] += days[today]

print(f'Total lanternfish after {TotalDays} days: {sum(days)}')

