grid=[(['.']*8 )[:]for i in range(8)]

turn=1

def init_grid():
    global grid
    arr=['R','N','B','K','Q','B','N','R']
    for x in range(8):
        grid[0][x]='B'+arr[x]
    for x in range(8):
        grid[-1][x]='W'+arr[x]
    for x in range(8):
        grid[1][x]='BP'
    for x in range(8):
        grid[-2][x]='WP'

init_grid()