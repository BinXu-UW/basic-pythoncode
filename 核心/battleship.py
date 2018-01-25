
def init_game_board(a_game_board):
    for row in range (10):
        for col in range (10):
            a_game_board[row][col] = '-';

           
def print_game_board(a_game_board):
    for row in range (10):
        for col in range (10):
            print a_game_board[row][col]+ " ",
        print '\n'



def get_location():
    location = [];
    row = raw_input("Enter row number: ");
    col = raw_input("Enter col number: ");
    location.append(row);
    location.append(col);
    return location;

def place_token (location, game_board, token_color):
    row = location[0];
    col = location[1];
    while game_board[row][col] != '-':
        row = row - 1
    game_board[row][col] = token_color

def check_win(game_board):
    for row in range (10):
        for col in range (10):
            if(game_board[row][col] 
    

def main():
    
    game_board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    init_game_board(game_board);
    print_game_board(game_board);
    attack = get_location();

    print_game_board(game_board)


main()
