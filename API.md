#API

## Functions

**coordinate**: Establishing a position and value for the x and y coordinates to create the game. Using the global keyword
to read and write a global variable inside the function. [1]

**highlighted_box**: Create a box using 2 horizontal and 2 vertical lines that will be highlighted to identify the users
chosen box in the sudoku grid. Using the pygame.draw.line function in order to create the box/square shape. [1]

**draw_grid**: Create the base sudoku 9 by 9 grid by drawing the horizontal and vertical lines using the pygame.draw.line function. 
Bold the lines to create the borders of the 3 by 3 grid within the whole sudoku grid by changing the thickness of the line. Using the 
render and blit functions in order to fill the squares with the generated numbers for the sudoku puzzle. Also, using the 
pygame.draw.rect function in order to fill in the squares with the generated numbers in the colour pink. [1,3,4]

**create_val**: Create the numbers on the surface level of the program and then drawing them onto the game screen so that the numbers
on the board are visible to the player. [1,3]

**error_wrong**: Adding in the "WRONG!" message if a number was inserted incorrectly in the sudoku puzzle. Creating the message on
the surface level and then drawing it onto the game screen so that it is visible to the player. [1,4]

**correct_board**: Checking to see if the numbers that was entered by the player is correct. The function takes the position of 
the number you are entering and the value of the number. Checks the row, column, and box to see if the values are correctly placed
or not. [1,3]

**solver**: Uses the backtracking algorithm in order to solve the sudoku puzzle. Loops through the size of the puzzle to fill the squares and incrementing 
the index position if the event is True. [1]

**instruction**: Displays the game instructions on the screen for the player to view. Uses the render and blit function in order to make 
the text viewable for the player. [1]

**result**: This function continuously runs in order to keep the game open, allow the player to input numbers, receive the wrong message, and
for the user to choose where on the grid they want to insert the numbers. [1]

###### Citations
[1] Building and visualizing sudoku game using pygame. GeeksforGeeks. (2021, September 4). Retrieved November 18, 2021, from https://www.geeksforgeeks.org/building-and-visualizing-sudoku-game-using-pygame/.

[2] marpit19. (n.d.). Sudoku-solver/solver.py at master · Marpit19/Sudoku-Solver. GitHub. Retrieved November 18, 2021, from https://github.com/marpit19/Sudoku-Solver/blob/master/solver.py.

[3] PiyushG14. (n.d.). Pygame-sudoku/sudoku.py at main · Piyushg14/Pygame-Sudoku. GitHub. Retrieved November 18, 2021, from https://github.com/PiyushG14/Pygame-sudoku/blob/main/sudoku.py.

[4] Written by Nat Dunn. Follow Nat on Twitter. (n.d.). Python color constants module. Webucator. Retrieved November 18, 2021, from https://www.webucator.com/article/python-color-constants-module/.
