#Group 3: Tristan Griffin, Jordan Hartong, Ryan Heavner, Kaifan Wei
import Queue

class Node:
    def __init__(self, value, par):  #, par
        self.value = value
        self.parent = par 
        
    def get(self):
        return self.value
        
    def set(self, val):
        self.value = val
        
    def getChildren(self):
        children = []
        x = self.value[0]
        y = self.value[1]

        #BOUNDS OF GRID / CHANGE IF GRID DIMENSIONS CHANGE
        if x+1 >= 0 and x+1 <= 6:
            children.append([x+1, y])
        if x-1 >= 0 and x-1 <= 6:
            children.append([x-1, y])
        if y+1 >= 0 and y+1 <= 6:
            children.append([x, y+1])
        if y-1 >= 0 and y-2 <= 6:
            children.append([x, y-1])
        return children

def main():
    typeOfSearch = raw_input("BFS OR DFS?")
    grid = readGrid("text.txt")
    search(grid, typeOfSearch)
    
#expandNode
def search(grid, typeOfSearch):
    closedList = Queue.Queue()
    inBothLists = []
    if typeOfSearch == 'BFS':
        openList = Queue.Queue()
    else:
        openList = Queue.LifoQueue()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
           if grid[i][j] == 's':
               start = Node([i, j], None)
               openList.put(start)
               inBothLists.append(start.value)
    
    while not openList.empty():
        child = openList.get()
        closedList.put(child)
        inBothLists.append(child.value)
        print "Moving to child: ", child.value
        x = child.value[0]
        y = child.value[1]
        if grid[x][y] == 'g':
            path = []
            while child.value != start.value:
                path.append(child.value)
                child = child.parent
            path.append(child.value)
            writeGrid(grid, path[len(path) - 1], path[0], path)
            print path
            break
        elif grid[x][y] == '1':
            print "Node is non-traversable: 1"
            None
        else:
            parent = child
            print "Parent Node: ", parent.value
            children = child.getChildren()
            print children
            for child in children:
                childNode = Node(child, parent)
                if childNode.value in inBothLists:
                    print "In OpenList: ", childNode.value
                    None
                elif childNode.value in inBothLists:
                    print "In ClosedList: ", childNode.value
                    None
                else:
                    openList.put(childNode)
                    inBothLists.append(childNode.value)

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
