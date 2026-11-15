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

def get_neighbors(pos,board):

    cell_row, cell_col = pos
    if cell_row > 0 and cell_row < 21 and cell_col > 0 and cell_col < 21:
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
    if board[cell_row][cell_col] == 1:
        neighbors_ls.remove(1)
    # removes the cell itself
    return neighbors_ls


def cell_action(pos,board):
    neighbors = get_neighbors(pos,board)
    cell = board[pos]
    match len(neighbors):
        case n if n < 2 and cell == 1:
            return 0
        case n if (n == 2 or n == 3) and cell == 1:
            return 1
        case n if n > 3 and cell == 1:
            return 0
        case n if n == 3 and cell == 0:
            return 1
        case _:
            return 0



def update_board(board):
    temp_board = np.copy(board)
    for row in range(1, 21):
        for col in range(1, 21):
            temp_board[row][col] = cell_action((row, col),board)
    board_history.append(np.copy(board))
    return temp_board

pices_dict = {
    "glider" : np.array([
        [1, 1, 1],
        [1, 0, 0],
        [0, 1, 0]
    ]),
    
    "blinker" : np.array([
        [1, 1, 1]
    ])
}

def random_fill():
    DEAD_CHANCE = 0.8 
    ALIVE_CHANCE = 0.2
    board[1:21, 1:21] = np.random.choice([0,1], size=(20, 20), p=[DEAD_CHANCE, ALIVE_CHANCE])
    return board

def draw_board(canvas, board):
    canvas.delete("all")

    for row in range(1, 21):
        for col in range(1, 21):

            if board[row][col] == 1:
                color = "#0f766e"
            else:
               color = "#ffffff"

            canvas.create_rectangle(
                (col - 1) * CELL_SIZE, (row - 1) * CELL_SIZE,
                col * CELL_SIZE, row * CELL_SIZE,
                fill=color,
                outline="#cbd5e1"
            )   

# ---------- WINDOW ----------

root = tk.Tk()
root.title("Game of Life")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

controls = tk.Frame(root)
controls.pack(pady=10)

running = False
selected_tool = tk.StringVar(value="Cell")

# ---------- LOGIC ----------

def run_game():
    global board

    if running:
        board = update_board(board)
        draw_board(canvas, board)
        root.after(300, run_game)


def start_stop():
    global running

    running = not running

    if running:
        start_button.config(text="Stop")
        run_game()
    else:
        start_button.config(text="Start")


def next_generation():
    global board

    if not running:
        board = update_board(board)
        draw_board(canvas, board)


def previous_generation():
    global board

    if not running and board_history:
        board = board_history.pop()
        draw_board(canvas, board)

def clear_board():
    board[1:21, 1:21] = 0
    board_history.clear()
    draw_board(canvas, board)


def randomize_board():
    random_fill()
    board_history.clear()
    draw_board(canvas, board)


# ---------- MOUSE ----------

def place_cell(event):
    row = event.y // CELL_SIZE + 1
    col = event.x // CELL_SIZE + 1

    if not (1 <= row <= 20 and 1 <= col <= 20):
        return

    tool = selected_tool.get()

    if tool == "Cell":
        board[row][col] = 1 - board[row][col]

    else:
        pattern = pices_dict[tool]
        height, width = pattern.shape

        if row + height - 1 > 20 or col + width - 1 > 20:
            return

        for r in range(height):
            for c in range(width):
                if pattern[r][c] == 1:
                    board[row + r][col + c] = 1

    board_history.clear()
    draw_board(canvas, board)


# ---------- BUTTONS ----------

start_button = tk.Button(
    controls, text="Start", command=start_stop
)
start_button.pack(side="left")

tk.Button(
    controls, text="Next", command=next_generation
).pack(side="left")

tk.Button(
    controls, text="Back", command=previous_generation
).pack(side="left")

tk.Button(
    controls, text="Random", command=randomize_board
).pack(side="left")

tk.Button(
    controls, text="Clear", command=clear_board
).pack(side="left")

tk.OptionMenu(
    controls,
    selected_tool,
    "Cell",
    "glider",
    "blinker"
).pack(side="left")

canvas.bind("<Button-1>", place_cell)

draw_board(canvas, board)

root.mainloop()
