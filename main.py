''' 
Name: Jacob Miranda & Daniel Puerto
Date: 02/11/26 
Group: 17
Description: Create a program that allows the user to solve a maze that is 
read in from a file. The program should incorporate a loop that will continually 
ask the user to move in a direction until the user completes the maze.  '''


import check_input

def read_maze():
  '''Takes the provided Maze text file and puts it into a 2D list.'''
  maze = []
  with open("maze.txt", 'r') as f: # put maze file
    #Copies all maze elements into a fresh 2D list
    for line in f:
        row = list(line.rstrip('\n'))
        if row:
            maze.append(row)
  return maze                          



def find_start(maze):
  #Iterates through maze until finding the starting point, then returns it as an Array
  for r in range(len(maze)):
    for c in range(len(maze[r])):
      if maze[r][c] == 's':
        return [r, c]
  return None
  

def display_maze(maze, loc):
    '''Prints out the maze in a more readable format with different lines for each row.'''
    user_r, user_c = loc
    for r in range(len(maze)):
      row_str = ""
      for c in range(len(maze[r])):
        if r == user_r and c == user_c:
          row_str += "X"
        else:
          row_str += maze[r][c]
      print(row_str)



def main():
    '''Main game. Sets up a loop where the user continuously inputs a direction to move in. 
    A move is succesful if there is no wall in the way. Checks every time to ensure that the 
    current position is not the finish area, and ends the loop if so.'''

    #Obtains the maze text file and sets up initializes variables for position and play condition 
    maze = read_maze()
    pos = find_start(maze) 
    solved = False
    X = 0
    Y = 0
    print('-Maze Solver-')
    while not solved: 
      #Maze UI
      display_maze(maze, pos)
      print("1: Go up")
      print("2: Go down")
      print("3: Go left")
      print("4: Go right")
      
      #Gets the user's movement choice, as well as their current position in X/Y coordinates
      direction = check_input.get_int_range("Enter direction: ", 1, 4)
      for r in range(len(maze)):
        for c in range(len(maze[r])):
            if [r, c] == pos:
              Y = r
              X = c
      
      #Checks the coresponding direction to see if there is a wall. If not, updates current position
      if direction == 1 and maze[Y-1][X] != '*':
        pos = [Y - 1, X]
      elif direction == 2 and maze[Y + 1][X] != '*':
        pos = [Y + 1,X]
      elif direction == 3 and maze[Y][X-1] != '*':
        pos = [Y, X -1]
      elif direction == 4 and maze[Y][X + 1] != '*':
        pos = [Y, X + 1]
      else:
         print("You cannot move there")

      #Clear condition check.
      if maze[pos[0]][pos[1]] == 'f':
        solved = True
    print("Congratulations! You solved the maze.")
      

main()

