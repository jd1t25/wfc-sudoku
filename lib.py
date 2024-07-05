from p5 import *

# SUDOKU_POS = []
# width=height=DIM = 0


def draw_main(w: int,h: int ,d: int, size: int=28,path: any='assests/R.ttf'):
    global width,height,DIM
    width = w
    height = h
    DIM = d

    FONT_REGULAR = loadFont(path)
    textFont(FONT_REGULAR,size)

def create_sudoku(sudoku_parameter):
  w = width / DIM
  h = height / DIM
  cell = []

  for j in range(DIM):
    row = []
    for i in range(DIM):
      row.append([i*w,j*h])
    cell.append(row)

  global SUDOKU_POS,sudoku
  SUDOKU_POS = cell
  sudoku = sudoku_parameter

# SUDOKU_POS = create_sudoku()

def draw_sudoku(posx:int=25,posy:int=20):
    w = width / DIM;
    h = height / DIM;

    for j in range(DIM):
        for i in range(DIM):
            rect( SUDOKU_POS[i][j][0] , SUDOKU_POS[i][j][1] ,w,h)
            if ( i%3 == 0):
                strokeWeight(3)
            line(SUDOKU_POS[j][i][0],0,SUDOKU_POS[j][i][0],height)
            # line(i*w,0,i*w,height)
            line(0,i*h,width,i*h)
            strokeWeight(1)

    ## Draw Numbers
    fill('black')
    for j in range(DIM):
      for i in range(DIM):
         if (sudoku[i][j] != 0):
            text(str(sudoku[i][j]),SUDOKU_POS[i][j][0]+posx,SUDOKU_POS[i][j][1]+posy)
    fill('white')