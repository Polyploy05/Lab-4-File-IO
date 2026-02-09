''' Name: Jacob Miranda
### Date:
### Group:
### Description:  '''

import check_input
import maze

def read_maze(): #put maze file
  maze = []
  with open( , 'r') as f: # put maze file
    for line in f:
      row = list(line.rstrip(\n'))
                 if row:
                             maze.append(row)
  return maze                          



def find_start(maze):
  for r in range(len(maze)):
    for c in range(len(maze[r])):
      in maze[r][c] == 's'
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
