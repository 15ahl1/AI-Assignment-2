def getInput():
    with open("pathfinding_a.txt") as f:
        input = f.readlines()
        input = [x.strip() for x in input]

    outputList = []

    blankLines = [-1]
    for i in range(0, len(input)):
        if input[i] == "":
            blankLines.append(i)

    for i in range(0, len(blankLines) - 1):
        start = blankLines[i] + 1
        end = blankLines[i + 1]

        rows = end - start
        cols = len(input[start])

        tempList = []
        for i in range(0, rows):
            new = []
            for j in range(0, cols):
                new.append(input[i][j])
            tempList.append(new)

        outputList.append(tempList)

    f.close()
    return outputList

def printGrid(m):
    for row in m:
        for e in row:
            print(e, end=''),
        print()
    print()

for i in getInput():
    printGrid(i)
