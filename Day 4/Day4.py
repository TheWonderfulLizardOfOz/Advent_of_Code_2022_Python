def parse():
    file = open("test.txt", "r")
    lines = file.readlines()
    file.close()
    assignments = []

    for line in lines:
        temp = line.split(",")
        for part in temp:
            l = part.strip("\n")
            assignments.append(l)

    newA = []
    for a in assignments:
        a = a.split("-")
        a[0] = int(a[0])
        a[1] = int(a[1])
        newA.append(a)

    return newA

def part1():
    newA = parse()
    count = 0
    for i in range(0, len(newA), 2):
        if newA[i][0] >= newA[i+1][0] and newA[i][1] <= newA[i+1][1]:
            count += 1
        elif newA[i+1][0] >= newA[i][0] and newA[i+1][1] <= newA[i][1]:
            count += 1

    return count

def part2():
    newA = parse()
    count = 0
    for i in range(0, len(newA), 2):
        if newA[i][1] >= newA[i+1][0] and newA[i][0] <= newA[i+1][1]:
            count += 1
        elif newA[i+1][1] >= newA[i][0] and newA[i+1][0] <= newA[i][1]:
            count += 1
    return count

print(part1())
print(part2())
