def part1():
    file = open("input.txt", "r")
    data = file.readline()
    file.close()

    packets = ["", "", "", ""]
    count = 0
    for c in data:
        count += 1

        if count > 7:
            share = False
            for i in range(len(packets)):
                if packets[i] in packets[i+1::]:
                    share = True

            if not share:
                print(c)
                return count - 1

        packets.append(c)
        packets.pop(0)

    return -1

def part2():
    file = open("input.txt", "r")
    data = file.readline()
    file.close()

    packets = [""]*14
    count = 0
    for c in data:
        count += 1

        if count > 7:
            share = False
            for i in range(len(packets)):
                if packets[i] in packets[i + 1::]:
                    share = True

            if not share:
                print(c)
                return count - 1

        packets.append(c)
        packets.pop(0)

    return -1

print(part1())
print(part2())