'''
Program Name:      turtleLab4_teamC.py
Authors:           Kaylee Grafton, Frederika Delcuore, Samuel Larocca, Fatema Yasmin, Brendan Loukes
Description:       This program is a game of Tic-Tac-Toe between two players using the turtle library.

Checklist:         Main function
                   At least 3 functions
                   Uses a list
                   Uses a single loop - done
                   Uses a nested loop
                   Uses a multi-if structure
                   Takes user input - done
                   Outputs something to the screen

'''

import turtle

def drawBoard(board_size, cell_size):
    '''
    Function drawBoard
    Written by:            Kaylee Grafton
    Description:           Sets up the turtle screen and draws the game board using turtle
    '''
    screen_size = board_size * cell_size
    padding = 75 #extra space outside of the grid for the screen

    #set up the screen
    screen = turtle.Screen()
    screen.setup(screen_size + padding, screen_size + padding)
    screen.title("Tic-Tac-Toe")

    #create the turtle and set its speed to the fastest
    t = turtle.Turtle()
    t.speed(0)

    #centers the board on the screen
    start_coord = -screen_size / 2 #-150

    #draw horizontal lines
    for i in range(1, board_size):
        t.penup()
        t.goto(start_coord, start_coord + ((i) * cell_size))
        t.pendown()
        t.forward(cell_size * board_size)

    #draw vertical lines
    t.left(90)  #rotates turtle to draw vertical lines
    for i in range(1, board_size):
        t.penup()
        t.goto(start_coord + ((i) * cell_size), start_coord)
        t.pendown()
        t.forward(cell_size * board_size)
    
    t.hideturtle() #hides the turtle
    screen.onscreenclick(lambda x, y: mouseClick(x, y, board_size, cell_size)) #gets coords of mouse click
    screen.mainloop() #keeps the window open

  	'''
    Function Check for Win
    Written by:             Samuel LaRocca
    Description:            Checks if the game has finished and figures out who won or if it was a tie
    '''

    # Check rows
    for row in board:
        if all(cell == 'X' for cell in row):
            return 'X'
        elif all(cell == 'O' for cell in row):
            return 'O'

    # Check columns
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 'X'
        elif all(board[row][col] == 'O' for row in range(3)):
            return 'O'

    # Check diagonals
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return 'X'
    elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return 'O'

    # Check for tie
    if all(all(cell != ' ' for cell in row) for row in board):
        return 'Tie'

    # No winner yet
    return None


def mouseClick(x, y, board_size, cell_size):
    '''
    Function mouseClick
    Written by:             Kaylee Grafton
    Description:            When the player clicks on the screen, returns the row and column of the cell.
    '''
    grid_offset = (cell_size * board_size) / 2 #offsets the negative number on the grid

    #determines row and col based on mouse coords, starts at 0
    row = int((y - grid_offset) // -cell_size)
    col = int((x + grid_offset) // cell_size)

    # Call the function to make a move and switch players
    makeMove(row, col)
    switchPlayers()

def initializeBoard(board_size):
    '''
    Function initializeBoard
    Written by:             Fatema Yasmin
    Description:            initialize the game board as a 2d list
    '''
    return [[' ' for _ in range(board_size)] for _ in range(board_size)]

current_player = 'X'  # Initial player

def makeMove(row, col):
    '''
    Function makeMove
    Written by:             Fatema Yasmin
    Description:            Mark the cell at given row and column for the current player.
     edited by:             Samuel LaRocca
    Description:            Gives an output if a player wins or it there is a tie and offers the chance to start a new game


    '''
    global current_player
    board[row][col] = current_player

      # Check for win or tie
    winner = checkForWin(board)
    if winner:
        if winner == 'Tie':
            print("It's a tie!")
        else:
            print(f"Player {winner} wins!")
        
        # Ask user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == 'yes':
            # Reset the board and start a new game
            global board
            board = initializeBoard(board_size)
            current_player = 'X'
            turtle.clear()  # Clear the previous game board
            drawBoard(board_size, cell_size)
        else:
            turtle.done()  # End the game if the user doesn't want to play again

    else:
        switchPlayers()

def switchPlayers():
    '''
    Function switchPlayers
    Written by:             Fatema Yasmin
    Description:            Switch the current player between 'X' and 'O' after each turn.
    '''
    global current_player
    # check current player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

def main():
    '''
    Function main
    '''
    board_size = 3 #how many cells each row/col gets
    cell_size = 100 #can change this value to make the board and screen bigger or smaller
    global board
    board = initializeBoard(board_size) # initialize the game board
    drawBoard(board_size, cell_size) #calls function to draw game board

main()
