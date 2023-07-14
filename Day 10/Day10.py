def cycleCheck(cycleCount, register):
    if (cycleCount+20)%40 == 0:
        return cycleCount*register
    return 0

def clockCycle(spritePos, cycleCount):
    global pixels
    insertPos = (cycleCount)%40

    spritePos = (spritePos+1)%40 - 1
    print(spritePos, insertPos)

    if spritePos - 1 <= insertPos <= spritePos + 1:
        add = "#"
    else:
        add = "."

    pixels[insertPos] = add

    if insertPos == 39:
        result.append(pixels)
        pixels = [""]*40

def part1():
    file = open("test.txt", "r")
    lines = file.readlines()
    file.close()

    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n").split(" ")

    total = 0
    cycleCount = 1
    registerX = 1

    for line in lines:
        if line[0] == "noop":
            cycleCount += 1
            total += cycleCheck(cycleCount, registerX)
        elif line[0] == "addx":
            cycleCount += 1
            total += cycleCheck(cycleCount, registerX)
            cycleCount += 1
            registerX += int(line[1])
            total += cycleCheck(cycleCount, registerX)

    return total

def part2():
    file = open("test.txt", "r")
    lines = file.readlines()
    file.close()

    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n").split(" ")

    cycleCount = 0
    xPos = 1

    for line in lines:
        if line[0] == "noop":
            clockCycle(xPos, cycleCount)
            cycleCount += 1
        elif line[0] == "addx":
            clockCycle(xPos, cycleCount)
            cycleCount += 1
            clockCycle(xPos, cycleCount)
            cycleCount += 1
            xPos += int(line[1])

    return result

print(part1())
pixels = [""]*40
result = []
part2()
print()
for r in result:
    string = ""
    for c in r:
        string += c
    print(string)
