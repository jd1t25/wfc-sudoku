import numpy as np

def is_valid(sudoku, row, col, num):
    # Check if the number is already in the current row
    if num in sudoku[row, :]:
        return False
    
    # Check if the number is already in the current column
    if num in sudoku[:, col]:
        return False
    
    # Check if the number is already in the 3x3 sub-grid
    subgrid_row_start = (row // 3) * 3
    subgrid_col_start = (col // 3) * 3
    if num in sudoku[subgrid_row_start:subgrid_row_start + 3, subgrid_col_start:subgrid_col_start + 3]:
        return False
    
    return True

def solve_sudoku(sudoku):
    empty_spot = find_empty_spot(sudoku)
    
    if not empty_spot:
        return True  # Sudoku is already solved
    
    row, col = empty_spot
    
    for num in range(1, 10):
        if is_valid(sudoku, row, col, num):
            sudoku[row, col] = num
            
            if solve_sudoku(sudoku):
                return True
            
            sudoku[row, col] = 0  # Backtrack
            
    return False

def find_empty_spot(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i, j] == 0:
                return (i, j)
    return None

# Example usage:
sudoku = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

if solve_sudoku(sudoku):
    print("Sudoku Solved:")
    print(sudoku)
else:
    print("No solution exists.")
