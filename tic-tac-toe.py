
def print_board(board):
    for row in board:
        print(row)
        # for column in row:
        #     print(column)


def is_valid_size(board):
    # 1. Setup/configuration
    is_valid = True

    # 2. Do some work
    # Does it have three rows?
    if len(board) != 3:
        is_valid = False
    # Does it have 3 columns per row?    
    for row in board:
        if len(row) != 3:
            is_valid = False
    
    # 3. Return the result
    return is_valid

def move(board, location, player):
    # Handle those errors!
    if not is_valid_size(board):
        raise Exception('Game board size is not valid!')

    # print(f"The player is {player}")
    row_number = location[0]
    col_number = location[1]
    # print(f"They want to move to row {row_number}")
    # print(f"They want to move to col {col_number}")

    board[row_number][col_number] = player    
    # print(board)
    return board


game_board = [
    [' ', ' '],
    [' ', ' ', ' '],    
    [' ', ' ', ' ']
]
# print(is_valid_size(game_board))
player = 'O'
loc = (0, 0)
game_board = move(game_board, loc, player)

player = 'X'
loc = (0, 1)
game_board = move(game_board, loc, player)

print_board(game_board)