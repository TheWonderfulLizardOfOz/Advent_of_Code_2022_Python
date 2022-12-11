def part1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    #monkey: [[items], [operation], [test], [true, false]]
    monkeys = {}

    for i in range(0, len(lines), 7):
        monkeyNo = i//7
        monkeys[monkeyNo] = []

        itemsLine = lines[i+1].strip().strip("\n").split(":")
        itemsLine = itemsLine[1].strip()
        items = itemsLine.split(", ")
        monkeys[monkeyNo].append([int(item) for item in items])

        operationLine = lines[i+2].strip().strip("\n").split(" ")
        monkeys[monkeyNo].append([operationLine[4], operationLine[5]])

        testLine = lines[i+3].strip().strip("\n").split()
        monkeys[monkeyNo].append([int(testLine[-1])])

        trueOpt = int(lines[i+4].strip("\n").split(" ")[-1])
        falseOpt = int(lines[i+5].strip("\n").split(" ")[-1])
        monkeys[monkeyNo].append([trueOpt, falseOpt])

    inspectNo = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(20):
        for m in monkeys.keys():
            monkey = monkeys[m]
            for j in range(len(monkey[0])):
                inspectNo[m] += 1

                worryLevel = monkey[0].pop(0)

                operator = monkey[1][0]
                if monkey[1][1] == "old":
                    operand = worryLevel
                else:
                    operand = int(monkey[1][1])

                if operator == "*":
                    worryLevel *= operand
                else:
                    worryLevel += operand

                worryLevel = worryLevel//3

                if worryLevel%monkey[2][0] == 0:
                    monkeys[monkey[3][0]][0].append(worryLevel)
                else:
                    monkeys[monkey[3][1]][0].append(worryLevel)


    inspectNo.sort(reverse=True)

    return inspectNo[0]*inspectNo[1]

def part2():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    # monkey: [[items], [operation], [test], [true, false]]
    monkeys = {}
    modProd = 1

    for i in range(0, len(lines), 7):
        monkeyNo = i // 7
        monkeys[monkeyNo] = []

        itemsLine = lines[i + 1].strip().strip("\n").split(":")
        itemsLine = itemsLine[1].strip()
        items = itemsLine.split(", ")
        monkeys[monkeyNo].append([int(item) for item in items])

        operationLine = lines[i + 2].strip().strip("\n").split(" ")
        monkeys[monkeyNo].append([operationLine[4], operationLine[5]])

        testLine = lines[i + 3].strip().strip("\n").split()
        monkeys[monkeyNo].append([int(testLine[-1])])
        modProd *= int(testLine[-1])

        trueOpt = int(lines[i + 4].strip("\n").split(" ")[-1])
        falseOpt = int(lines[i + 5].strip("\n").split(" ")[-1])
        monkeys[monkeyNo].append([trueOpt, falseOpt])

        monkeys[monkeyNo].append([0])

    inspectNo = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(10000):
        for m in monkeys.keys():
            monkey = monkeys[m]
            length = len(monkey[0])
            pointer = monkey[4][0]
            operator = monkey[1][0]
            operand = monkey[1][1]
            divOp = monkey[2][0]
            trueMonkey = monkey[3][0]
            falseMonkey = monkey[3][1]

            if operand != "old":
                operand = int(operand)

            inspectNo[m] += length

            for _ in range(length):
                worryLevel = monkey[0].pop(0)

                if operand == "old":
                    if operator == "*":
                        worryLevel *= worryLevel
                    else:
                        worryLevel += worryLevel
                else:
                    if operator == "*":
                        worryLevel *= operand
                    else:
                        worryLevel += operand

                worryLevel = worryLevel%modProd

                if worryLevel % divOp == 0:
                    monkeys[trueMonkey][0].append(worryLevel)
                else:
                    monkeys[falseMonkey][0].append(worryLevel)


    inspectNo.sort(reverse=True)
    return inspectNo[0] * inspectNo[1]

    


print(part1())
print(part2())