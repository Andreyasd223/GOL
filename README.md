Game Of Life (GOL):

The main idea:
    idea of the project its to remake the game in 20x20 board with some features
    i didnt use the .gitignore file bcz the project doesnt contain other files

How to run:
    1. clone the repo. Terminal: git clone https://github.com/Andreyasd223/GOL.git 
    2. install the numpy libraries (Tkinter should be alredy installed)
    3. run the code 

Rules:
    Dead cell (0) | Living cell (1)
    1. A living cell with less than 2 living neighbours dies
    2. A living cell with 2 or 3 living neighbours survives
    3. A living cell with more than 3 living neighbours dies
    4. A dead cell with exactly 3 living neighbours becomes alive

The code:
    the board made of 20x20 matrix with 0 and a None border with the total size 22x22, the idea behind it make the get_neighbors func. easier
    the code runs by generations for each generation the code checks every cell and acts according the rules and creates a new generation

    Main Functios:
        get_neighbors(pos,board): gets the coords of the cell, returns a list of living neighbors
        cell_action(pos,board): acts according the rules 
        update_board(board): copies the board and calculates the next generation
        pices_dict: dictonary with some structures glider,blinker
        random_fill(): randomly fills the board with 20% chance of living cell 

    Render Functions:
        The rander Realised by the Tk lib 
        draw_board(canvas, board): updates the canvas 
        ---------- WINDOW ----------:
            some initilation lines 
        ---------- LOGIC ----------:
            functions that links to some buttons
            runs the game (run_game()) 
            start stop button(start_stop())
            updates the board (next_generation()) 
            replaces the board by the old generation (previous_generation())
            randomly fills the board (randomize_board())
            places the structures/cells (place_cell(event))
        ---------- BUTTONS ----------:
            all the buttons and some options
    

 
