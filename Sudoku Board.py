#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#citation1: https://github.com/PiyushG14/Pygame-sudoku/blob/main/sudoku.py
#citation2: webucator.com/article/python-color-constants-module/
#citation3: https://github.com/marpit19/Sudoku-Solver/blob/master/solver.py
#citation4: https://www.geeksforgeeks.org/building-and-visualizing-sudoku-game-using-pygame/

# import the pygame 
import pygame
import requests

# initialise pygame
pygame.init()

# initialise the pygame font
# citation 4 
pygame.font.init()
 
# set the size of the game screen
# citation 4
window = pygame.display.set_mode((500, 600))
#set the value for x position on sudoku board
x = 0
#set the value for y position on sudoku board 
y = 0
# difference in the iteration for the x and y coordinates
dif = 500 / 9
# starting point
value = 0

# citation 1
# Default Sudoku Board
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json()['board']
 
# citation 1 
# loading the font for the sudoku board 
# font 1 is for the numbers on the board
numbersfont = pygame.font.SysFont("arial", 40)
# font 2 is for the instructional text under the board
instructfont = pygame.font.SysFont("arial", 20)
# citation 1 and 4
# use the global keyword to read and write a global variable inside a function
def coordinate(position):
    # position for x 
    global x
    x = position[0]//dif
    #position for y
    global y
    y = position[1]//dif
 
