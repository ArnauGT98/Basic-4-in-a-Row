
from IPython.display import clear_output

# Define needed variables
player = 1
row = 6
column = 7
char1 = 'x'
char2 = 'o'

# Define needed functions
def create_board(row, column):
    """Creates the game board.
    
    Parameters:
    row : int
        Number of rows in the board.
    column : int
        Number of columns in the board.
        
    Returns:
    list of lists
        The initialized game board with dimensions row x column.
    """
    board = [[' ' for _ in range(column)] for _ in range(row)]
    return board

def show_board(board):
    """Prints the current state of the game board.    
    Parameters:
    board : list of lists
        Represents the board with all the squares.
    """
    # Print reference numbers at the top
    for i in range(len(board[0])):
        print(i, end='  ')
    print()  # Move to the next line after printing reference numbers
    
    # Print the rest of the board
    for row in board:
        print()
        for square in row:
            print(square, end='  ')

def drop_piece(board, column, player):
    """Allows to drop a new piece onto the board and returns the updated board with the piece placed.
    
    Parameters:
    board : list of lists
        Represents the board with all the squares.
    column : int
        Represents the column value in which the new piece is to be dropped.
    player : int
        Represents the player making the move.
        
    Returns:
    list of lists
        Updated board with the piece placed.
    """
    # Verify if the column is full
    new_row = len(board) - 1
    if column >= len(board[0]):
        print("[+] Error: This column is full!")
        
    for i in range(len(board)):
        if board[i][column - 1] == char1 or board[i][column - 1] == char2:
            new_row = i - 1
            break
    
    # Restrictions
    if new_row < 0 or new_row > len(board):
        print("[+] Error: This row is not in this board!")
    else:
        # Place the piece on the board
        if player == 1:
            board[new_row][column - 1] = char1
        else:
            board[new_row][column - 1] = char2
            
    return board

def check_rows(board, player):
    """Checks if there are four consecutive pieces of the same player in a row and prints a message if so.
    
    Parameters:
    board : list of lists
        Represents the board with all the squares.
    player : int
        Represents the player whose pieces are being checked.
        
    Returns:
    bool
        True if there are four consecutive pieces of the same player in a row, False otherwise.
    """
    # Get the color of the player
    if player == 1:
        color = char1
    else:
        color = char2 
    
    for r in range(len(board)): # Iterate through the rows
        for c in range(len(board[0]) - 3): # Iterate through the columns
            if board[r][c] == color and board[r][c+1] == color and board[r][c+2] == color and board[r][c+3] == color:
                print("\n[+] ... "), print("[+] Congratulations, you won with four in a row horizontally!!!"), print("The winner is:", color)
                return True
    
def check_columns(board, player):
    """Checks if there are four consecutive pieces of the same player in a column and prints a message if so.
    
    Parameters:
    board : list of lists
        Represents the board with all the squares.
    player : int
        Represents the player whose pieces are being checked.
        
    Returns:
    bool
        True if there are four consecutive pieces of the same player in a column, False otherwise.
    """
    # Get the color of the player
    if player == 1:
        color = char1
    else:
        color = char2
    
    for c in range(len(board[0])): # Iterate through the columns
        for r in range(len(board) - 3): # Iterate through the rows
            if board[r][c] == color and board[r+1][c] == color and board[r+2][c] == color and board[r+3][c] == color:
                print("\n[+] ... "), print("[+] Congratulations, you won with four in a row vertically!!!"), print("The winner is:", color )
                return True

def check_right_diagonal(board, player):
    """Checks if there are four consecutive pieces of the same player in a right diagonal and prints a message if so.
    
    Parameters:
    board : list of lists
        Represents the board with all the squares.
    player : int
        Represents the player whose pieces are being checked.
        
    Returns:
    bool
        True if there are four consecutive pieces of the same player in a right diagonal, False otherwise.
    """
    # Get the color of the player
    if player == 1:
        color = char1
    else:
        color = char2
    
    # Start looking from the bottom-left corner of the board
    col_start = 0
    row_start = 5
    
    # Check if the square is empty or filled
    for c in range(len(board[0]) - 3): # Iterate through the columns 
        for r in range(len(board) - 1, 2, -1):
            if board[r][c] == color and board[r-1][c+1] == color and board[r-2][c+2] == color and board[r-3][c+3] == color:
                print("\n\n[+] ... "), print("[+] Congratulations, you won with four in a row in a right diagonal!!"), print("[+] Winner: 4", color)
                return True

