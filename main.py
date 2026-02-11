''' Name: Jacob Miranda & Daniel Puerto
### Date: 02/11/26 
### Group: 17
### Description: Create a program that allows the user to solve a maze that is read in from a file.  The program should incorporate a loop that will continually ask the user to move in a direction until the user completes the maze.  '''

import check_input
maze = open("maze.txt") # put maze file


def read_maze(): #put maze file
  maze = []
  with open("maze.txt", 'r') as f: # put maze file
    for line in f:
        row = list(line.rstrip('\n'))
        if row:
            maze.append(row)
  return maze                          



def find_start(maze):
  for r in range(len(maze)):
    for c in range(len(maze[r])):
      if maze[r][c] == 's':
        return [r, c]
  return None
  
def display_maze(maze, loc):
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
    pos = find_start(read_maze()) 
    display_maze(read_maze(), pos)
    solved = False
    while not solved: 
        print("1: Go up /n2: Go down /n3: Go left /n4: Go right")
        direction = check_input.get_int_range("Enter direction:", 1, 4)
        for r in range(len(maze)):
          for c in range(len(maze[r])):
             if maze[r][c] == 'X':
                x = r
                y = c
        if direction == 1 and x > 0 and maze[x-1][y] != '#':
          pos = [x - 1, y]

main()
