# Rain White
# Start: 10/17/2022
# Finish: 10/17/2022

output = 0
store = [0, 0]  # 0: list pointer, 1: prev entry storage
triStore = []  # (n*2): a storage

with open("Day1_Input", "r") as inputFile:  # Grabs data from input file and creates "lines" to store it
    lines = inputFile.readlines()
    lines = [line.rstrip() for line in lines]
    inputFile.close()

for i in lines:  # Divides "lines" into ABC sums to be compared
    try:
        a = int(lines[store[0]]) + int(lines[store[0] + 1]) + int(lines[store[0] + 2])
        triStore.append(a)
        store = [store[0] + 1, 0]

    except:
        print("Overflow!!!")

store = [0, 0]
print(triStore)
for i in triStore:  #compares current int > prev int, adds +1 to output if true
    if int(i) > store[1]:
        output += 1
    print(store, i)
    print(int(i) > store[1])
    store = [store[0] + 1, int(i)]

print(output-1)
