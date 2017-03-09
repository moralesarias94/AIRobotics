# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']
def main():
    print(search(grid, init, goal, cost))
def search(grid,init,goal,cost):
    path = 'fail'
    openList = [[0]]
    openList[0].extend(init)
    openList[0].extend([0])
    cell_to_expand = int(getSmallestG(openList))
    # expand cell, mark cell[x][3] = 1
    openList[cell_to_expand][3] = 1
    openList = expandCell(grid, openList, openList[cell_to_expand], goal)
    while(True):
        cell_to_expand = getSmallestG(openList)
        if(cell_to_expand == -1):
            break
        if(openList[cell_to_expand][1] == goal[0] and openList[cell_to_expand][2] == goal[1]):
            path = [openList[cell_to_expand][0], goal[0], goal[1]]
            break
        openList = expandCell(grid, openList, openList[cell_to_expand], goal)
    return path

def getSmallestG(openList):
    smallest = 1000
    pos = -1
    for x in range (len(openList)):
        if(int(openList[x][0])<smallest and int(openList[x][3]) == 0):
            smallest = openList[x][0]
            pos = x
    return pos

def expandCell(grid, openList, cell, goal):
    gVal = cell[0]+1
    print(cell)
    expansion = []
    for i in range(len(delta)):
        print("delta x")
        print(delta[i][0])
        print("delta y")
        print(delta[i][1])
        print("cell x")
        print(cell[1])
        print("cell y")
        print(cell[2])
        x = cell[1] + delta[x][0]
        y = cell[2] + delta[x][1]
        print(x, " ", y)

        if(0 <= x < len(grid) and 0 <= y < len(grid[x]) and not inOpenList(openList, x, y) and grid[x][y] != 1):
            expansion.append([gVal, x, y])
    openList.append(expansion)
    print(openList)
    return openList
def inOpenList(openList, x, y):
    for i in range(len(openList)):
        if(x == openList[i][1] and y == openList[i][2]):
            return True
    return False