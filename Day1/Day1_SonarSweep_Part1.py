with open("Day1_Input", "r") as inputFile:
    lines = inputFile.readlines()
    lines = [line.rstrip() for line in lines]

output = 0
store = [0, 0]  # 0: list pointer, 1: prev entry storage

for i in lines:  #
    if int(i) > store[1]:
        output += 1
    store = [store[0] + 1, int(i)]
print(output-1)
