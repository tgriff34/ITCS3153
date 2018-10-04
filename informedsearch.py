#Group 3: Tristan Griffin, Jordan Hartong, Ryan Heavner, Kaifan Wei
import heapq

class Node:
    def __init__(self, value, par, g, h):  #, par
        self.value = value
        self.parent = par 
        self.g = g
        self.h = h
        self.f = g + h
        
    def get(self):
        return self.value
        
    def set(self, val):
        self.value = val
        
    def getChildren(self):
        children = []
        x = self.value[0]
        y = self.value[1]

        #BOUNDS OF GRID / 
        #CHANGE IF GRID DIMENSIONS CHANGE / 
        #BASED ON EXAMPLE GRID /
        if x+1 >= 0 and x+1 <= 8: #Number of columns
            children.append([x+1, y])
        if x-1 >= 0 and x-1 <= 8: #Number of columns
            children.append([x-1, y])
        if y+1 >= 0 and y+1 <= 7: #Number of rows 
            children.append([x, y+1])
        if y-1 >= 0 and y-2 <= 7: #Number of rows 
            children.append([x, y-1])
        return children

def main():
    #GREEDY IS BASED ON H AND A* IS BASED ON F
    typeOfSearch = raw_input("G or A?")
    grid = readGrid("text.txt")
    search(grid, typeOfSearch)
    
#expandNode
def search(grid, typeOfSearch):
    startLocation = [0, 0]
    goalLocation = [0, 0]
    openList = []
    closedList = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
           if grid[i][j] == 's':
               startLocation[0] = i
               startLocation[1] = j
           if grid[i][j] == 'g':
               goalLocation[0] = i
               goalLocation[1] = j

    startNode = Node([startLocation[0], startLocation[1]], None, 0, manhattanDistance(startLocation[0], goalLocation[0], startLocation[1], goalLocation[1])) 

    if typeOfSearch == 'G':
        heapq.heappush(openList, (startNode.h, startNode))
    else:
        heapq.heappush(openList, (startNode.f, startNode))

    while openList:
       child = heapq.heappop(openList)
       closedList.append(child[1].value)
       if typeOfSearch == 'G':
           print "Moving to parent:", child[1].value, " Has h value: ", child[1].h
       else:
           print "Moving to parent:", child[1].value, " Has f value: ", child[1].f
       print "Adding parent: ", child[1].value, " to closed list."
       x = child[1].value[0]
       y = child[1].value[1]
       if child[1].h == 0 and typeOfSearch == 'G':
           print "Found it."
           path = []
           while child[1].value != startLocation:
               path.append(child[1].value)
               child = child[1].parent
           path.append(child[1].value)
           writeGrid(grid, path[len(path) - 1], path[0], path)
           print path
           break
       elif child[1].value == goalLocation:
           print "Found it."
           path = []
           while child[1].value != startLocation:
               path.append(child[1].value)
               child = child[1].parent
           path.append(child[1].value)
           writeGrid(grid, path[len(path) - 1], path[0], path)
           print path
           break
       elif grid[x][y] == '1':
           print "	Child: ", child[1].value, " not traversable"
           None
       else:
           parent = child
           children = child[1].getChildren()
           print children
           #print "OpenList: ", openList, " ClosedList: ", closedList
           for child in children:
               if child in openList: 
                   print "	Child ", child, "already in open list"
                   None
               if child in closedList:
                   print "	Child ", child, "already in closed list"
                   None
               else:
                   print "	Adding child: ", child 
                   childNode = Node(child, parent, parent[1].g + 1, manhattanDistance(child[0], goalLocation[0], child[1], goalLocation[1]))
                   if typeOfSearch == 'G':
                       heapq.heappush(openList, (childNode.h, childNode))
                   else:
                       heapq.heappush(openList, (childNode.f, childNode))

def manhattanDistance(x_value, x_goal, y_value, y_goal):
    distance = 0
    distance += abs(x_value - x_goal) + abs(y_value - y_goal)
    return distance

def readGrid(filename): 
    l = []
    file = open(filename, "r")
    
    for x in file.readlines():
        l.append(x.split())
    return l

def writeGrid(grid, start, goal, path):
    for obj in path:
        grid[obj[0]][obj[1]] = '*'

    grid[start[0]][start[1]] = 's'
    grid[goal[0]][goal[1]] = 'g'

    f = open("path.txt", "w")
    f.writelines(' '.join(str(i) for i in j) + '\n' for j in grid)

main()
