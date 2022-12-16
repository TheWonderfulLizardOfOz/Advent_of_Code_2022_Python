import numpy


def part1():

    for i in range(len(lines)):
        lines[i] = lines[i].strip("/n").split(" -> ")
        for j in range(len(lines[i])):
            lines[i][j] = lines[i][j].split(",")
            lines[i][j][0] = int(lines[i][j][0])
            lines[i][j][1] = int(lines[i][j][1])

    for i in range(len(lines)):
        prevX = lines[i][0][0]
        prevY = lines[i][0][1]
        rockSpots.add((prevX,prevY))
        line = lines[i]
        for j in range(1, len(lines[i])):
            move = line[j]
            cX = move[0]
            cY = move[1]
            diffX = cX - prevX
            diffY = cY - prevY


            if diffX > 0:
                for i in range(prevX + 1, cX + 1):
                    rockSpots.add((i, prevY))
            elif diffX < 0:
                for i in range(cX, prevX):
                    rockSpots.add((i, prevY))

            if diffY > 0:
                for i in range(prevY + 1, cY + 1):
                    rockSpots.add((prevX, i))
            elif diffY < 0:
                for i in range(cY, prevY):
                    rockSpots.add((prevX, i))

            prevX = cX
            prevY = cY

    for rock in rockSpots:
        takenSpot.add(rock)

    sandDrop = (500, 0)
    infinityFall = False
    while not infinityFall:
        sandLoc = sandDrop
        placed = False
        for i in range(300):
            if (sandLoc[0], sandLoc[1] + 1) not in takenSpot:
                sandLoc = (sandLoc[0], sandLoc[1] + 1)
            elif (sandLoc[0] - 1, sandLoc[1] + 1) not in takenSpot:
                sandLoc = (sandLoc[0] - 1, sandLoc[1] + 1)
            elif (sandLoc[0] + 1, sandLoc[1] + 1) not in takenSpot:
                sandLoc = (sandLoc[0] + 1, sandLoc[1] + 1)
            else:
                takenSpot.add(sandLoc)
                sandSpots.add(sandLoc)
                placed = True
                break

        if placed == False:
            infinityFall = True

    return len(sandSpots)


def part2():
    largeY = 0

    for i in range(len(lines)):
        prevX = lines[i][0][0]
        prevY = lines[i][0][1]
        rockSpots.add((prevX,prevY))
        line = lines[i]
        for j in range(1, len(lines[i])):
            move = line[j]
            if move[1] > largeY:
                largeY = move[1]

    floorY = largeY + 2

    takenSpot.clear()
    sandSpots.clear()

    for rock in rockSpots:
        takenSpot.add(rock)

    for i in range(-1000, 1000):
        rockSpots.add((i, floorY))
        takenSpot.add((i, floorY))

    sandDrop = (500, 0)
    blocked = False
    while not blocked:
        sandLoc = sandDrop
        for i in range(floorY+1):
            if (sandLoc[0], sandLoc[1] + 1) not in takenSpot:
                sandLoc = (sandLoc[0], sandLoc[1] + 1)
            elif (sandLoc[0] - 1, sandLoc[1] + 1) not in takenSpot:
                sandLoc = (sandLoc[0] - 1, sandLoc[1] + 1)
            elif (sandLoc[0] + 1, sandLoc[1] + 1) not in takenSpot:
                sandLoc = (sandLoc[0] + 1, sandLoc[1] + 1)
            else:
                takenSpot.add(sandLoc)
                sandSpots.add(sandLoc)
                if sandLoc == sandDrop:
                    blocked =True
                break
    return len(sandSpots)
file = open("input.txt", "r")
lines = file.readlines()
file.close()

rockSpots = set()
sandSpots = set()
takenSpot = set()

print(part1())
print(part2())