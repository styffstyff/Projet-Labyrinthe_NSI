import graph

go_N = lambda pos: (pos[0]-1, pos[1])
go_S = lambda pos: (pos[0]+1, pos[1])
go_E = lambda pos: (pos[0], pos[1]+1)
go_W = lambda pos: (pos[0], pos[1]-1)

def dead_end_filling(G, start, end):
    """
    Dead-end filling algorithm : https://en.wikipedia.org/wiki/Maze-solving_algorithm#Dead-end_filling
    The idea is to delete vertices that do not lead to any vertex.
    :return string: the solution of the labyrinth
    """
    stop = False
    while not stop:
        stop = True
        # usage of `list(G)` instead of `G.items()`
        # to avoid `RuntimeError: dictionary changed size during iteration`
        for k in list(G):
            if G[k] == set() and k != end:
                graph.del_vertex(G, k)
                stop = False

    # translate from graph to path
    pos = start
    path = ""
    while pos != end:
        assert len(G[pos]) == 1, "Maze unsolvable using dead_end_filling algorithm."
        next_pos = list(G[pos])[0]
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

if __name__ == "__main__":
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
