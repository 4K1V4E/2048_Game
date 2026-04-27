import functions
# import pyfiglet       # For customizing ASCII character fonts

# Initializing the game
if __name__ == '__main__':          # This checks that 'main.py' isn't being run as a module. Meaning, we check that 'main.py' wasn't imported and run from a different file.
    print("\nLET'S PLAY 2048!\n")
    print("I'd like to dedicate this game to my wife, Lizzy, the ultimate 2048 champion.\n")
    
    # Produce picture of the board and do some other things.
    board = functions.start_game()    
    # Creates a 4 x 4 grid initialized with all 0s.
    # Displays the movement controls.
    # Places a '2' in a random cell.
    
    functions.print_board(board)

while True:

    status = functions.get_current_state(board)
    if status != "":
        print(status)
        break

    # User chooses a direction.
    command = input("Choose a direction to swipe:\n> ").upper()
    print()

    # SWIPE UP
    if command == 'W':
        # User wishes to swipe UP.
        board, flag = functions.move_up(board)
        # If the user is silly and tries to move numbers that are against the wall.
        if flag == False:        # Nothing changed when user swiped because the numbers are against the wall.
            print("Ya can't go that way, ma guy! You tryna cheat, or somethin'? Ya Mudda wouldn't be proudaya.\n")
            continue
            # board_display = The updated board (list of lists)
            # flag = If any changes were made whatsoever (bool)
        # Check if the game has been won, is ongoing, or has been lost.
        status = functions.get_current_state(board)
        if status == "":
            # A new '2' is added and the game continues.
            functions.add_new_2(board)
        else:
            functions.print_board(board)
            print(status)
            # If the game has been won or lost.
            break

    # SWIPE DOWN
    elif command == 'S':
        # User wishes to swipe DOWN.
        board, flag = functions.move_down(board)
        # If the user is silly and tries to move numbers that are against the wall.
        if flag == False:       # Nothing changed when user swiped because the numbers are against the wall.
            print("Ya can't go that way, ma guy! You tryna cheat, or somethin'? Ya Mudda wouldn't be proudaya.\n")
            continue
            # board_display = The updated board (list of lists)
            # flag = If any changes were made whatsoever (bool)
        # Check if the game has been won, is ongoing, or has been lost.
        status = functions.get_current_state(board)
        if status == "":
            # A new '2' is added and the game continues.
            functions.add_new_2(board)
        else:
            functions.print_board(board)
            print(status)
            # If the game has been won or lost.
            break

    # SWIPE LEFT
    elif command == 'A':
        # User wishes to swipe LEFT.
        board, flag = functions.move_left(board)
        # If the user is silly and tries to move numbers that are against the wall.
        if flag == False:       # Nothing changed when user swiped because the numbers are against the wall.
            print("Ya can't go that way, ma guy! You tryna cheat, or somethin'? Ya Mudda wouldn't be proudaya.\n")
            continue
            # board_display = The updated board (list of lists)
            # flag = If any changes were made whatsoever (bool)
        # Check if the game has been won, is ongoing, or has been lost.
        status = functions.get_current_state(board)
        if status == "":
            # A new '2' is added and the game continues.
            functions.add_new_2(board)
        else:
            functions.print_board(board)
            print(status)
            # If the game has been won or lost.
            break

    # SWIPE RIGHT
    elif command == 'D':
        # User wishes to swipe RIGHT.
        board, flag = functions.move_right(board)
        # If the user is silly and tries to move numbers that are against the wall.
        if flag == False:       # Nothing changed when user swiped because the numbers are against the wall.
            print("Ya can't go that way, ma guy! You tryna cheat, or somethin'? Ya Mudda wouldn't be proudaya.\n")
            continue
            # board_display = The updated board (list of lists)
            # flag = If any changes were made whatsoever (bool)
        # Check if the game has been won, is ongoing, or has been lost.
        status = functions.get_current_state(board)
        if status == "":
            # A new '2' is added and the game continues.
            functions.add_new_2(board)
        else:
            functions.print_board(board)
            print(status)
            # If the game has been won or lost.
            break
    
    # Invalid entry. User isn't very bright, you see.
    else:
        print(f"Ya gonna have to try dat one maw time, {functions.random_name()}.\n")
    
    # Print the board after each turn move.
    functions.print_board(board)