import re
import time
def part1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    noBeaconXVal = set()
    tRow = 2000000
    sensor = {}
    for line in lines:
        numbers = re.findall("-?\d+", line)
        sensor[(int(numbers[0]), int(numbers[1]))] = (int(numbers[2]), int(numbers[3]))

    for sLoc in sensor.keys():
        bLoc = sensor[sLoc]

        dx = abs(bLoc[0] - sLoc[0])
        dy = abs(bLoc[1] - sLoc[1])
        manDist = dx + dy

        if sLoc[1] - manDist <= tRow <= sLoc[1] + manDist :

            dyFromT = tRow - sLoc[1]
            noChecks = manDist - abs(dyFromT)
            noBeaconXVal.add(sLoc[0])
            for i in range(1, noChecks+1):
                noBeaconXVal.add(sLoc[0]+i)
                noBeaconXVal.add(sLoc[0]-i)
            if bLoc[1] == tRow:
                noBeaconXVal.remove(bLoc[0])
    return len(noBeaconXVal)

def inSensor(loc, sensorLocs):
    for sLoc in sensorLocs.keys():
        bLoc = sensorLocs[sLoc]
        manDist = abs(sLoc[0] - loc[0]) + abs(sLoc[1] - loc[1])
        bManDist = abs(sLoc[0] - bLoc[0]) + abs(sLoc[1] - bLoc[1])

        if manDist <= bManDist:
            return True
    return False

def part2():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    perimSurround = set()
    t = 4000000
    sensor = {}

    for line in lines:
        numbers = re.findall("-?\d+", line)
        sensor[(int(numbers[0]), int(numbers[1]))] = (int(numbers[2]), int(numbers[3]))

    for sLoc in sensor.keys():
        bLoc = sensor[sLoc]

        dx = abs(bLoc[0] - sLoc[0])
        dy = abs(bLoc[1] - sLoc[1])
        manDist = dx + dy


        for i in range(manDist):
            if 0 <= sLoc[0] + manDist - i + 1 <= t and 0 <= sLoc[1] + i <= t:
                perimSurround.add((sLoc[0] + manDist - i + 1, sLoc[1] + i))
            if 0 <= sLoc[0] + manDist - i + 1 <= t and 0 <= sLoc[1] - i <= t:
                perimSurround.add((sLoc[0] + manDist - i + 1, sLoc[1] - i))
            if 0 <= sLoc[0] - manDist + i - 1 <= t and 0 <= sLoc[1] + i <= t:
                perimSurround.add((sLoc[0] - manDist + i - 1, sLoc[1] + i))
            if 0 <= sLoc[0] - manDist + i - 1 <= t and 0 <= sLoc[1] - i <= t:
                perimSurround.add((sLoc[0] - manDist + i - 1, sLoc[1] - i))

        if 0 <= sLoc[0] <= t:
            if 0 <= sLoc[1] + manDist + 1 <= t:
                perimSurround.add((sLoc[0], sLoc[1] + manDist + 1))
            if 0 <= sLoc[1] - manDist - 1 <= t:
                perimSurround.add((sLoc[0], sLoc[1] - manDist - 1))

        if 0 <= sLoc[0] + 1 <= t and 0 <= sLoc[1] + manDist <= t:
            perimSurround.add((sLoc[0] + 1, sLoc[1] + manDist))
        if 0 <= sLoc[0] - 1 <= t and 0 <= sLoc[1] - manDist <= t:
            perimSurround.add((sLoc[0] - 1, sLoc[1] - manDist))

        for loc in perimSurround:
            if not inSensor(loc, sensor):
                return (loc[0] * 4000000) + loc[1]

        perimSurround.clear()



start = time.time()
print(part1())
end = time.time()
print(end - start)

start = time.time()
print(part2())
end = time.time()
print(end - start)