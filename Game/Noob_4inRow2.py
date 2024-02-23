from colorama import init, Fore

# Define needed variables
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
    """Prints the current state of the game board with enumerated columns and rows.

    Parameters:
    board : list of lists
        Represents the board with all the squares.
    """
    # Initialize colorama
    init()

    # Print column numbers at the top in yellow
    print('    ' + Fore.YELLOW + '   '.join(str(i+1) for i in range(len(board[0]))))

    # Print the board with grid lines, enumerated columns, and rows
    for r, row in enumerate(board, start=1):
        print(f'{r} ', end='')  # Print row number
        print(Fore.MAGENTA + '|', end='')  # Print left border of the row
        for square in row:
            print(Fore.MAGENTA + f' {square} |', end='')  # Print square with color
        print('\n+' + '---+' * len(row) + '-')  # Print horizontal grid lines between rows

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
    for i in range(len(board)):
        if board[i][column - 1] == char1 or board[i][column - 1] == char2:
            new_row = i - 1
            break
    
    # Restrictions
    if new_row < 0 or new_row > len(board):
        print("[+] Error:  This column is full!")
        return board

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

#def check_right_diagonal(board, player):
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

#Gdef check_right_diagonal(board, player):
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
    color = char1 if player == 1 else char2
    
    for c in range(len(board[0]) - 3): # Iterate through the columns 
        for r in range(len(board) - 3): # Iterate through the rows
            if board[r][c] == color and board[r+1][c+1] == color and board[r+2][c+2] == color and board[r+3][c+3] == color:
                print("\n[+] Congratulations, you won with four in a row in a right diagonal!!")
                return True
    
    for c in range(3, len(board[0])): # Iterate through the columns 
        for r in range(len(board) - 3): # Iterate through the rows
            if board[r][c] == color and board[r+1][c-1] == color and board[r+2][c-2] == color and board[r+3][c-3] == color:
                print("\n[+] Congratulations, you won with four in a row in a right diagonal!!")
                return True
                
    return False

#def check_left_diagonal(board, player):
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

#Gdef check_left_diagonal(board, player):
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
    color = char1 if player == 1 else char2
    
    for c in range(len(board[0]) - 3): # Iterate through the columns 
        for r in range(len(board) - 3): # Iterate through the rows
            if board[r][c] == color and board[r+1][c+1] == color and board[r+2][c+2] == color and board[r+3][c+3] == color:
                print("\n[+] Congratulations, you won with four in a row in a left diagonal!!")
                return True
    
    for c in range(3, len(board[0])): # Iterate through the columns 
        for r in range(len(board) - 3): # Iterate through the rows
            if board[r][c] == color and board[r+1][c-1] == color and board[r+2][c-2] == color and board[r+3][c-3] == color:
                print("\n[+] Congratulations, you won with four in a row in a left diagonal!!")
                return True
                
    return False

def upp_right_diag(board, player):
    """Checks if there are four consecutive pieces of the same player in an upper right diagonal and prints a message if so.
    
    Parameters:
    board : list of lists
        Represents the board with all the squares.
    player : int
        Represents the player whose pieces are being checked.
        
    Returns:
    bool
        True if there are four consecutive pieces of the same player in an upper right diagonal, False otherwise.
    """
    color = char1 if player == 1 else char2
    
    for c in range(len(board[0]) - 3):
        for r in range(len(board) - 3):
            if board[r][c] == color and board[r+1][c+1] == color and board[r+2][c+2] == color and board[r+3][c+3] == color:
                print("\n[+] Congratulations, you won with four in a row in an upper right diagonal!!")
                return True
    return False

