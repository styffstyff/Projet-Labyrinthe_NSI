"""
Main module
"""

import maze
from make_graph import make_graph
import solve

maze_example, start, exit = maze.open_maze('./maze.txt')
graph = make_graph(maze_example)

solution = solve.dead_end_filling(graph, start, exit)


print(solution)

        
solve.check(maze_example, solution, start, exit)
        
