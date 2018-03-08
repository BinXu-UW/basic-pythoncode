# This is the start of our Connect 4 game. We started by first defining
# the playing board as a list of lists (seen in main ()). We have finished
# the definitions for initializing the game board to '.' and printing out the
# game board.

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

#def check_horizontal_win (column, game_board, token_color):
    

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
    while number < 4:
        column = get_column ()
        place_token (column, game_board, 'r')

        print_game_board (game_board)

        number = number + 1

    status = check_vertical_win (column, game_board, 'r')
    print status

main ()
