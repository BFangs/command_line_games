import random
import sys
import doctest


class Ship(object):
    """base ship class"""
    _length = 0
    name = ""
    coords = []

    def __init__(self):
        assert self._length > 0 and self.name

        self.hits = 0
        self.coords = []

    def is_sunk(self):
        return self.hits == self._length

    def place(self, col, row, direction):
        """Place ship.

        Given a row and column and direction, determine coordinates
        ship will occupy and update it's coordinates property.

        Raises an exception for an illegal direction.

        This is meant to be an abstract class--you should subclass it
        for individual ship types.

            >>> class TestShip(Ship):
            ...     _length = 3
            ...     name = "Test Ship"

        Let's make a ship and place it:

            >>> ship = TestShip()

            >>> ship.place(1, 2, "H")
            >>> ship.coords
            [(1, 2), (2, 2), (3, 2)]

            >>> ship.place(1, 2, "V")
            >>> ship.coords
            [(1, 2), (1, 3), (1, 4)]

        Illegal directions raise an error:

            >>> ship.place(1, 2, "Z")
            Traceback (most recent call last):
            ...
            ValueError: Illegal direction
        """
        self.coords = []
        for x in xrange(self._length):
            if direction.upper() == "H":
                self.coords.append((col + x, row))
            elif direction.upper() == "V":
                self.coords.append((col, row + x))
            else:
                raise ValueError("Illegal direction")


class AircraftCarrier(Ship):
    _length = 5
    name = "Aircraft Carrier"


class Destroyer(Ship):
    _length = 2
    name = "Destroyer"


class Submarine(Ship):
    _length = 3
    name = "Submarine"


class Battleship(Ship):
    _length = 4
    name = "Battleship"

SHIP_TYPES = [AircraftCarrier, Battleship, Submarine, Destroyer]


class Player(object):
    """player with player's board and ship"""
    name = ""
    opponent = None

    _board = None
    _ships = None

    def __init__(self, name):
        """Create player:

        - set up their board
        - set up their (empty initially) list of ships

        Let's create a player:

            >>> player = Player('Jane')

        They should have an empty board:

            >>> player._board   # doctest: +NORMALIZE_WHITESPACE
            [[False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False]]

        THey should have no ships:

            >>> player._ships
            []

        They should have no opponent (yet!):

            >>> player.opponent is None
            True

        """

        self.name = name
        self._board = []
        for row in range(10):
            self._board.append([False] * 10)
        self._ships = []

    def place_ship(self, ship, col, row, direction):
        """Place a ship on the board at col, row, going in direction.

        :col: 0-based column
        :row: 0-based row
        :direction: "H" or "V"

        LEt's create a player and place a ship:

            >>> player = Player('Jane')
            >>> destroyer = Destroyer()
            >>> player.place_ship(destroyer, 1, 2, "V")

        Did it place the destroyer on all the cells for it?

            >>> player._board[1][2] is destroyer
            True
            >>> player._board[1][3] is destroyer
            True

        Did it get the coordinates right?

            >>> destroyer.coords
            [(1, 2), (1, 3)]

        Is the destroyer the only ship in their player's arsenal?

            >>> player._ships == [destroyer]
            True
        """
        ship.place(col, row, direction)
        for col, row in ship.coords:
            if self._board[col][row]:
                raise ValueError("already taken")
            else:
                self._board[col][row] = ship
        self._ships.append(ship)

    def place_ships(self):
        """Place a ship on the board at col, row, going in direction.

        :col: 0-based column
        :row: 0-based row
        :direction: "H" or "V"

        LEt's create a player and place a ship:

            >>> player = Player('Jane')
            >>> destroyer = Destroyer()
            >>> player.place_ship(destroyer, 1, 2, "V")

        Did it place the destroyer on all the cells for it?

            >>> player._board[1][2] is destroyer
            True
            >>> player._board[1][3] is destroyer
            True

        Did it get the coordinates right?

            >>> destroyer.coords
            [(1, 2), (1, 3)]

        Is the destroyer the only ship in their player's arsenal?

            >>> player._ships == [destroyer]
            True
        """
        for ship in SHIP_TYPES:
            while True:
                try:
                    place = raw_input("\nPlace your %s (col row H/V, '00H')>" % ship.name)
                    col = int(place[0])
                    row = int(place[1])
                    direction = place[2].upper()
                    self.place_ship(ship(), col, row, direction)
                    print self.show_board(show_hidden=True)
                    break
                except:
                    print "\nWrong input: try again"
            print "\nDone!\n"

    def show_board(self, show_hidden=False):
        """Print out board:

        _ = missed here
        * = hit here
        # = destroyed ship here
        . = nothing here
        ELSE = first letter of ship type hidden here

        If `show_hidden` is False, hidden ships are shown as nothing-here.
        This is the view shown to opponents.

        If `tight` is True, skip some of the space in the board
        (good for tests and smaller screens)

        So we can see this, let's create a player and make a few
        shots:

            >>> player = Player('Jane')
            >>> destroyer = Destroyer()
            >>> player._board[1][2] = destroyer
            >>> player._board[1][3] = destroyer
            >>> player._board[0][0] = "_"  # miss
            >>> player._board[1][2] = "*"  # hit

        Here's what the opponent should see:

            >>> player.show_board()  # doctest: +NORMALIZE_WHITESPACE
              0 1 2 3 4 5 6 7 8 9
            0 _ . . . . . . . . .
            1 . . . . . . . . . .
            2 . * . . . . . . . .
            3 . . . . . . . . . .
            4 . . . . . . . . . .
            5 . . . . . . . . . .
            6 . . . . . . . . . .
            7 . . . . . . . . . .
            8 . . . . . . . . . .
            9 . . . . . . . . . .

        The player can see their own ships:

            >>> player.show_board(show_hidden=True
            ...     ) # doctest: +NORMALIZE_WHITESPACE
              0 1 2 3 4 5 6 7 8 9
            0 _ . . . . . . . . .
            1 . . . . . . . . . .
            2 . * . . . . . . . .
            3 . D . . . . . . . .
            4 . . . . . . . . . .
            5 . . . . . . . . . .
            6 . . . . . . . . . .
            7 . . . . . . . . . .
            8 . . . . . . . . . .
            9 . . . . . . . . . .

        """
        print " ",
        for coli in range(10):
            print "%s" % coli,
        print

        for rowi in range(10):

            # Print row numbers across left
            print rowi,

            # Print cells
            for coli in range(10):
                ship = self._board[coli][rowi]

                if ship == "*":
                    print "*",

                elif ship == "#":
                    print "#",

                elif ship == "_":
                    print "_",

                elif not ship or not show_hidden:
                    # Square is empty OR is enemy ship & you can't see it yet
                    print ".",

                else:
                    # Cell has ship and you're allowed to see it
                    print "%s" % ship.name[0],
            print ""

    def handle_shot(self, col, row):
        """Handle being shot at at col, row.

        If the shot is in an already-tried spot:
        - raise ValueError("You've already played there")

        If the shot misses:
         - update the board to show '_' for that cell

        Else, If the shot hits a ship:
        - update the board to '*' for that cell
        - update the ship's hits
        - check to see if it's destroyed
        - report a hit

        If the shot destroys a ship:
        - update ALL the ship's coordinates to '#'
        - report the sunk ship

        Let's create a player and add a ship:

            >>> player = Player('Jane')
            >>> destroyer = Destroyer()
            >>> player._board[1][2] = destroyer
            >>> player._board[1][3] = destroyer

        Handle misses:

            >>> player.handle_shot(0, 0)
            Miss

            >>> player.handle_shot(0, 0)
            Traceback (most recent call last):
            ...
            ValueError: You've already played there

        Handle hits:

            >>> player.handle_shot(1, 2)
            Hit!

            >>> player.handle_shot(1, 2)
            Traceback (most recent call last):
            ...
            ValueError: You've already played there


        Handle sinking things:

            >>> player.handle_shot(1, 3)
            Hit!
            You sunk my Destroyer
        """
        ship = self._board[col][row]
        if not ship:
            self._board[col][row] = "_"
            print "Miss"
        elif isinstance(ship, Ship):
            ship.hits += 1
            print "Hit!"
            self._board[col][row] = "*"
            if ship.is_sunk():
                for col, row in ship.coords:
                    self._board[col][row] = "#"
                print "You sunk my " + ship.name
        else:
            raise ValueError("You've already played there")

    def is_dead(self):
        """Is player dead (out of ships)?

            >>> player = Player('Jane')

        Since they have no placed ships, they're technically dead:

            >>> player.is_dead()
            True

        Let's place some ships:

            >>> destroyer = Destroyer()
            >>> player.place_ship(destroyer, 1, 2, "V")
            >>> player.is_dead()
            False

        And we'll hit a ship:

            >>> player.handle_shot(1, 2)
            Hit!

            >>> player.is_dead()
            False

        And destroy it (and it's their only ship, too1)

            >>> player.handle_shot(1, 3)
            Hit!
            You sunk my Destroyer

            >>> player.is_dead()
            True
        """
        for ship in self._ships:
            if not ship.is_sunk():
                return False
        return True


