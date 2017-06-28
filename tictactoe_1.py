import random

class Board(object):
    """should create a tic tac toe board 3x3"""

    def __init__(self):
        self.top_left = "-"
        self.top_middle = "-"
        self.top_right = "-"
        self.middle_left = "-"
        self.middle_middle = "-"
        self.middle_right = "-"
        self.bottom_left = "-"
        self.bottom_middle = "-"
        self.bottom_right = "-"

    def print_board(self):
        print "%s|%s|%s\n%s|%s|%s\n%s|%s|%s" %(self.top_left,
                                               self.top_middle,
                                               self.top_right,
                                               self.middle_left,
                                               self.middle_middle,
                                               self.middle_right,
                                               self.bottom_left,
                                               self.bottom_middle,
                                               self.bottom_right)

    def add_token(self, vertical, horizontal, ):
        if vertical=="top":
            if horizontal == "left":
                self.top_left = "X"
            elif horizontal == "middle":
                self.top_middle = "X"
            elif horizontal == "right":
                self.top_right = "X"
            else:
                print "error that is not a thing"
        elif vertical == "middle":
            if horizontal == "left":
                self.middle_left = "X"
            elif horizontal == "middle":
                self.middle_middle = "X"
            elif horizontal == "right":
                self.middle_right = "X"
            else:
                print "error that is not a thing"
        elif vertical == "bottom":
            if horizontal == "left":
                self.bottom_left = "X"
            elif horizontal == "middle":
                self.bottom_middle = "X"
            elif horizontal == "right":
                self.bottom_right = "X"
            else:
                print "error that is not a thing"
        else:
            print "error that is not a thing"

    def check_board(self):
        """check if board is full"""
        if self.top_left=="-" or self.top_middle=="-" or self.top_right=="-":
            return False
        if self.middle_left=="-" or self.middle_middle=="-" or self.middle_right=="-":
            return False
        if self.bottom_left=="-" or self.bottom_middle=="-" or self.bottom_right=="-":
            return False
        return True

    def computer_move(self):
        spaces = [top_left, top_middle, top_right,
                  middle_left, middle_middle, middle_right,
                  bottom_left, bottom_middle, bottom_right]

        move = random.choice(spaces)
        if self.move == "-":
            self.add_token

