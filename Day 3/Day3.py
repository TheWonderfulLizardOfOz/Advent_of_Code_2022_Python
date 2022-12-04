def day3Part1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    total = 0

    for line in lines:
        shared = []
        line1 = line[0:int(len(line)/2)]
        line2 = line[int(len(line)/2)::]

        for item in line1:
            if item in line2 and item not in shared:
                shared.append(item)

        for item in shared:
            if item.isupper():
                total += ord(item) - 38
            else:
                total += ord(item) - 96

    return total

def day3Part2():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    total = 0

    for i in range(0, len(lines), 3):
        line1 = lines[i]
        line2 = lines[i+1]
        line3 = lines[i+2]

        for item in line1:
            if item in line2 and item in line3:
                if item.isupper():
                    total += ord(item) - 38
                else:
                    total += ord(item) - 96
                break

    return total

print(day3Part1())
print(day3Part2())