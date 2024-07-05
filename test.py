from p5 import *
import numpy as np
from lib import *

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

# easy_sudoku = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]

width = 650
height = 650
DIM = 9
entropy = {}

# sudoku_cell = []
# sudoku_cell = create_sudoku(width,height,DIM)

def find_entropy():

    ## Fill first all entropy values with default
    ## Create tuple as key and fill values with list containing 1 to 9
    entropy = {(i,j):list(range(1,10)) for i in range(9) for j in range(9)}
    # print(entropy)

    for i in range(9):
        for j in range(9):
            if sudoku[i, j] == 0:
                # Get numbers in current row and column
                row = set(sudoku[i, :])
                col = set(sudoku[:, j])
                
                # Get numbers in current 3x3 sub-grid
                subgrid_row_start = (i // 3) * 3
                subgrid_col_start = (j // 3) * 3
                subgrid = set(sudoku[subgrid_row_start:subgrid_row_start + 3, subgrid_col_start:subgrid_col_start + 3].flatten())
                
                # Subtract numbers in row, column, and sub-grid from possible numbers
                total = row.union(col).union(subgrid)
                entropy[(i, j)] = list(set(entropy[(i, j)]) - total)

    print(entropy)

def setup():
    size(width,height)
    no_stroke
    background(200)

    ## Setup Sudoku
    draw_main(width,height,DIM)
    create_sudoku(sudoku)
    find_entropy()


def draw(): 
    background('#ECECEC')
    # print(sudoku_cell)

    ## Draw Sudoku
    draw_sudoku()

# p5 supports different backends to render sketches,
# "vispy" for both 2D and 3D sketches & "skia" for 2D sketches
# use "skia" for better 2D experience
# Default renderer is set to "vispy"
run(renderer="vispy")



















# def drawSudoku()
#     fontRegular = loadFont('assests/R.ttf');
#     strokeWeight(2);

#     startx = 10
#     starty = 10
#     for i in range(10):
#         y = starty + (i*70)
#         if (i % 3 == 0):
#             strokeWeight(5)
#         else:
#             strokeWeight(2)
#         line(startx,y,650-startx,y)
#         line(y,startx,y,650-startx)
#         # line(startx,y,600-starty,600-y)
#     # line(20,20,600,20)
#     textFont(fontRegular, 45);
#     # text('5',25,15)
#     posx = 25
#     posy = 15
#     for i in range(len(easy_sudoku)):
#         for j in range(len(easy_sudoku[0])):
#             # text(str(easy_sudoku[i][j]),posx+(70*i),posy+(70*j))
#             if easy_sudoku[i][j] == 0:
#                 text('',posx+(70*i),posy+(70*j))
#             else:
#                 text(str(easy_sudoku[i][j]),posx+(70*j),posy+(70*i))
