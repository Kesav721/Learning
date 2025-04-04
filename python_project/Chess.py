# Chess Board Representation
grid = [
    ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
    ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["NP", "NP", "NP", "NP", "NP", "NP", "NP", "NP"],
    ["NR", "NN", "NB", "NQ", "NK", "NB", "NN", "NR"]
]

# Print the board
def print_grid():
    print("\n    A    B    C    D    E    F    G    H")  # Column labels
    print("  ----------------------------------------")
    for i, row in enumerate(grid):
        print(f"{8 - i}|", " | ".join(row), "|")
        print(" -----------------------------------------")


def direction(x,y,ex,ey):
    val1,val2=-1,-1
    if ex-x>0:
        val1 =1
    elif ex-x ==0:
        val1=0

    if ey-y>0:
        val2=1
    elif ey-y==0:
        val2=0
    return val1,val2
    
def obstruction(x,y,ex,ey):
    global grid
    dirx,diry=direction(x,y,ex,ey)
    print(dirx,diry)
    stx,sty= x+dirx,y+diry
    while (stx !=ex or sty !=ey):
        if grid[stx][sty] !='.':
            return False

    return True


# Move validation functions
def straight(x,y,ex,ey) :
    if x==ex or y==ey and obstruction(x,y,ex,ey):
        return True
    return False

def diagonal(x,y,ex,ey):
    if x-ex==y-ey and obstruction(x,y,ex,ey):
        return True
    return False

def lmove(x,y,ex,ey):
    if (abs(x-ex),abs(y-ey)) in [(2,1),(1,2 )]:
        return True
    return False

def movable(piece, x, y, ex, ey):
    color = piece[0]
    piece = piece[1]

    if piece == 'P':  # Pawn movement
        if straight(x, y, ex, ey) and abs(y - ey) == 1 and x == ex:  # Normal move
            if (color == 'B' and ey > y) or (color == 'N' and ey < y):
                return True
        elif diagonal(x, y, ex, ey) and abs(x - ex) == 1 and abs(y - ey) == 1:  # Capture move
            if (color == 'B' and ey > y) or (color == 'N' and ey < y):
                return True
        return False

    elif piece == 'Q':  # Queen
        return straight(x, y, ex, ey) or diagonal(x, y, ex, ey)
    
    elif piece == 'R':  # Rook
        return straight(x, y, ex, ey)
    
    elif piece == 'B':  # Bishop
        return diagonal(x, y, ex, ey)
    
    elif piece == 'N':  # Knight
        return lmove(x, y, ex, ey)
    
    elif piece == 'K':  # King
        if (straight(x, y, ex, ey) or diagonal(x, y, ex, ey)) and abs(x - ex) <= 1 and abs(y - ey) <= 1:
            return True
    
    return False  # Default return False

# Convert chess board notation to array indices
def chess_to_index(position):
    column = ord(position[0].upper()) - ord('A')
    row = 8 - int(position[1])
    return row, column

# Main game loop
turn = "N"  # "N" = White, "B" = Black
while True:
    print_grid()

    # Get move input
    move = input(f"\n{turn}'s turn. Enter move (e.g., E2 E4): ").strip().upper()

    # Validate input
    if len(move) != 5 or move[2] != ' ' or not move[0].isalpha() or not move[3].isalpha():
        print("Invalid input. Use format: E2 E4")
        continue

    # Convert positions
    try:
        start_pos, end_pos = move.split()
        x, y = chess_to_index(start_pos)
        ex, ey = chess_to_index(end_pos)
    except:
        print("Invalid coordinates. Try again.")
        continue

    # Check if the move is within board limits
    if not (0 <= x < 8 and 0 <= y < 8 and 0 <= ex < 8 and 0 <= ey < 8):
        print("Move out of bounds.")
        continue

    # Get the piece
    piece = grid[x][y]

    if piece == "  ":
        print("No piece at selected position.")
        continue

    # Check turn order
    if piece[0] != turn:
        print("Not your turn!")
        continue

    # Check if move is valid
    if not movable(piece, x, y, ex, ey):
        print("Invalid move for this piece.")
        continue

    # Check if capturing the opponent's king
    if grid[ex][ey][1:] == "K":
        print(f"\n{turn} wins by capturing the King!")
        print_grid()
        break

    # Move the piece
    grid[ex][ey] = piece
    grid[x][y] = "  "  # Empty the old position

    # Switch turns
    turn = "B" if turn == "N" else "N"
