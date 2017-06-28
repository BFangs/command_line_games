"""practicing object orientation by making little games"""

class Board(object):
    """3x3 board"""

    def __init__(self):
        self.grid = [["-","-","-"],
                     ["-","-","-"],
                     ["-","-","-"]]

    def print_board(self):
        """printing the board"""
        print "Game status: "
        for row in self.grid:
            print "%s|%s|%s" % (row[0], row[1], row[2])

    def add_token(self, x, y):
        """adding a token user side"""
        if (0<x<4) and (0<y<4) and isinstance( x, int ) and isinstance( y, int ):
            if self.grid[-y][x-1] == "-":
                self.grid[-y][x-1] = "X"
            else:
                print "Sorry that spot is taken!"
        else:
            print "Sorry, that isn't part of the board"

    def check_board(self):
        """check if board is full"""
        for row in self.grid:
            for spot in row:
                if spot == "-":
                    return False
        return True

class Computer(object):
    """computer to make moves on board"""
