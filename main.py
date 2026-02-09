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
  
