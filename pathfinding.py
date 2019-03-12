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
    if (map[y][x + 1] == '_' or map[y][x + 1] == 'G'):
        output.append((y, x + 1))
    if (map[y][x - 1] == '_' or map[y][x - 1] == 'G'):
        output.append((y, x - 1))
    if (map[y - 1][x] == '_' or map[y - 1][x] == 'G'):
        output.append((y - 1, x))
    if (map[y + 1][x] == '_' or map[y + 1][x] == 'G'):
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

    #print("Start: " + str(start))
    frontier = PriorityQueue()
    cameFrom = {}
    frontier.put((0, start))
    cameFrom[start] = None
    while not frontier.empty():
        current = frontier.get()
        #print("Current: " + str(current[1]) + ", came from: " + str(cameFrom[current[1]]))
        if current[1] == goal:
            break
        o = getOpenSpaces(current[1], map, cols, rows)
        for n in o:
            #print("Possible Space" + str(n))
            if not(n in cameFrom):
                priority = euclideanDistance(n, goal)
                #print("Position: " + str(n) + " has priority: " +str(priority))
                frontier.put((priority, n))
                cameFrom[n] = current[1]
    path = [current[1]]
    current = current[1]
    while(cameFrom[current] != None):
        current = cameFrom[current]
        path.insert(0, current)
    #print(path)
    return path

def cost(a, b):
    return 1

def aStarSearch(map, cols, rows):
    start = getStart(map, cols, rows)
    goal = getGoal(map, cols, rows)
    print("Start: " + str(start))
    print("Goal: " + str(goal))

    frontier = PriorityQueue()
    frontier.put((0, start))
    cameFrom = {}
    costSoFar = {}
    cameFrom[start] = None
    costSoFar[start] = 0

    while not frontier.empty():
        current = frontier.get()[1] #Pulling the position instead of position and priority
        print("Current: " + str(current))
        if current == goal:
            break
        openSpaces = getOpenSpaces(current, map, cols, rows)
        print("Open Spaces: " + str(openSpaces))
        for n in openSpaces:
            print("Possible Space: " + str(n))
            newCost = costSoFar[current] + cost(current, n)
            if not(n in costSoFar) or (newCost < costSoFar[n]):
                costSoFar[n] = newCost
                priority = newCost + euclideanDistance(n, goal)
                print("Position: " + str(n) + " has priority: " +str(priority))
                frontier.put((priority, n))
                cameFrom[n] = current

    path = [current]
    while(cameFrom[current] != None):
        current = cameFrom[current]
        path.insert(0, current)
    return path


def outputGrid(map, mode):
    file = open("pathfinding_a_out.txt", "a")
    if(mode == "Greedy"):
        file.write("Greedy\n")
    elif(mode == "A*"):
        file.write("A*\n")
    for line in map:
        string = ""
        for char in line:
            string += char
        file.write(string + "\n")
    file.write("\n")
    file.close()

def main():
    #Creates grid from Inputs
    map = getInput()
    aStarMap = map.copy() #Copy of the original map
    greedyMap = map.copy() #Copy of the original map

    colNum = len(map)    #Number of Columns
    rowNum = len(map[0]) #Number of Rows
    start = getStart(map, colNum, rowNum) #Tuple containg Start Position
    end = getGoal(map, colNum, rowNum) #Tuple containing Goal Position

    printGrid(map)

    aStarPath = aStarSearch(aStarMap, colNum, rowNum)
    print("A* Path: " + str(aStarPath))
    #Modifying greedyMap to show the path taken by the greedy algorithm
    for p in aStarPath:
        if not((aStarMap[p[0]][p[1]] == 'G') or (aStarMap[p[0]][p[1]] == 'S')):
            aStarMap[p[0]][p[1]] = 'P'
    print("A*")
    printGrid(aStarMap)
    outputGrid(aStarMap, "A*")
    printGrid(map)

    greedyPath = greedySearch(greedyMap, colNum, rowNum)
    #Modifying greedyMap to show the path taken by the greedy algorithm
    for p in greedyPath:
        if not((greedyMap[p[0]][p[1]] == 'G') or (greedyMap[p[0]][p[1]] == 'S')):
            greedyMap[p[0]][p[1]] = 'P'
    print("Greedy")
    printGrid(greedyMap)
    outputGrid(greedyMap, "Greedy")

main()
