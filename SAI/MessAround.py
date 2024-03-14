import numpy

class TicTacToe:
    
    def __init__(self):
        self.table = numpy.array([[str(((x) + (y + 1))) for y in range(3)] for x in range(3)])
    
    def board(self):
        print('|'.join(self.table[y][x] for x in range(3) for y in range(3)))
    
    def playerMove(self):
        pass
    
    def checkGame(self):
        pass
    
    def Game(self):
        pass        


if 'a' == 'a':
    TTT = TicTacToe()
    TTT.board()