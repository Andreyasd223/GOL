import numpy as np


board = np.array([
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
])
# lt, ct ,rt
# cl,pos,cr
# lb, cb, rb
def get_neighbors(pos):
    cell_row, cell_col = pos
    if cell_row > 0 and cell_row < 11 and cell_col > 0 and cell_col < 11:
        pass
    else:
        return "ERROR out of range"
    neighbors = board[cell_row-1:cell_row+2, cell_col-1:cell_col+2]
    return neighbors

def dead_alone(pos):# if pos==1
    neighbors = get_neighbors(pos)
    life_count

    for neighbors_row in neighbors:
        for neighbor in neighbors_row:
