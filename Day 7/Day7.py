def calculateSizes():
    file = open("test.txt", "r")
    lines = file.readlines()
    file.close()

    parentStack = []
    sizes = {}
    fileLocations = {"/.0": 0}
    sizes[0] = 0
    totalSize = 0

    for i in range(len(lines)):
        splitLine = lines[i].strip("\n").split(" ")
        if splitLine[1] == "cd" and splitLine[2] != "..":
            if parentStack == []:
                p = "0"
            else:
                p = str(parentStack[-1])
            parentStack.append(fileLocations[splitLine[2] + "." + p])
        elif splitLine[1] == "cd" and splitLine[2] == "..":
            parentStack.pop(-1)
        elif splitLine[0] == "dir":
            sizes[i] = 0
            fileLocations[splitLine[1] + "." + str(parentStack[-1])] = i
        elif splitLine[0].isdigit():
            value = int(splitLine[0])
            totalSize += value
            for index in parentStack:
                sizes[index] += value

    return sizes, totalSize

def part1():
    total = 0
    for dir in sizes.keys():
        if sizes[dir] <= 100000:
            total += sizes[dir]

    return total

def part2():
    small = 99999999999
    freeSpace = 70000000 - totalSize
    spaceNeeded = 30000000 - freeSpace

    for dir in sizes.keys():
        if spaceNeeded <= sizes[dir] < small:
            small = sizes[dir]
    return small

(sizes, totalSize) = calculateSizes()
print(totalSize)
print(part1())
print(part2())