def check_left_diagonal(board, player):
    """Checks if there are four consecutive pieces of the same player in a left diagonal and prints a message if so.
    
    Parameters:
    board : list of lists
        Represents the board with all the squares.
    player : int
        Represents the player whose pieces are being checked.
        
    Returns:
    bool
        True if there are four consecutive pieces of the same player in a left diagonal, False otherwise.
    """
    # Get the color of the player
    if player == 1:
        color = char1
    else:
        color = char2
    
    # Start looking from the bottom-left corner of the board
    col_start = 0
    row_start = 5
    
    for c in range(len(board[0]) - 1, 2, -1): # Iterate through the columns 
        for r in range(len(board) - 1, 2, -1):
            if board[r][c] == color and board[r-1][c-1] == color and board[r-2][c-2] == color and board[r-3][c-3] == color:
                print("\n\n[+] ... "), print("[+] Congratulations, you won with four in a row in a left diagonal!!"), print("[+] Winner: 4", color)
                return True

def check_winner(board, color):
    """Checks if a player has won the game and returns True if so.
    
    Parameters:
    board : list of lists
        Represents the board with all the squares.
    color : str
        Represents the color of the player's pieces being checked.
        
    Returns:
    bool
        True if a player has won, False otherwise.
    """
    if check_rows(board, color) or check_columns(board, color) or check_right_diagonal(board, color) or check_left_diagonal(board, color):
        return True

def display_logo():
    print("""
          
 ██████╗  █████╗ ███╗   ███╗███████╗    ██╗  ██╗    ██╗███╗   ██╗    ██████╗  ██████╗ ██╗    ██╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██║  ██║    ██║████╗  ██║    ██╔══██╗██╔═══██╗██║    ██║
██║  ███╗███████║██╔████╔██║█████╗      ███████║    ██║██╔██╗ ██║    ██████╔╝██║   ██║██║ █╗ ██║
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ╚════██║    ██║██║╚██╗██║    ██╔══██╗██║   ██║██║███╗██║
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗         ██║    ██║██║ ╚████║    ██║  ██║╚██████╔╝╚███╔███╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝         ╚═╝    ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ 

""")

def clear_board(board):
    """Clears the content of the board and resets it.
    
    Params:
    board : list of lists
        Represents the game board.
        
    Returns:
    list of lists
        The cleared and reset game board.
    """
    rows = len(board)  # Get the number of rows in the board
    columns = len(board[0])  # Get the number of columns in the board
    new_board = create_board(rows, columns)  # Generates a new board using the dimensions of the current board
    board[:] = new_board  # Overwrites the content of the current board with the new board
    print("The board has been cleared, and a new game can begin.")
    return board

# Define Game settings
next_turn = 1  # Initialize next_turn with the first turn
player_num = input("Enter your player number: ")

# Game starts here
if not player_num.isdigit():
    print("[+] Error: The input value must be numeric")
else:
    player_num = int(player_num)
    
    # Assuming `board` needs to be defined before its use
    board = create_board(6, 7)
    display_logo()
    
    while True:
        turn = next_turn
        print("Player's turn:", turn)
        show_board(board)
        print("\n\n")
        column = int(input("[+] Inserting a new chip in column: "))
        print("\n\n")
        if column >= len(board[0]):
            print("[+] Error: Invalid column, this board doesn't have that many columns!"); print("\n\n");
            print("[+] Error: The maximum number of columns is:", len(board[0]))
            continue  # Retry the turn if the column is invalid
        
        if turn == 1:
            token = 'x'  # Color of player 1's token
            next_turn = 2  # Switch the turn to player 2
        elif turn == 2:
            token = 'o'  # Color of player 2's token
            next_turn = 1  # Switch the turn to player 1
        
        drop_piece(board, column, turn)
        show_board(board)
        clear_output(wait=False)
        
        if check_winner(board, token):
            print("[+] Winner: Player ", turn, "\n")
            show_board(board)
            break





 



