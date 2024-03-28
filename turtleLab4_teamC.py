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

'''
Function drawBoard
Written by:            Kaylee Grafton
Description:           Sets up the turtle screen and draws the game board using turtle
'''
def drawBoard(board_size, cell_size):
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
Function mouseClick
Written by:             Kaylee Grafton
Description:            When the player clicks on the screen, returns the row and column of the cell.
'''
def mouseClick(x, y, board_size, cell_size):
    grid_offset = (cell_size * board_size) / 2 #offsets the negative number on the grid

    #determines row and col based on mouse coords, starts at 0
    row = int((y - grid_offset) // -cell_size)
    col = int((x + grid_offset) // cell_size)

    return row, col

'''
Function main
'''
def main():
    board_size = 3 #how many cells each row/col gets
    cell_size = 100 #can change this value to make the board and screen bigger or smaller

    drawBoard(board_size, cell_size) #calls function to draw game board

main()