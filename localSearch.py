import queens

#def simulatedAnneal(board, schedule):
    

def main():
    T = .000001
    decay_rate = .9
    temperature = T * decay_rate

    board = queens.Board(8)
    board.rand()
    #simulatedAnneal(board, temperature) 
    print board.getSuccessorStates()
    print board.numAttackingQueens()

main()
