class Ship(object):
    """base ship class"""
    pass

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

class Player(object):
    """player with player's board and ship"""
    pass

class Game(object):
    """instance of gameplay"""
    player1 = None
    player2 = None
    current = None

def play(player1, player2):
    """function to instantiate a game"""
    pass
