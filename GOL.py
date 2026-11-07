import numpy as np
import tkinter as tk
CELL_SIZE = 25
board_history = []


board = np.zeros((22, 22), dtype=object)
board[0, :] = None
board[-1, :] = None
board[:, 0] = None
board[:, -1] = None
# Main matrix 20x20 with a None border


matrix = np.array([
    [None, None, None, None, None, None, None, None, None, None, None, None],
    [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None],
    [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None],
    [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None],
    [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None],
    [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None],
    [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None],
    [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None],
    [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None],
    [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None],
    [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None],
    [None, None, None, None, None, None, None, None, None, None, None, None]
], dtype=object)
# Test matrix 10x10 {12x12}



def get_neighbors(pos):

    cell_row, cell_col = pos
    if cell_row > 0 and cell_row < 11 and cell_col > 0 and cell_col < 11:
        pass
    else:
        return "ERROR out of range"
    
    neighbors = board[cell_row-1:cell_row+2, cell_col-1:cell_col+2]
    # 0, 0, 0
    # 0,pos,0
    # 0, 0, 0
    neighbors_ls = []

    for row in neighbors:
        for cell in row:
            if cell == 1:
                neighbors_ls.append(cell)
    return neighbors_ls


def cell_action(pos):
    neighbors = get_neighbors(pos)
    cell = board[pos]
    match len(neighbors):
        case n if n < 2 and cell == 1:
            return 0
        case n if n == 2 or n == 3 and cell == 1:
            return 1
        case n if n > 3 and cell == 1:
            return 0
        case n if n == 3 and cell == 0:
            return 1

def update_board():
    temp_board = np.copy(board)
    for row in range(1, 21):
        for col in range(1, 21):
            temp_board[row][col] = cell_action((row, col))
    board = np.copy(temp_board)
    board_history.append(np.copy(board))


    