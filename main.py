"""
Main module
"""

from make_graph import make_graph
import maze
import solve

import random

size = (random.randint(5, 25), random.randint(5, 25))
maze.new_maze("maze.txt", size)
maze_example, start, exit = maze.open_maze('./maze.txt')

print("MAZE :")
for l in maze_example:
    print(l)

graph = make_graph(maze_example, start)

solution = solve.dead_end_filling(graph, start, exit)
if solve.check(maze_example, start, exit, solution):
    print(f"Solution with dead_end_filling : {solution}")
else:
    print("Maze unsolvable using dead_end_filling")


solution = solve.depth_first_search(graph, start, exit)
if solve.check(maze_example, start, exit, solution):
    print(f"Solution with depth_first_search : {solution}")
else:
    print("Maze unsolvable using depth_first_search")
