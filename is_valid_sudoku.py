def is_valid_sudoku(board: list[list[str]]) -> bool:
    for i in range(9):
        row = get_row(board, i)
        if contains_duplicates(row):
            return False
        for j in range(9):
            col = get_col(board, j)
            if contains_duplicates(col):
                return False
            if i % 3 == 0 and j % 3 == 0:
                sub = get_sub(board, i, j)
                if contains_duplicates(sub):
                    return False
    return True

def get_sub(board, row, col):
    sub = []
    for i in range(row // 3 * 3, (row // 3 + 1) * 3):
        sub += board[i][col // 3 * 3 : (col // 3 + 1) * 3]
    return sub

def get_row(board, row):
    return board[row]

def get_col(board, col):
    return [
        board[i][col]
        for i in range(9)
    ]

def contains_duplicates(lst):
    temp = [
        item
        for item in lst
        if item != '.'
    ]
    return len(temp) != len(set(temp))

board = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(is_valid_sudoku(board))

board = \
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(is_valid_sudoku(board))