# citation 4
# Highlight the cell that is selected with the mouse
def highlighted_box():
    for i in range(2):
        pygame.draw.line(window, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(window, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)  

# citation 4
# Function to create the sudoku grid    
def draw_grid():
    # create a 9x9 grid (standard size for sudoku)
    for i in range (9):
        for j in range (9):
            if grid[i][j]!= 0:
 
                # Fill pink color in already numbered grid
                pygame.draw.rect(window, (255,182,193), (i * dif, j * dif, dif + 1, dif + 1))
 
                # Fill grid with the default numbers that came from the grid 
                text1 = numbersfont.render(str(grid[i][j]), 1, (0,0,0))
                window.blit(text1, (i * dif + 15, j * dif + 15))
    # Draw lines horizontally and vertically to form grid 
    # citation 1 
    # citation 3 
    for i in range(0,10):
        #bold the borders of the sudoku boxes (3x3)
        if i % 3 == 0 :
            # vertical BOLD line
            pygame.draw.line(window, (0, 0, 0), (0, i * dif), (500, i * dif), 4)
            # horizontal BOLD line
            pygame.draw.line(window, (0, 0, 0), (i * dif, 0), (i * dif, 500), 4)    
        #vertical line
        pygame.draw.line(window, (0, 0, 0), (0, i * dif), (500, i * dif), 2)
        # horizontal line
        pygame.draw.line(window, (0, 0, 0), (i * dif, 0), (i * dif, 500), 2)     

# citation 4 
# create the value and fill in the sudoku board   
def create_val(value):
    # create the numbers on a surface level
    # citation 3 
    grid_nums = numbersfont.render(str(value), 1, (0, 0, 255))
    # draw the text onto the grid/screen
    window.blit(grid_nums, (x * dif + 15, y * dif + 15))   
 
#citation 4
# wrong message will appear if the number that is entered is not correct for the board
def error_wrong():
    # add "WRONG! message"
    # citation 3
    text1 = numbersfont.render("WRONG!", 1, (0, 0, 0))
    # draw the text onto the grid/screen
    window.blit(text1, (20, 570)) 

# citation 1 
# citation 4 
# Check if the value entered in board is valid
# takes the position of the number you are entering and the number itself
def correct_board(m, i, j, value):
    #row, column, and box
    for it in range(9):
        #if any element in the row is equal to the value it is an invalid number
        if m[i][it]== value:
            return False
        # check the element in the column is equal to the value it is an invalid number
        if m[it][j]== value:
            return False
    #to get the block number divide the position by 3 
    it = i//3
    jt = j//3
    # check the element in the column 
    for i in range(it * 3, it * 3 + 3):
        for j in range (jt * 3, jt * 3 + 3):
            if m[i][j]== value:
                return False
    #if the elements are all passed then we can return true 
    return True

#citation 4 
# Solves the sudoku board using the Backtracking Algorithm
# check position of i at the position j 
def solver(grid, i, j):
    # start with the first grid position 
    while grid[i][j]!= 0:
        if i<8:
            # try the next index position
            i+= 1
        elif i == 8 and j<8:
            # first value to fill field before increment
            i = 0
            # increment, try the next index position
            j+= 1
        # success case then return true 
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()   
    #check row, column and the box 
    #loop through all possible values in sudoku 1-9
    for it in range(1, 10):
        if correct_board(grid, i, j, it)== True:
            grid[i][j]= it
            global x, y
            x = i
            y = j
            # white color background
            window.fill((255, 255, 255))
            draw_grid()
            highlighted_box()
            pygame.display.update()
            if solver(grid, i, j)== 1:
                return True
            else:
                grid[i][j]= 0
            # remove the value from the grid
            # white color background
            window.fill((255, 255, 255))
            draw_grid()
            highlighted_box()
            pygame.display.update()   
    # if there is no valid value it will return back
    return False 
   
#citation4
# Display instruction for the game in the pygame window
def instruction():
    #instruction on how to reset the board
    reset_board = instructfont.render("Press D to reset the board", 1, (0, 0, 0))
    #instruction on how to either find the full solution or check if your answer is correct
    solution_board = instructfont.render("Press ENTER to check answer or give solution", 1, (0, 0, 0))
    # draw the text onto the grid/screen
    window.blit(reset_board, (20, 520)) 
    # draw the text onto the grid/screen
    window.blit(solution_board, (20, 540))
 
#citation 4 
#display the inputs and solution
def result():
    #message that appears when the game is complete/finished
    complete_msg = numbersfont.render("Finished: Press D to reset", 1, (0, 0, 0))
    # draw the text onto the grid/screen
    window.blit(complete_msg, (20, 570)) 
#set up the variables for the input numbers
correct_f = 0
incorrect_f = 0
rs = 0
error = 0
# main loop which starts everything up and runs the event loop
while True:
     
    # White color background
    window.fill((255, 255, 255))
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False 
        # using the mouse to get to the highlighted position on the sudoku board
        if event.type == pygame.MOUSEBUTTONDOWN:
            correct_f = 1
            position = pygame.mouse.get_pos()
            coordinate(position)
        # user inserts the number   
        # detect if a key is physically pressed down or released using keydown
        if event.type == pygame.KEYDOWN:
            #use left arrow key to move the highlighted box
            if event.key == pygame.K_LEFT:
                x-= 1
                correct_f = 1
            #use right arrow key to move the highlighted box
            if event.key == pygame.K_RIGHT:
                x+= 1
                correct_f = 1
            #use up arrow key to move the highlighted box
            if event.key == pygame.K_UP:
                y-= 1
                correct_f = 1
            #use down arrow key to move the highlighted box
            if event.key == pygame.K_DOWN:
                y+= 1
                correct_f = 1   
            #press down 1 to input it in the grid
            if event.key == pygame.K_1:
                value = 1
            #press down 2 to input it in the grid
            if event.key == pygame.K_2:
                value = 2   
            #press down 3 to input it in the grid
            if event.key == pygame.K_3:
                value = 3
            #press down 4 to input it in the grid
            if event.key == pygame.K_4:
                value = 4
            #press down 5 to input it in the grid
            if event.key == pygame.K_5:
                value = 5
            #press down 6 to input it in the grid
            if event.key == pygame.K_6:
                value = 6
            #press down 7 to input it in the grid
            if event.key == pygame.K_7:
                value = 7
            #press down 8 to input it in the grid
            if event.key == pygame.K_8:
                value = 8
            #press down 9 to input it in the grid
            if event.key == pygame.K_9:
                value = 9 
            if event.key == pygame.K_RETURN:
                incorrect_f = 1  
            # If D is pressed reset the board to default
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                incorrect_f = 0
                #citation 1 
                response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
                grid = response.json()['board']  
    #message based on whether or not the board is correct
    if incorrect_f == 1:
        if solver(grid, 0, 0)== False:
            error = 1
        else:
            rs = 1
            incorrect_f = 0 
    #messages based on whether or not the board is correct
    if value != 0:           
        create_val(value)
        if correct_board(grid, int(x), int(y), value)== True:
            grid[int(x)][int(y)]= value
            flag1 = 0
        else:
            grid[int(x)][int(y)]= 0
            error_wrong()  
        value = 0   
    #print out the error message
    if error == 1:
        error_wrong() 
    #print out finishing message 
    if rs == 1:
        result()       
    draw_grid() 
    #print out the instructions 
    if correct_f == 1:
        highlighted_box()      
    instruction()   
 
#citation 1
    # Update window
    pygame.display.update()

 
# Quit pygame window   
pygame.quit()


# In[ ]:




