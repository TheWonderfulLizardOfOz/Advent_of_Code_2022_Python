def setUp():
    global stackLines, operations, stacks
    file = open("test.txt", "r")
    lines = file.readlines()
    stackLines = lines[0:8]
    operations = lines[10::]

    stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

    for i in range(len(stackLines) - 1, -1, -1):
        for j in range(1, len(stackLines[i]) - 1, 4):
            if stackLines[i][j] == " ":
                continue
            stackNo = (j // 4) + 1
            stacks[stackNo].append(stackLines[i][j])

def part1():
    for op in operations:
        newOp = op.strip("\n")
        newOp = newOp.split(" ")
        fromS = int(newOp[3])
        toS = int(newOp[5])
        for i in range(int(newOp[1])):
            stacks[toS].append(stacks[fromS].pop())
    string = ""
    for s in stacks:
        string += str(stacks[s][-1])

    return string

def part2():
    for op in operations:
        newOp = op.strip("\n")
        newOp = newOp.split(" ")
        fromS = int(newOp[3])
        toS = int(newOp[5])
        for i in range(int(newOp[1]), 0, -1):
            stacks[toS].append(stacks[fromS].pop(-i))
    string = ""
    for s in stacks:
        string += str(stacks[s][-1])

    return string

stackLines = []
operations = []
stacks = {}

setUp()
print(part1())
setUp()
print(part2())