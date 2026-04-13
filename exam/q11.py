board = """
 {s1:^3} | {s2:^3} | {s3:^3}
-----+-----+-----
 {s4:^3} | {s5:^3} | {s6:^3}
-----+-----+-----      123
 {s7:^3} | {s8:^3} | {s9:^3}       456
                       789
"""
print(board)
"""
 {s1:^3} | {s2:^3} | {s3:^3}
-----+-----+-----
 {s4:^3} | {s5:^3} | {s6:^3}
-----+-----+-----      123
 {s7:^3} | {s8:^3} | {s9:^3}       456
                       789
"""

play = {}


def initialize_board(play):
    for n in range(9):
        play[f"s{n + 1}"] = ""


initialize_board(play)
"""
{'s1': '',
 's2': '',
 's3': '',
 's4': '',
 's5': '',
 's6': '',
 's7': '',
 's8': '',
 's9': ''}
"""
a = "{s1:} {s2:}".format(s2=1, s1=2)
a


# '2 1'
def show_board(play):
    """display the playing board.  We take a dictionary with the current state of the board
    We rely on the board string to be a global variable"""
    print(board.format(**play))


show_board(play)
"""
     |     |
-----+-----+-----
     |     |
-----+-----+-----      123
     |     |           456
                       789
"""


def get_move(n, xo, play):
    """ask the current player, n, to make a move -- make sure the square was not
    already played.  xo is a string of the character (x or o) we will place in
    the desired square"""
    valid_move = False
    while not valid_move:
        idx = input(f"player {n}, enter your move (1-9)")
        if play[f"s{idx}"] == "":
            valid_move = True
        else:
            print("invalid move")

    play[f"s{idx}"] = xo


help(get_move)


def play_game():
    """play a game of tic-tac-toe"""

    play = {}
    initialize_board(play)
    show_board(play)
