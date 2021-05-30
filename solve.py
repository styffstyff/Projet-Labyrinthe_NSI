from copy import deepcopy
import graph

def go_N(pos): return (pos[0]-1, pos[1])
def go_S(pos): return (pos[0]+1, pos[1])
def go_E(pos): return (pos[0], pos[1]+1)
def go_W(pos): return (pos[0], pos[1]-1)

def vertices_to_path(vertices):
    """
    Translates from list of vertices to path ("NSEW").
    :return str: path ("NSEW") from `vertices[0]` to `vertices[-1]`
    """
    path = ""
    for idx, pos in enumerate(vertices[:-1]):
        next_pos = vertices[idx+1]
        while pos != next_pos:
            if pos[0] < next_pos[0]:
                pos = go_S(pos)
                path += "S"
            elif pos[0] > next_pos[0]:
                pos = go_N(pos)
                path += "N"
            elif pos[1] < next_pos[1]:
                pos = go_E(pos)
                path += "E"
            elif pos[1] > next_pos[1]:
                pos = go_W(pos)
                path += "W"
    return path

def dead_end_filling(G, start, end):
    """
    Dead-end filling algorithm :
    https://en.wikipedia.org/wiki/Maze-solving_algorithm#Dead-end_filling
    The idea is to delete vertices that do not lead to any vertex.
    Maze must have only one solution.
    :return str: the solution of the labyrinth
    """
    G = deepcopy(G)
    stop = False
    while not stop:
        stop = True
        # usage of `list(G)` instead of `G.keys()`
        # to avoid `RuntimeError: dictionary changed size during iteration`
        for k in list(G):
            if len(G[k]) <= 1 and k != start and k != end:
                graph.del_vertex(G, k)
                stop = False
    # translate from graph to a list of vertices
    pos = start
    vertices = [pos]
    while pos != end:
        assert len(G[pos]) <= 2, "Maze unsolvable using dead_end_filling algorithm."
        next_pos = list(G[pos])[0]
        if next_pos in vertices:
            next_pos = list(G[pos])[1]
        vertices.append(next_pos)
        pos = next_pos

    return vertices_to_path(vertices)

def depth_first_search(G, start, end, cur_vertex=None, visited=None, path=None):
    """
    depth-first search algorithm.
    Follow a path util its end.
    If it leads to a dead-end, choose another path.
    If it leads to the end of the maze, return this path.
    :return str: the solution of the maze
    """
    if cur_vertex is None:
        cur_vertex = start
    if visited is None:
        visited = set()
    if path is None:
        path = list()

    visited.add(cur_vertex)
    path.append(cur_vertex)

    if cur_vertex == end:
        return vertices_to_path(path)

    if not G[cur_vertex].difference(visited):
        return

    # iterates on each adjacent vertex that has not already been visited
    for vertex in G[cur_vertex].difference(visited):
        res = depth_first_search(G, start, end, vertex, visited, path)
        if res:
            return res

def check(maze, start, end, solution):
    pos = start
    for direction in solution:
        if direction == 'N':
            pos = go_N(pos)
        elif direction == 'S':
            pos = go_S(pos)
        elif direction == 'E':
            pos = go_E(pos)
        else:
            pos = go_W(pos)

        if maze[pos[0]][pos[1]] == 1:
            return False

    if pos == end:
        return True
    return False


if __name__ == "__main__":
    import make_graph

    """
    [[1, 1, 1, 1, 1, 1],
     [2, 0, 1, 1, 0, 1],
     [1, 0, 0, 0, 0, 1],
     [1, 1, 0, 1, 1, 1],
     [1, 0, 0, 0, 0, 1],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 1, 1, 3, 1]]
    """

    start = (1, 0)
    end = (6, 4)

    G = graph.new_graph()
    graph.add_vertex(G, start)
    graph.add_vertex(G, (1, 1))
    graph.add_vertex(G, (2, 1))
    graph.add_vertex(G, (2, 2))
    graph.add_vertex(G, (2, 4))
    graph.add_vertex(G, (1, 4))
    graph.add_vertex(G, (4, 2))
    graph.add_vertex(G, (4, 1))
    graph.add_vertex(G, (5, 1))
    graph.add_vertex(G, (4, 4))
    graph.add_vertex(G, end)

    graph.add_arc(G, start, (1, 1))
    graph.add_arc(G, (1, 1), (2, 1))
    graph.add_arc(G, (2, 1), (2, 2))
    graph.add_arc(G, (2, 2), (2, 4))
    graph.add_arc(G, (2, 4), (1, 4))
    graph.add_arc(G, (2, 2), (4, 2))
    graph.add_arc(G, (4, 2), (4, 1))
    graph.add_arc(G, (4, 1), (5, 1))
    graph.add_arc(G, (4, 2), (4, 4))
    graph.add_arc(G, (4, 4), end)

    assert dead_end_filling(G, start, end) == "ESESSEESS"
    assert depth_first_search(G, start, end) == "ESESSEESS"

    laby = [[1, 1, 1, 1, 1, 1],
            [2, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1],
            [1, 1, 1, 1, 3, 1]]

    start = (1, 0)
    end = (6, 4)

    G = make_graph.make_graph(laby)

    solution = depth_first_search(G, start, end)
    assert check(laby, start, end, solution)
