class Node:
    def __init__(self, location, graph):
        self.location = location
        self.graph = graph

        self.children = []
        self.setChildren()


    def setChildren(self):
        x = self.location[0]
        y = self.location[1]

        if self.checkLeft():
            self.children.append((x-1, y))
        if self.checkDown():
            self.children.append((x, y+1))
        if self.checkRight():
            self.children.append((x+1, y))
        if self.checkUp():
            self.children.append((x, y-1))

    def checkLeft(self):
        x = self.location[0]
        y = self.location[1]
        lines = self.graph
        if lines[y][x] == "S":
            order = ord("a")
        else:
            order = ord(lines[y][x])
        if x == 0:
            return False
        elif lines[y][x - 1] == "E":
            return lines[y][x] == "z" or lines[y][x] == "y"
        elif lines[y][x - 1] == "S":
            return False
        elif ord(lines[y][x - 1]) - order <= 1:
            return True
        return False

    def checkDown(self):
        x = self.location[0]
        y = self.location[1]
        lines = self.graph

        if lines[y][x] == "S":
            order = ord("a")
        else:
            order = ord(lines[y][x])
        if y == len(lines) - 1:
            return False
        elif lines[y + 1][x] == "S":
            return False
        elif lines[y + 1][x] == "E":
            return lines[y][x] == "z" or lines[y][x] == "y"
        elif ord(lines[y + 1][x]) - order <= 1:
            return True
        return False

    def checkRight(self):
        x = self.location[0]
        y = self.location[1]
        lines = self.graph

        if lines[y][x] == "S":
            order = ord("a")
        else:
            order = ord(lines[y][x])
        if x == len(lines[0]) - 1:
            return False
        elif lines[y][x + 1] == "E":
            return lines[y][x] == "z" or lines[y][x] == "y"
        elif lines[y][x + 1] == "S":
            return False
        elif ord(lines[y][x + 1]) - order <= 1:
            return True
        return False

    def checkUp(self):
        x = self.location[0]
        y = self.location[1]
        lines = self.graph

        if lines[y][x] == "S":
            order = ord("a")
        else:
            order = ord(lines[y][x])
        if y == 0:
            return False
        elif lines[y - 1][x] == "E":
            return lines[y][x] == "z" or lines[y][x] == "y"
        elif lines[y - 1][x] == "S":
            return False
        elif ord(lines[y - 1][x]) - order <= 1:
            return True
        return False

def makeTree():
    tree = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            point = (x, y)
            tree[point] = Node(point, lines)
    return tree

def getRoot():
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "S":
                return x, y

def getTarget():
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "E":
                return x, y

def bfs(graph, src, dest):
    queue = []
    visited = {}
    distance = {}
    predecessor = {}
    for point in graph.keys():
        visited[point] = False
        distance[point] = 999999999
        predecessor[point] = (-1, -1)

    queue.append(src)
    visited[src] = True
    distance[src] = 0

    while (len(queue) != 0):
        u = queue.pop(0)
        for child in graph[u].children:
            if not visited[child]:
                visited[child] = True
                distance[child] = distance[u] + 1
                queue.append(child)

                if child == dest:
                    return distance[child]

def part1():
    graph = makeTree()
    root = getRoot()
    target = getTarget()
    return bfs(graph, root, target)


def part2():
    graph = makeTree()
    target = getTarget()
    aLocs = [(0, i) for i in range(len(lines))]
    distances = []
    for aLoc in aLocs:
        distances.append(bfs(graph, aLoc, target))

    return min(distances)
file = open("input.txt", "r")
lines = file.readlines()
file.close()

for i in range(len(lines)):
    lines[i] = list(lines[i].strip("\n"))


print(part1())
print(part2())