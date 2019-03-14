from queue import PriorityQueue
import math

def getInput():
    if PHASE == 1:
        f = open("pathfinding_a.txt", "r")
    if PHASE == 2:
        f = open("pathfinding_b.txt", "r")

    input = f.readlines()
    input = [x.strip() for x in input]

    outputList = []

    blankLines = [-1]
    for i in range(0, len(input)):
        if input[i] == "":
            blankLines.append(i)
    blankLines.append(len(input))

    for i in range(0, len(blankLines) - 1):
        start = blankLines[i] + 1
        end = blankLines[i + 1]

        rows = end - start
        cols = len(input[start])

        tempList = []
        for i in range(start, end):
            new = []
            for j in range(0, cols):
                new.append(input[i][j])
            tempList.append(new)

        outputList.append(tempList)
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

    if PHASE == 2:
        if (map[y + 1][x + 1] == '_' or map[y + 1][x + 1] == 'G'):
            output.append((y + 1, x + 1))
        if (map[y + 1][x - 1] == '_' or map[y + 1][x - 1] == 'G'):
            output.append((y + 1, x - 1))
        if (map[y - 1][x + 1] == '_' or map[y - 1][x + 1] == 'G'):
            output.append((y - 1, x + 1))
        if (map[y - 1][x - 1] == '_' or map[y - 1][x - 1] == 'G'):
            output.append((y - 1, x - 1))

    return output

def printGrid(m):
    for row in m:
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
        current = frontier.get()[1]
        #print("Current: " + str(current[1]) + ", came from: " + str(cameFrom[current[1]]))
        if current == goal:
            break
        for n in getOpenSpaces(current, map, cols, rows):
            #print("Possible Space" + str(n))
            if not(n in cameFrom):
                priority = euclideanDistance(n, goal)
                #print("Position: " + str(n) + " has priority: " +str(priority))
                frontier.put((priority, n))
                cameFrom[n] = current
    path = [current]
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
    #print("Start: " + str(start))
    #print("Goal: " + str(goal))

    frontier = PriorityQueue()
    frontier.put((0, start))
    cameFrom = {}
    costSoFar = {}
    cameFrom[start] = None
    costSoFar[start] = 0

    while not frontier.empty():
        current = frontier.get()[1] #Pulling the position instead of position and priority
        #print("Current: " + str(current))
        if current == goal:
            break

        openSpaces = getOpenSpaces(current, map, cols, rows)
        #print("Open Spaces: " + str(openSpaces))
        for n in openSpaces:
            #print("Possible Space: " + str(n))
            newCost = costSoFar[current] + cost(current, n)
            if not(n in costSoFar) or (newCost < costSoFar[n]):
                costSoFar[n] = newCost
                priority = newCost + euclideanDistance(n, goal)
                #print("Position: " + str(n) + " has priority: " +str(priority))
                frontier.put((priority, n))
                cameFrom[n] = current

    path = [current]
    while(cameFrom[current] != None):
        current = cameFrom[current]
        path.insert(0, current)
    return path


def outputGrid(map, mode):
    if PHASE == 1:
        file = open("pathfinding_a_out.txt", "a")
    if PHASE == 2:
        file = open("pathfinding_b_out.txt", "a")

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

def copyMap(a):
    out = [[a[j][i] for i in range(len(a[0]))] for j in range(len(a))]
    return out


def main():
    global PHASE
    PHASE = 1
    mapInputList = getInput()
    for mapInput in mapInputList:
        aStarMap = copyMap(mapInput) #Copy of the original map
        greedyMap = copyMap(mapInput) #Copy of the original map

        colNum = len(mapInput)    #Number of Columns
        rowNum = len(mapInput[0]) #Number of Rows
        start = getStart(mapInput, colNum, rowNum) #Tuple containg Start Position
        end = getGoal(mapInput, colNum, rowNum) #Tuple containing Goal Position
        '''
        print("Original Map")
        printGrid(mapInput)
        '''
        aStarPath = aStarSearch(aStarMap, colNum, rowNum)
        #print("A* Path: " + str(aStarPath))
        #Modifying greedyMap to show the path taken by the greedy algorithm
        for p in aStarPath:
            if not((aStarMap[p[0]][p[1]] == 'G') or (aStarMap[p[0]][p[1]] == 'S')):
                aStarMap[p[0]][p[1]] = 'P'
        #print("A*")
        #printGrid(aStarMap)
        outputGrid(aStarMap, "A*")

        greedyPath = greedySearch(greedyMap, colNum, rowNum)
        #Modifying greedyMap to show the path taken by the greedy algorithm
        for p in greedyPath:
            if not((greedyMap[p[0]][p[1]] == 'G') or (greedyMap[p[0]][p[1]] == 'S')):
                greedyMap[p[0]][p[1]] = 'P'
        #print("Greedy")
        #printGrid(greedyMap)
        outputGrid(greedyMap, "Greedy")

    PHASE = 2

    mapInputList = getInput()
    for mapInput in mapInputList:
        #Makes Copies of maps

        aStarMap = copyMap(mapInput) #Copy of the original map
        greedyMap = copyMap(mapInput) #Copy of the original map

        #Info of maps
        colNum = len(mapInput)    #Number of Columns
        rowNum = len(mapInput[0]) #Number of Rows
        start = getStart(mapInput, colNum, rowNum) #Tuple containg Start Position
        end = getGoal(mapInput, colNum, rowNum) #Tuple containing Goal Position

        #Prints copy of Original Map
        print("Original Map")
        printGrid(mapInput)

        #A* calculation
        aStarPath = aStarSearch(aStarMap, colNum, rowNum)
        #print("A* Path: " + str(aStarPath))
        #Modifying greedyMap to show the path taken by the greedy algorithm
        for p in aStarPath:
            if not((aStarMap[p[0]][p[1]] == 'G') or (aStarMap[p[0]][p[1]] == 'S')):
                aStarMap[p[0]][p[1]] = 'P'
        print("A*")
        printGrid(aStarMap)
        outputGrid(aStarMap, "A*") #Outputing A*

        greedyPath = greedySearch(greedyMap, colNum, rowNum)
        #Modifying greedyMap to show the path taken by the greedy algorithm
        for p in greedyPath:
            if not((greedyMap[p[0]][p[1]] == 'G') or (greedyMap[p[0]][p[1]] == 'S')):
                greedyMap[p[0]][p[1]] = 'P'
        print("Greedy")
        printGrid(greedyMap)
        outputGrid(greedyMap, "Greedy")


main()