class Game(object):
    """instance of gameplay"""
    player1 = None
    player2 = None
    player = None

    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.player1.opponent = self.player2
        self.player2.opponent = self.player1

    def pick_start_player(self):
        self.player = random.choice([self.player1, self.player2])

    def setup_ships(self):
        for i in range(2):
            print "=" * 60
            print "%s: Place your ships (%s, turn away!)" % (
                self.player.name, self.player.opponent.name)
            self.player.place_ships()
            raw_input("\nPress ENTER to switch players >")
            print "\n" * 80  # scroll private stuff off screen
            self.player = self.player.opponent

    def play(self):
        while True:
            print
            print "=" * 40
            print "\n%s, let's attack %s\n" % (
                self.player.name, self.player.opponent.name)
            self.player.opponent.show_board()
            while True:
                try:
                    move = raw_input("\nMove (col row, e.g. '00') >")
                    col = int(move[0])
                    row = int(move[1])
                    print
                    self.player.opponent.handle_shot(col, row)
                    break
                except (ValueError, IndexError) as e:
                    print "\n(%s: try again)" % e
            print
            self.player.opponent.show_board()
            if self.player.opponent.is_dead():
                break
            self.player = self.player.opponent
        print "\n *** YOU WIN!"

def play(player1_name, player2_name):
    game = Game(player1_name, player2_name)
    game.pick_start_player()
    print "\n\n*** HACKBRIGHT BATTLESHIP: %s vs %s ***" % (
        game.player.name, game.player.opponent.name)
    print """
Battleship is played on a 10x10 grid. Each player has a separate,
secret board. Your goal is to sink your opponent's ships before
she sinks yours.

Each player will place their four ships secretly. To place a ship,
you'll be prompted for a location. Enter it like '12H', where that is
the column=1, the row=2, and going horizontally ("V" for vertically).

"""
    game.setup_ships()

    print """
How, play begins. On your turn, you'll be shown your opponent's board.
Enter coordinates for an attack on your opponent. Enter it like "12",
where column=1 and row=2.

You will receive a report on whether you missed, hit a ship, or
sunk a ship.
"""
    game.play()

    print """
That was fun! Let's play again soon!
"""
