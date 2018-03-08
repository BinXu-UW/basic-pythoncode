def init_game_board(game_board):
    for row in range (6):
        for col in range (7):
            game_board[row] [col] = '.'

def print_game_board (game_board):
    for row in range (6):
        for col in range (7):
            print game_board[row] [col];
    
    
def mian():
    game_board= [[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],
                 [' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],
                 [' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]

    init_game_board(game_board)
