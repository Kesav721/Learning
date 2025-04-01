#SUDOKU 9X9

import numpy as np

grid=[
    [4,0,9,0,0,5,1,0,0],
    [5,3,0,2,1,0,0,0,0],
    [0,6,2,7,0,4,5,0,8],
    [0,0,3,0,6,0,4,0,0],
    [0,8,7,3,0,0,0,0,0],
    [0,5,4,0,9,7,6,8,0],
    [0,0,5,9,0,6,0,0,1],
    [7,2,0,0,0,0,3,0,0],
    [8,9,0,0,7,0,0,5,6]
]
print(grid)
print(np.matrix(grid))

def possible(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i]==n:
            return False
    for i in range(0,9):
         if grid[i][x]==n:
            return False
    x0=(x//3)*3
    y0=(y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j]==n:
                return False
    return True
        
def solve():
    global grid
    for y in range(0,9):
        for x in range(0,9):
            if grid[y][x]==0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x]=n
                        solve()
                        grid[y][x]=0
                return

    print(np.matrix(grid))
    input('Do you want to try more: ') 

solve()             
