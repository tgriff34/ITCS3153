#Tristan Griffin - Sep 12, 2018 - ITCS 3153

from random import randint

def readGrid(filename):
    l = []
    f = open(filename, "r")
    for x in f.readlines():
        l.append(x.split())
    return l

def writeGrid(filename, grid):
    f = open(filename, "w")
    f.writelines(' '.join(str(i) for i in j) + '\n' for j in grid)

def modifyGrid(grid, location, value):
    grid[location[0]][location[1]] = value

def findAllFreeLocs(grid):
    freeLocs = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '0':
                freeLocs.append([i, j])
    return freeLocs

def main():
    #Read grid
    grid = readGrid("text.txt")
    print grid

    #Locate 0's
    freeLocs = findAllFreeLocs(grid)
    #Foreach free loc place random num
    for loc in freeLocs:
        modifyGrid(grid, loc, randint(2, 9))
    print grid
    
    #Write to file
    writeGrid("writefile.txt", grid)
main()
