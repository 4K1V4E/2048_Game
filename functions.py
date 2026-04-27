import random


def print_board(board):
    print(board[0][0], "\t", board[0][1], "\t", board[0][2], "\t", board[0][3], "\n")
    print(board[1][0], "\t", board[1][1], "\t", board[1][2], "\t", board[1][3], "\n")
    print(board[2][0], "\t", board[2][1], "\t", board[2][2], "\t", board[2][3], "\n")
    print(board[3][0], "\t", board[3][1], "\t", board[3][2], "\t", board[3][3], "\n")


def start_game():
    # Initializes empty board. 4 rows, 4 columns.
    board = []
    for i in range(4):
        board.append([0] * 4)       

    # [0, 0, 0, 0]
    # [0, 0, 0, 0]
    # [0, 0, 0, 0]
    # [0, 0, 0, 0]

    # Display possible movement commands
    print("'W' = Swipe Up\n'S' = Swipe Down\n'A' = Swipe Left\n'D' = Swipe Right\nAnything Else = Swipe yourself into bed and get some rest because clearly, your noggin isn't loggin'.\n")

    # Add a '2' in a random empty cell.
    # Loops until an empty cell is found.
    add_new_2(board)    # This function will actually update the board.
    
    # We may not always want to add a '2'.
    # Let's say the player entered an invalid key.


    # A '2' is added to random cell.
    # The board is returned.
    return board


def add_new_2(the_board):
    # If the board is full.
    # For each element in each row, check if the value of the element is 0, which would mean that the space is empty.
    # Wrap that in an all() function to check if any of those 4 elements were falsy.
    # If the whole row is comprised of zeros, then the all() function will return 'False'.
    # For each row in the board, check if the all() function returned 'False'.
    if all(all(cell != 0 for cell in row) for row in the_board):
        # A fully populated board will return 'T'.
        # If even one space is empty, the function returns 'F'.
        return      # If the board is full, don't return anything. The board is full and cannot accept a '2'.
    
    # Random placement of a fresh '2'.
    while True:       # 1000 attempts
        # Pick a random row and column.
        r = random.randint(0, 3)    # Picks a number from 0-3, inclusive, and stores it in 'r'. Probably a row index.
        c = random.randint(0, 3)    
        
        if the_board[r][c] == 0:    # If this random spot on the board is unpopulated.
            the_board[r][c] = 2    # Place a '2' in that spot.
            return                  # We've successfully placed a '2'. We can leave now.
        

# Finds the first empty cell in the board.
# This function should produce an iterable exactly 2 items. One for 'r', and one for 'c'.
def find_empty(the_board_again):  
    for i in range(4):
        for j in range(4):
            if the_board_again[i][j] == 0:
                return i, j     # return the index of the empty spot.
    # If there are no empty cells.
    return None, None


# Lol
def random_name():
    list_of_names = ["Harry", "Ron", "Hermione", "Hagrid", "Dumbledore", "Voldemort", "Snape", "Draco"]
    name = random.choice(list_of_names)
    return name


def move_left(the_board):
    # compress() shifts all of the numbers to the left.
    # If there are, for example, two 2s on one row, the compress function returns the row with only the left-most column filled with a '2'. It should be a '4' after they merge.
    new_board, changed1 = compress(the_board)
        # new_board = The new board
        # changed1 = True, if a change was made to the new board
    # Now, we combine identical numbers
    # We pass the new board generated in the compress() function to the merge() function.
    new_board, changed2 = merge(new_board)
    # Matching numbers have been merged.
        # new_board = The modified board
        # changed2 = True, if a modification was actually made to the board
    changed_at_all = changed1 or changed2
    # If any modification was made during compression or merging, this will be 'True'.
    # Another round of compression.
    # This final compression handles cases where there are 3 identical numbers on the same row.
    new_board, does_not_matter = compress(new_board)      # 'does_not_matter' does not matter, because if a change happens at this point, it means that a change must have happened in the first compression. The flag here is not helpful because we know that a change has already occurred.
    # Finally, we show return the updated board and the flag that informs whether any changes whatsoever occurred.
    return new_board, changed_at_all
# Summary: Takes board, compresses, merges, compresses, returns board.


# Shift all numbers to the left
def compress(old_board):
    changed = False
    # old_board --> new_board
    new_board = []
    # Now, we iterate through every spot on the board.
    for i in range(4):
        new_board.append([0] * 4)
    # We just created a new board entirely populated with 0s.

    for i in range(4):
        position = 0        # Slots the added numbers in preparation for merging.
        for j in range(4):
            if old_board[i][j] != 0:      # If the cell on the old board is populated.
                # Add the value of the cell in the old board to the leftmost position on the current row the new board.
                new_board[i][position] = old_board[i][j]

                if j != position:       # If 'j' is the left-most cell, even though no compression is going to happen to it, we visit it solely to cause the position to increase.
                    changed = True      # If j == 0 == position, then that would mean that 'j' is already against the left wall and no shift, or change, would have occured.
                position += 1           # Now, when we copy the next non-zero number to the new board, it will be positioned to the immediate right of the previously added non-zero number.

    # After iterating through every spot on the board, we return the newly crafted board and the 'changed' flag to indicate that a change has occurred.
    return new_board, changed


