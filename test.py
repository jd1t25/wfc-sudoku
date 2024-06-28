from p5 import *

easy_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def setup():
    size(650,650)
    no_stroke
    background(200)

def draw(): 
    drawSudoku();


def drawSudoku():
    fontRegular = loadFont('assests/R.ttf');
    strokeWeight(2);

    startx = 10
    starty = 10
    for i in range(10):
        y = starty + (i*70)
        if (i % 3 == 0):
            strokeWeight(5)
        else:
            strokeWeight(2)
        line(startx,y,650-startx,y)
        line(y,startx,y,650-startx)
        # line(startx,y,600-starty,600-y)
    # line(20,20,600,20)
    textFont(fontRegular, 45);
    # text('5',25,15)
    posx = 25
    posy = 15
    for i in range(len(easy_sudoku)):
        for j in range(len(easy_sudoku[0])):
            # text(str(easy_sudoku[i][j]),posx+(70*i),posy+(70*j))
            if easy_sudoku[i][j] == 0:
                text('',posx+(70*i),posy+(70*j))
            else:
                text(str(easy_sudoku[i][j]),posx+(70*j),posy+(70*i))


# p5 supports different backends to render sketches,
# "vispy" for both 2D and 3D sketches & "skia" for 2D sketches
# use "skia" for better 2D experience
# Default renderer is set to "vispy"
run(renderer="vispy")