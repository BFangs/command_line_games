"""practicing object orientation by making little games"""

class Board(object):
    """3x3 board"""

    def __init__(self, grid=[["-","-","-"],
                             ["-","-","-"],
                             ["-","-","-"]]):
        self.grid = grid

    @classmethod
    def starting_board(cls, grid=[["-","-","-"],
                                  ["-","-","-"],
                                  ["-","-","-"]]):
        board = cls(grid)

    def print_board(self):
        """printing the board"""
        print "Game status: "
        for row in self.grid:
            print "%s|%s|%s" % (row[0], row[1], row[2])

    def get_board(self):
        """returning board"""
        return self.grid

    def move(self, x, y, player):
        """adding a token user side"""
        if player != "X" or player != "O":
            print "Sorry, that isn't a valid player"
            return False
        if (0<x<4) and (0<y<4) and isinstance( x, int ) and isinstance( y, int ):
            if self.grid[-y][x-1] == "-":
                self.grid[-y][x-1] = player
                return True
            else:
                print "Sorry that spot is taken!"
                return False
        else:
            print "Sorry, that isn't part of the board"
            return False

    def is_winner(self, player):
        """checking if player has won"""
        pass

    def is_full(self):
        """check if board is full"""
        for row in self.grid:
            for spot in row:
                if spot == "-":
                    return False
        return True

class Computer(object):
    """computer to make moves on board"""
    pass
