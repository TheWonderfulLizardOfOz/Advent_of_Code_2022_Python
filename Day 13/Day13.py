import functools


def part1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    packets1 = []
    packets2 = []

    for i in range(0, len(lines), 3):
        line = lines[i].strip("\n")
        line = eval(line)
        packets1.append(line)

        line = lines[i+1].strip("\n")
        line = eval(line)
        packets2.append(line)

    total = 0

    for i in range(len(packets1)):
        p1 = packets1[i]
        p2 = packets2[i]

        valid = comparisons(p1, p2)
        if valid is None:
            valid = len(p1) <= len(p2)
        print(i+1, valid)

        if valid:
            total += i + 1

    return total


def comparisons(p1, p2):
    if len(p1) == 0 and len(p2) !=0:

        return True
    elif len(p2) == 0 and len(p1) != 0:
        return False
    for i in range(min(len(p1), len(p2))):
        if type(p1[i]) == type(list()) and type(p2[i]) == type(list()):
            res = comparisons(p1[i], p2[i])
            if res is not None:
                return res
            if len(p2[i]) > len(p1[i]):
                return True

        elif type(p1[i]) != type(list()) and type(p2[i]) == type(list()):
            res = comparisons([p1[i]], p2[i])
            if res is not None:
                return res

        elif type(p1[i]) == type(list()) and type(p2[i]) != type(list()):
            res = comparisons(p1[i], [p2[i]])
            if res is not None:
                return res

        else:
            if p1[i] < p2[i]:
                return True
            elif p1[i] > p2[i]:
                return False

    if len(p1) > len(p2):
        return False

def sortCompare(p1, p2):
    result = comparisons(p1, p2)
    if result is None:
        result = len(p1) <= len(p2)

    if result:
        return 1
    elif not result:
        return -1
    else:
        return 0

def part2():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    packets = []
    divLocks = []

    for i in range(0, len(lines), 3):
        line = lines[i].strip("\n")
        line = eval(line)
        packets.append(line)

        line = lines[i+1].strip("\n")
        line = eval(line)
        packets.append(line)

    packets.append([[2]])
    packets.append([[6]])

    packets.sort(key = functools.cmp_to_key(sortCompare), reverse=True)

    for i in range(len(packets)):
        if packets[i] == [[6]] or packets[i] == [[2]]:
            divLocks.append(i+1)
    return divLocks[0]*divLocks[1]
print(part1())
print(part2())