def upp_left_diag(board, player):
    """Checks if there are four consecutive pieces of the same player in an upper left diagonal and prints a message if so.
    
    Parameters:
    board : list of lists
        Represents the board with all the squares.
    player : int
        Represents the player whose pieces are being checked.
        
    Returns:
    bool
        True if there are four consecutive pieces of the same player in an upper left diagonal, False otherwise.
    """
    color = char1 if player == 1 else char2
    
    for c in range(3, len(board[0])):
        for r in range(len(board) - 3):
            if board[r][c] == color and board[r+1][c-1] == color and board[r+2][c-2] == color and board[r+3][c-3] == color:
                print("\n[+] Congratulations, you won with four in a row in an upper left diagonal!!")
                return True
    return False

def low_right_diag(board, player):
    """Checks if there are four consecutive pieces of the same player in a lower right diagonal and prints a message if so.
    
    Parameters:
    board : list of lists
        Represents the board with all the squares.
    player : int
        Represents the player whose pieces are being checked.
        
    Returns:
    bool
        True if there are four consecutive pieces of the same player in a lower right diagonal, False otherwise.
    """
    color = char1 if player == 1 else char2
    
    for c in range(len(board[0]) - 3):
        for r in range(3, len(board)):
            if board[r][c] == color and board[r-1][c+1] == color and board[r-2][c+2] == color and board[r-3][c+3] == color:
                print("\n[+] Congratulations, you won with four in a row in a lower right diagonal!!")
                return True
    return False

def low_left_diag(board, player):
    """Checks if there are four consecutive pieces of the same player in a lower left diagonal and prints a message if so.
    
    Parameters:
    board : list of lists
        Represents the board with all the squares.
    player : int
        Represents the player whose pieces are being checked.
        
    Returns:
    bool
        True if there are four consecutive pieces of the same player in a lower left diagonal, False otherwise.
    """
    color = char1 if player == 1 else char2
    
    for c in range(3, len(board[0])):
        for r in range(3, len(board)):
            if board[r][c] == color and board[r-1][c-1] == color and board[r-2][c-2] == color and board[r-3][c-3] == color:
                print("\n[+] Congratulations, you won with four in a row in a lower left diagonal!!")
                return True
    return False

def check_all_diagonals(board, player):
    """Checks if there are four consecutive pieces of the same player in any diagonal direction and prints a message if so.
    
    Parameters:
    board : list of lists
        Represents the board with all the squares.
    player : int
        Represents the player whose pieces are being checked.
        
    Returns:
    bool
        True if there are four consecutive pieces of the same player in any diagonal direction, False otherwise.
    """
    if upp_right_diag(board, player) or upp_left_diag(board, player) or low_right_diag(board, player) or low_left_diag(board, player):
        return True
    return False


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
    return check_rows(board, color) or check_columns(board, color) or check_all_diagonals(board, color)

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

# Rest of the functions remain unchanged...

# Game starts here
player_num = input("Enter your player number: ")
from IPython.display import clear_output

if not player_num.isdigit():
    print("[+] Error: The input value must be numeric")
else:
    player_num = int(player_num)
    
    # Assuming `board` needs to be defined before its use
    board = create_board(6, 7)
    display_logo()
    
    next_turn = 1 if player_num == 1 else 2
    
    while True:
        turn = next_turn
        print('\n\n\n')
        print("Player's turn:", turn)
        show_board(board)
        column_input = input("[+] Inserting a new chip in column: ")
        print("\n\n")
        
        # Check if column_input is a valid integer
        if not column_input.isdigit():
            print("[+] Error: The introduced column must be numeric.")
            continue
        
        column = int(column_input)
        
        # Check if column_input is within board's column range
        if column < 1 or column > len(board[0]):
            print("[+] Error: The introduced column is out of board's domain.")
            continue
        
        # Make the move
        board = drop_piece(board, column, turn)

        # Check if there is a winner
        token = 'x' if turn == 1 else 'o'
        if check_winner(board, token):
            print("[+] Winner: Player ", turn, "\n")
            show_board(board)
            clear_output(wait=False)
            break
        
        # Switch to the next player's turn
        next_turn = 2 if turn == 1 else 1