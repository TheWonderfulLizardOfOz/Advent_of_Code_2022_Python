import time
def day1():
    topELves = [0, 0, 0]
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    elfCal = 0

    print(lines)
    for line in lines:
        if line == "\n":
            if topELves[2] < elfCal < topELves[1]:
                topELves[2] = elfCal
            elif topELves[1] < elfCal < topELves[0]:
                topELves[2] = topELves[1]
                topELves[1] = elfCal
            elif elfCal > topELves[1]:
                topELves[2] = topELves[1]
                topELves[1] = topELves[0]
                topELves[0] = elfCal
            elfCal = 0
        else:
            elfCal += int(line)
    return sum(topELves)

print(day1())