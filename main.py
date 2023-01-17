
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]


def found_winning_sequence(_board, piece):
    # check rows
    for row in _board:
        if row[0] == piece and row[1] == piece and row[2] == piece:
            return True

    # check columns
    cols = [0, 1, 2]
    for col in cols:
        if _board[0][col] == piece and _board[1][col] == piece and _board[2][col] == piece:
            return True

    # check diagonals
    if not _board[1][1] == piece:
        return False

    if _board[0][0] == piece and _board[1][1] == piece and _board[2][2] == piece:
        return True

    if _board[0][2] == piece and _board[1][1] == piece and _board[2][0] == piece:
        return True

    return False


def print_board(current_board):
    a = current_board[0][0] or ' '
    b = current_board[0][1] or ' '
    c = current_board[0][2] or ' '
    d = current_board[1][0] or ' '
    e = current_board[1][1] or ' '
    f = current_board[1][2] or ' '
    g = current_board[2][0] or ' '
    h = current_board[2][1] or ' '
    i = current_board[2][2] or ' '
    print(f'  {a}  |  {b}  |  {c}  \n_________________\n  {d}  |  {e}  |  {f}  \n_________________\n  {g}  |  {h}  |  {i}  ')


def set_piece_on_board(current_board, row, col, piece):
    if current_board[row][col]:
        print(f'Board location: {row}, {col} already has a piece on the board. Turn Forfeited!')
        return False
    current_board[row][col] = piece
    return True


def who_is_current_player(total_turns):
    return f'Player {(total_turns % 2) + 1}'


def x_or_o(total_turns):
    if total_turns % 2 == 0:
        return 'X'
    else:
        return 'O'


turns = 0
game_is_live = True

while game_is_live:
    current_player = who_is_current_player(turns)
    current_piece = x_or_o(turns)
    # get player move
    print(f'Next piece: {current_piece}')
    row_move = int(input(f'{current_player}: select an available row: 0,1,2: \n'))
    col_move = int(input(f'{current_player}: select an available column: 0,1,2: \n'))
    placed_board = set_piece_on_board(board, row_move, col_move, current_piece)
    if placed_board:
        # check if player move won
        if found_winning_sequence(board, current_piece):
            game_is_live = False
            print(f'{current_player} wins!')
        else:
            turns += 1
    else:
        turns += 1
    # print board
    print_board(board)
