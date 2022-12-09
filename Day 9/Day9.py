def part1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n").split(" ")

    hPos = [0, 0]
    tPos = [0, 0]
    tailVisit = {(0, 0)}

    for line in lines:
        direction = line[0]
        times = int(line[1])

        for i in range(times):
            absDistance = abs(tPos[0] - hPos[0]) + abs(tPos[1] - hPos[1])
            hPrev = hPos.copy()
            dx = abs(tPos[1] - hPos[1])
            dy = abs(tPos[0] - hPos[0])

            if direction == "L":
                hPos[1] -= 1
            elif direction == "R":
                hPos[1] += 1
            elif direction == "U":
                hPos[0] += 1
            elif direction == "D":
                hPos[0] -= 1

            newAbs = abs(tPos[0] - hPos[0]) + abs(tPos[1] - hPos[1])
            if newAbs == 0:
                continue
            if absDistance == 2 and newAbs != 1:
                tPos = hPrev.copy()

            elif absDistance != 0 and dy == 0 and direction in ["R", "L"]:
                if direction == "L":
                    tPos[1] -= 1
                elif direction == "R":
                    tPos[1] += 1

            elif absDistance != 0 and dx == 0 and direction in ["U", "D"]:
                if direction == "U":
                    tPos[0] += 1
                elif direction == "D":
                    tPos[0] -= 1

            tailVisit.add((tPos[0], tPos[1]))

    return len(tailVisit)




def part2():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    for i in range(len(lines)):
        newLine = lines[i].strip("\n").split(" ")
        lines[i] = newLine

    hPos = [0, 0]
    tPos = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    tailVisit = {(0, 0)}

    for line in lines:
        direction = line[0]
        times = int(line[1])

        for _ in range(times):
            if direction == "L":
                hPos[1] -= 1
            elif direction == "R":
                hPos[1] += 1
            elif direction == "U":
                hPos[0] += 1
            elif direction == "D":
                hPos[0] -= 1

            for i in range(len(tPos)):
                touching = False
                #check touching
                if i == 0:
                    dy = hPos[0] - tPos[i][0]
                    dx = hPos[1] - tPos[i][1]
                    if abs(dy) <= 1 and abs(dx) <= 1:
                        touching = True
                else:
                    dy = tPos[i-1][0] - tPos[i][0]
                    dx = tPos[i-1][1] - tPos[i][1]
                    if abs(dy) <= 1 and abs(dx) <= 1:
                        touching = True

                if touching == True:
                    continue
                if dx != 0:
                    dx = int(dx / abs(dx))
                if dy != 0:
                    dy = int(dy/abs(dy))

                tPos[i][0] += dy
                tPos[i][1] += dx
            tailVisit.add((tPos[-1][0], tPos[-1][1]))
    return len(tailVisit)


print(part1())
print(part2())