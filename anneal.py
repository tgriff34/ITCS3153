#Group 3: Tristan Griffin, Kaifan Wei, Ryan Heavner, Jordan Hartong
import nqueens
import random
import math
import decimal

def anneal(board, T_min, alpha):
    new_board = board
    cost = new_board.numAttackingQueens()
    T = 100
    while T > T_min:
        if cost == 0:
            print "Solution board: "
            new_board.printBoard()
            print "Solution h: ", cost
            return cost

        next_board = random_neighbour(new_board.getSuccessorStates())
        new_cost = next_board.numAttackingQueens()
        delta_e = cost - new_cost
        ap = acceptance_probability(float(delta_e), T)

        if delta_e > 0 or random.random() <= ap:
            new_board = next_board
            cost = new_cost
        T = T*alpha

    print "Solution board: "
    new_board.printBoard()
    print "Solution h: ", cost
    return cost


def random_neighbour(neighbours):
    return random.choice(neighbours)


def acceptance_probability(delta_e, T):
    return decimal.Decimal(decimal.Decimal(math.e)**(decimal.Decimal(delta_e) / decimal.Decimal(T)))


print("######################################")
print("Decay rate 0.9 T Threshold 0.000001" )
print("######################################")
for i in range(0, 3):
    if i == 0: 
        print("*************")
        print("Board Size: 4")
        print("*************")
        average_h = 0
        for j in range(0, 10):
            b = nqueens.Board(4)
            b.rand()
            print "Initial board:"
            b.printBoard()
            print "Initial h value: ", b.numAttackingQueens()
            average_h = average_h + anneal(b, .000001, .9)
        print "Average h-cost of final solutions: ", average_h / 10
    elif i == 1:
        print("*************")
        print("Board Size: 8")
        print("*************")
        average_h = 0
        for j in range(0, 10):
            b = nqueens.Board(8)
            b.rand()
            print "Initial board:"
            b.printBoard()
            print "Initial h value: ", b.numAttackingQueens()
            average_h = average_h + anneal(b, .000001, .9)
        print "Average h-cost of final solutions: ", average_h / 10
    else:
        print("**************")
        print("Board Size: 16")
        print("**************")
        average_h = 0
        for j in range(0, 10):
            b = nqueens.Board(16)
            b.rand()
            print "Initial board:"
            b.printBoard()
            print "Initial h value: ", b.numAttackingQueens()
            average_h = average_h + anneal(b, .000001, .9)
        print "Average h-cost of final solutions: ", average_h / 10

print("######################################")
print("Decay rate 0.75 T Threshold 0.0000001" )
print("######################################")
for i in range(0, 3):
    if i == 0: 
        print("*************")
        print("Board Size: 4")
        print("*************")
        average_h = 0
        for j in range(0, 10):
            b = nqueens.Board(4)
            b.rand()
            print "Initial board:"
            b.printBoard()
            print "Initial h value: ", b.numAttackingQueens()
            average_h = average_h + anneal(b, .0000001, .75)
        print "Average h-cost of final solutions: ", average_h / 10
    elif i == 1:
        print("*************")
        print("Board Size: 8")
        print("*************")
        average_h = 0
        for j in range(0, 10):
            b = nqueens.Board(8)
            b.rand()
            print "Initial board:"
            b.printBoard()
            print "Initial h value: ", b.numAttackingQueens()
            average_h = average_h + anneal(b, .0000001, .75)
        print "Average h-cost of final solutions: ", average_h / 10
    else:
        print("**************")
        print("Board Size: 16")
        print("**************")
        average_h = 0
        for j in range(0, 10):
            b = nqueens.Board(16)
            b.rand()
            print "Initial board:"
            b.printBoard()
            print "Initial h value: ", b.numAttackingQueens()
            average_h = average_h + anneal(b, .0000001, .75)
        print "Average h-cost of final solutions: ", average_h / 10

print("######################################")
print("Decay rate 0.5 T Threshold 0.00000001" )
print("######################################")
for i in range(0, 3):
    if i == 0: 
        print("*************")
        print("Board Size: 4")
        print("*************")
        average_h = 0
        for j in range(0, 10):
            b = nqueens.Board(4)
            b.rand()
            print "Initial board:"
            b.printBoard()
            print "Initial h value: ", b.numAttackingQueens()
            average_h = average_h + anneal(b, .00000001, .5)
        print "Average h-cost of final solutions: ", average_h / 10
    elif i == 1:
        print("*************")
        print("Board Size: 8")
        print("*************")
        average_h = 0
        for j in range(0, 10):
            b = nqueens.Board(8)
            b.rand()
            print "Initial board:"
            b.printBoard()
            print "Initial h value: ", b.numAttackingQueens()
            average_h = average_h + anneal(b, .00000001, .5)
        print "Average h-cost of final solutions: ", average_h / 10
    else:
        print("**************")
        print("Board Size: 16")
        print("**************")
        average_h = 0
        for j in range(0, 10):
            b = nqueens.Board(16)
            b.rand()
            print "Initial board:"
            b.printBoard()
            print "Initial h value: ", b.numAttackingQueens()
            average_h = average_h + anneal(b, .00000001, .5)
        print "Average h-cost of final solutions: ", average_h / 10
