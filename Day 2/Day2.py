def day2part1():
    file = open("testCase.txt", "r")
    lines = file.readlines()
    file.close()

    bonusScores = {"X": 1, "Y": 2, "Z": 3}
    elfScores = {"A": 1, "B": 2, "C": 3}
    results = [3, 6, 0]
    total = 0

    for line in lines:
        total += bonusScores[line[2]]
        total += results[bonusScores[line[2]] - elfScores[line[0]]]


    return total

def day2part2():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    resultScores = {"X": 0, "Y": 3, "Z": 6}
    #R, P, S
    #S, R, P - 3, 1, 2
    elfScores = {"A": 1, "B": 2, "C": 3}

    total = 0

    for line in lines:
        total += resultScores[line[2]]
        if line[2] == "Y":
            total += elfScores[line[0]]
        elif line[2] == "Z":
            if line[0] == "C":
                total += 1
            else:
                total += elfScores[line[0]] + 1
        elif line[2] == "X":
            if line[0] == "A":
                total += 3
            else:
                total += elfScores[line[0]] - 1

    return total

print(day2part1())
print(day2part2())