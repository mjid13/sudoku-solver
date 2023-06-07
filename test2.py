import clingo


def solve_sudoku(grid):
    # Create a clingo control object
    ctl = clingo.Control()

    # Load the ASP program
    ctl.add("base", [], """
        %Define the domain of the Sudoku grid \n
        { num(1..9,X,Y,V) : val(V) } = 1 :- pos(X,Y). \n
        
        %Define the initial state of the grid \n
        { num(X,Y,V) } = 1 :- grid(X,Y,V). \n
        
        %Ensure that each row contains unique values \n
        :- num(X,Y1,V), num(X,Y2,V), Y1 != Y2. \n
        
        %Ensure that each column contains unique values \n
        :- num(X1,Y,V), num(X2,Y,V), X1 != X2. \n
        
        %Ensure that each subgrid contains unique values \n
        :- num(X1,Y1,V), num(X2,Y2,V), V == num_val, X1 != X2, Y1 != Y2,  \n
           ((X1-1)//3)*3 < X2, X2 <= ((X1-1)//3)*3+3, ((Y1-1)//3)*3 < Y2, Y2 <= ((Y1-1)//3)*3+3. \n
    """)

    # Add the initial grid to the ASP program
    for x in range(1, 10):
        for y in range(1, 10):
            if grid[x-1][y-1] != 0:
                ctl.add("base", [], f"grid({x},{y},{grid[x-1][y-1]}).")

    # Solve the ASP program
    ctl.ground([("base", [])])
    ctl.solve(on_model=lambda m: print_model(m))


def print_model(model):
    # Print the solution grid
    for x in range(1, 10):
        for y in range(1, 10):
            for v in range(1, 10):
                if model.contains(f"num({x},{y},{v})"):
                    print(v, end=" ")
                    break
            else:
                print("ERROR", end=" ")
        print()


# Example usage:
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

grid[0][2] = 4
grid[0][3] = 3
grid[0][5] = 2
grid[0][6] = 9
grid[1][0] = 6
grid[1][1] = 1
grid[1][6] = 7
grid[1][8] = 8
grid[2][2] = 9
grid[2][3] = 8
grid[2][4] = 7
grid[3][0] = 9
grid[3][3] = 7
grid[3][5] = 8
grid[3][8] = 1
grid[4][2] = 8
grid[4][6] = 5
grid[5][0] = 2
grid[5][3] = 1
grid[5][5] = 7
grid[5][8] = 3
grid[6][4] = 3
grid[6][5] = 6
grid[6][6] = 1
grid[6][7] = 7
grid[7][0] = 8
grid[7][2] = 6
grid[7][8] = 4
grid[8][2] = 7
grid[8][3] = 5
grid[8][5] = 4
grid[8][6] = 3
# Set some values in the grid
solve_sudoku(grid)