def merge(the_new_board):
    # At the start, nothing has changed with the board (obviously, since we just passed it in).
    changed = False

    for i in range(4):
        for j in range(3):      # We don't need to iterate through the 4th row, because, naturally, a shift from the 4th row to the 4th row cannot occur.
            # If the current cell is non-zero and is equal to the next cell.
            if the_new_board[i][j] == the_new_board[i][j + 1] and the_new_board[i][j] != 0:
                # Multiply the value in the current cell by 2
                the_new_board[i][j] = the_new_board[i][j] * 2
                # Set the value in the next cell to 0 (since the values have merged).
                the_new_board[i][j + 1] = 0
                # A change has occurred.
                changed = True

        # Finally, return the modified board and the flag.
    return the_new_board, changed
    
    
# Check if game has been won, lost, or is ongoing.
def get_current_state(the_new_board):

    # If game has been won.
    for i in range(4):
        for j in range(4):
            if the_new_board[i][j] == 2048:
                return "Hey everybody, look! Einstein ova he won the game. Bravo. Good f'you. Whattaya want, a prize or somethin'? Ya Mudda would be proudaya. Whateva.\n"
            
    # If there's a spot with a 0, we know that the game is certainly not over.
    for i in range(4):
        for j in range(4):
            if the_new_board[i][j] == 0:
                return ""
    
    # First, see if there are identical values between the cells that are not along the edges.         for i in range(3):          # No need to check the bottom row, since there are no values below them for them to be compared to.
    for i in range(3):      # No need to check the right-most column, since there are no values to the right of them for them to be compared to.
        for j in range(3):
            if the_new_board[i][j] == the_new_board[i + 1][j] or the_new_board[i][j] == the_new_board[i][j + 1]:
            # If the value of the current cell is either equal to the value of the cell right beside it or right beneath it.
                return ""

    # Then, see if there are identical values between the cells along the edges.  
    # After doing so, we'll have addressed every cell, and we'll have certainty regarding the status of the game.   
    for j in range(3):      # No need to check the corner.
        # Check the bottom row.
        if the_new_board[3][j] == the_new_board[3][j + 1]:
            return ""
        
    for i in range(3):      # No need to check the corner.
        # Check the right-most column.
        if the_new_board[i][3] == the_new_board[i + 1][3]:
            return ""
        
    # Otherwise, the game is over.
    return "Betta luck next time, ma guy. Maybe stop wastin' ya time on TicTac and hit the books aw somethin'.\n"


# We needed to create 'move_left()' first in order to create 'move_right()', since 'move_right()' utilizes 'move_left()'.
def move_right(the_board):
    # First, we reverse the board by calling the 'reverse()' function.
    new_board = reverse(the_board)
    # Next, we shift the elements of the reversed board to the left.
    new_board, changed = move_left(new_board)
    # Finally, we reverse the board back to it's original position.
    new_board = reverse(new_board)
    
    return new_board, changed


def reverse(old_board):
    # A fresh list ready to be populated with lists i.e. rows.
    new_board = []
    for i in range(4):      
        new_board.append([])    # Add a row.
        for j in range(4):      # For each cell in the row.
            # for each newly added row, replace 4th row in old board with 1st row in new board, 3rd row in old board with 2nd row in new board, 2nd row in old board with 1st row in new board, and 4th row in old board with 4th row in new board.
            new_board[i].append(old_board[i][3 - j])
    # Return reversed board.
    return new_board


def move_up(the_board):
    # First, we transpose the board by calling the 'transpose()' function.
    new_board = transpose(the_board)
    # Next, we shift the elements of the transposed board to the left.
    new_board, changed = move_left(new_board)
    # Finally, we transpose the board back to it's original position.
    new_board = transpose(new_board)
    
    return new_board, changed


def transpose(old_board):
    # A fresh list ready to be populated with lists i.e. rows.
    new_board = []
    for i in range(4):      
        new_board.append([])    # Add a row.
        for j in range(4):      # For each cell in the row.
            # for each newly added row, replace 
            new_board[i].append(old_board[j][i])
    # Return reversed board.
    return new_board


def move_down(the_board):
    # We've already seen all of the functions that are used here.
    # Transpose, Move Right, Transpose
    new_board = transpose(the_board)
    new_board, changed = move_right(new_board)
    new_board = transpose(new_board)

    return new_board, changed
