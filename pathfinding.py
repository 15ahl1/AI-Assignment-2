from queue import PriorityQueue
import math

def getInput():
    with open("pathfinding_a.txt") as f:
        input = f.readlines()
        input = [x.strip() for x in input]

    x = len(input[0])
    y = len(input)

    outputList = []
    for i in range(0, y):
        new = []
        for j in range(0, x):
            new.append(input[i][j])
        outputList.append(new)
    f.close()
    return outputList


def getStart(map, cols, rows):
    for i in range(0, cols):
        for j in range(0, rows):
            if map[i][j] == 'S':
                return(i, j)

def getGoal(map, cols, rows):
    for i in range(0, cols):
        for j in range(0, rows):
            if map[i][j] == 'G':
                return(i, j)

def getOpenSpaces(position, map, cols, rows):
    y = int(position[0])
    x = int(position[1])
    output = []
    if (x - 1 >= 0) and (map[y][x - 1] == '_' or map[y][x - 1] == 'G'):
        output.append((y, x - 1))
    if (y - 1 >= 0) and (map[y - 1][x] == '_' or map[y - 1][x] == 'G'):
        output.append((y - 1, x))
    if (x + 1 < cols) and (map[y][x + 1] == '_' or map[y][x + 1] == 'G'):
        output.append((y, x + 1))
    if (y + 1 < rows) and (map[y + 1][x] == '_' or map[y + 1][x] == 'G'):
        output.append((y + 1, x))

    return output

def printGrid(map):
    for row in map:
        for e in row:
            print(e, end=''),
        print()
    print()

def euclideanDistance(pos, goal):
    return math.sqrt(math.pow(pos[0] - goal[0], 2) + math.pow(pos[1] - goal[1], 2))

def greedySearch(map, cols, rows):
    start = getStart(map, cols, rows)
    goal = getGoal(map, cols, rows)

    print("Start: " + str(start))
    frontier = PriorityQueue()
    cameFrom = {}
    frontier.put((0, start))
    cameFrom[start] = None
    while not frontier.empty():
        current = frontier.get()
        print("Current: " + str(current[1]))
        if current[1] == goal:
            break
        for n in getOpenSpaces(current[1], map, cols, rows):
            print(n)
            if not(n in cameFrom):
                priority = euclideanDistance(n, goal)
                print("Position: " + str(n) + " has priority: " +str(priority))
                frontier.put((priority, n))
                cameFrom[n] = current
    path = [current[1]]
    while not(cameFrom[current[1]] == None):
        current = cameFrom[current[1]]
        path.insert(0, current[1])
    return path

def outputGrid(map):
    file = open("pathfinding_a_out.txt", "w+")
    for line in map:
        string = ""
        for char in line:
            string += char
        file.write(string + "\n")
    file.close()

def main():
    #Creates grid from Inputs
    map = getInput()
    colNum = len(map)    #Number of Columns
    rowNum = len(map[0]) #Number of Rows
    start = getStart(map, colNum, rowNum) #Tuple containg Start Position
    end = getGoal(map, colNum, rowNum) #Tuple containing Goal Position

    printGrid(map)
    greedyPath = (greedySearch(map, colNum, rowNum))
    for p in greedyPath:
        if not((map[p[0]][p[1]] == 'G') or (map[p[0]][p[1]] == 'S')):
            map[p[0]][p[1]] = 'P'
    printGrid(map)
    outputGrid(map)

main()
