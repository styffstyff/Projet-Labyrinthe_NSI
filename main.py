"""
Main module
"""

import maze

maze_example=maze.open_maze('./maze.txt')
for e in maze_example:
    print(e)
