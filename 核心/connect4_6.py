# This is the start of our Connect 4 game. We started by first defining
# the playing board as a list of lists (seen in main ()). We have finished
# the definitions for initializing the game board to '.' and printing out the
# game board. We also have in place the ability to check for vertical or
# horizontal connect 4.

def init_game_board (game_board):
    for row in range (6):
        for col in range (7):
            game_board[row][col] = '.'

def print_game_board (game_board):
    for row in range (6):
        for col in range (7):
            print game_board[row][col] + " ",
        print '\n'

def get_column ():
    column = input ("Enter column number: ")
    return column

def place_token (column, game_board, token_color):
    row = 5
    while game_board[row][column] != '.':
        row = row - 1

    game_board[row][column] = token_color

# Added 3/24/10
def check_vertical_win (column, game_board, token_color):
    row = 0
    while game_board[row][column] == '.':
        row = row + 1
    
    number_in_col = 0
    winner = 0
    if row <= 2:
        while row <= 5 and game_board[row][column] == token_color:
            row = row + 1
            number_in_col = number_in_col + 1
            
        if number_in_col == 4:
            winner = 1

    return winner

# Added 3/31/10
def check_horizontal_win (column, game_board, token_color):
    row = 0
    while game_board [row][column] == ".":
        row= row +1
    winner =0
    column =0
    while game_board[row][column]!= token_color:
        column = column +1
    while column<=3 and winner != 1:
        if game_board [row][column+0] == token_color and game_board [row][column+1] == token_color and game_board [row][column+2] == token_color and game_board [row][column+3] == token_color:
            winner = 1
        else:
            column = column +1
    return winner

# Completed 4/7/10
def check_diagonal_win (column, game_board, token_color):
    row = 0
    while game_board[row][column] == '.':
        row = row + 1
    original_row = row
    original_col = column

    # down left
    count = 0
    winner = 0
    while row <= 5 and column >= 0 and game_board[row][column] == token_color:
        count = count + 1
        row = row + 1
        column = column - 1
    if count >= 4:
        winner = 1
    else: # up right
        column = original_col + 1
        row = original_row - 1
        while row >= 0 and column <= 6 and game_board[row][column] == token_color:
            count = count + 1
            row = row - 1
            column = column + 1
        if count >= 4:
            winner = 1 
        else: # down right
            count = 0
            winner = 0
            row = original_row
            column = original_col
            while row <= 5 and column <= 6 and game_board[row][column] == token_color:
                count = count + 1
                row = row + 1
                column = column + 1
            if count >= 4:
                winner = 1
            else: # up left
                column = original_col - 1
                row = original_row - 1
                while row >= 0 and column >= 0 and game_board[row][column] == token_color:
                    count = count + 1
                    row = row - 1
                    column = column - 1
                if count >= 4:
                    winner = 1 
    return winner

def main():
    game_board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    init_game_board (game_board)
    print_game_board (game_board)

    number = 0
    token_color = 'r'
    status = 0
    status2 = 0
    status3 = 0
    while status != 1 and status2 != 1 and status3 != 1:
        column = get_column ()
        place_token (column, game_board, token_color)
        number = number + 1
        
        if number >= 7:
            status = check_vertical_win (column, game_board, token_color)
            print status
            status2 = check_horizontal_win (column, game_board, token_color)
            print status2
            status3 = check_diagonal_win (column, game_board, token_color)
            print status3
            
        if token_color == 'r':
            token_color = 'b'
        else:
            token_color = 'r'

        print_game_board (game_board)

 

main ()
