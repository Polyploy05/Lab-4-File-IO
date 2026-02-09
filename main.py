''' Name: Jacob Miranda
### Date:
### Group:
### Description:  '''

import check_input
import maze

def read_maze():
  maze = []
  with open( , 'r') as f:
    for line in f:
      row = list(line.rstrip(\n'))
                 if row:
                             maze.append(row)
  return maze                          
