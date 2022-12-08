def openFile():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    for i in range(len(lines)):
        lines[i] = list(lines[i].strip("\n"))

    return lines

def findVisibleTrees():
    lines = openFile()

    markedTrees = {}
    # Check left view
    for i in range(1, len(lines) - 1):
        maxInRow = lines[i][0]
        for j in range(1, len(lines[i]) - 1):
            if lines[i][j] > maxInRow:
                markedTrees[i, j] = "marked"
                maxInRow = lines[i][j]

    # check right
    for i in range(len(lines) - 2, 0, -1):
        maxInRow = lines[i][(len(lines) - 1)]
        for j in range(len(lines[i]) - 2, 0, -1):
            if lines[i][j] > maxInRow:
                markedTrees[i, j] = "marked"
                maxInRow = lines[i][j]

    # check top
    for i in range(1, len(lines[0]) - 1):
        maxInColumn = lines[0][i]
        for j in range(1, len(lines) - 1):
            if lines[j][i] > maxInColumn:
                markedTrees[j, i] = "marked"
                maxInColumn = lines[j][i]

    # check bottom
    for i in range(len(lines[0]) - 2, 0, -1):
        maxInColumn = lines[len(lines) - 1][i]
        for j in range(len(lines) - 2, 0, -1):
            if lines[j][i] > maxInColumn:
                markedTrees[j, i] = "marked"
                maxInColumn = lines[j][i]

    return markedTrees

def part1():
    lines = openFile()

    return len(findVisibleTrees()) + 2*(len(lines[0]) + len(lines) - 2)

def part2():
    markedTrees = findVisibleTrees()
    lines = openFile()

    maxMult = 0
    for tree in markedTrees.keys():
        left = 0
        right = 0
        top = 0
        bottom = 0
        height = lines[tree[0]][tree[1]]


        #left
        for i in range(tree[1] - 1, -1, -1):
            left += 1
            if lines[tree[0]][i] >= height:
                break

        #right
        for i in range(tree[1] + 1, len(lines[0])):
            right += 1
            if lines[tree[0]][i] >= height:
                break

        #top
        for i in range(tree[0] - 1, -1, -1):
            top += 1
            if lines[i][tree[1]] >= height:
                break

        #bottom
        for i in range(tree[0] + 1, len(lines)):
            bottom += 1
            if lines[i][tree[1]] >= height:
                break

        scene = left*right*top*bottom
        maxMult = max(scene, maxMult)

    return maxMult

print(part1())
print(part2())