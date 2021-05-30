import maze
import graph

def go_N(pos): return (pos[0]-1, pos[1])
def go_S(pos): return (pos[0]+1, pos[1])
def go_E(pos): return (pos[0], pos[1]+1)
def go_W(pos): return (pos[0], pos[1]-1)

def is_in_maze(laby, pos):
    return 0 <= pos[0] < len(laby) and 0 <= pos[1] < len(laby[0])

def make_graph(laby):
    G = graph.new_graph()

    # place vertices
    for y in range(len(laby)):
        for x in range(len(laby[y])):
            if laby[y][x] == 1:
                continue
            if laby[y][x] == 2 or laby[y][x] == 3:
                graph.add_vertex(G, (y, x))
                continue

            pos = (y, x)
            north, south, east, west = 1, 1, 1, 1
            if is_in_maze(laby, go_N(pos)):
                north = laby[go_N(pos)[0]][go_N(pos)[1]]
            if is_in_maze(laby, go_S(pos)):
                south = laby[go_S(pos)[0]][go_S(pos)[1]]
            if is_in_maze(laby, go_E(pos)):
                east = laby[go_E(pos)[0]][go_E(pos)[1]]
            if is_in_maze(laby, go_W(pos)):
                west = laby[go_W(pos)[0]][go_W(pos)[1]]

            if north != south or east != west:
                graph.add_vertex(G, pos)

    for vertex in G.keys():
        pos = vertex
        while is_in_maze(laby, go_N(pos)) and laby[go_N(pos)[0]][go_N(pos)[1]] != 1:
            pos = go_N(pos)
            if pos != vertex and pos in G.keys():
                graph.add_arc(G, vertex, pos)
                break

        pos = vertex
        while is_in_maze(laby, go_S(pos)) and laby[go_S(pos)[0]][go_S(pos)[1]] != 1:
            pos = go_S(pos)
            if pos != vertex and pos in G.keys():
                graph.add_arc(G, vertex, pos)
                break

        pos = vertex
        while is_in_maze(laby, go_E(pos)) and laby[go_E(pos)[0]][go_E(pos)[1]] != 1:
            pos = go_E(pos)
            if pos != vertex and pos in G.keys():
                graph.add_arc(G, vertex, pos)
                break

        pos = vertex
        while is_in_maze(laby, go_W(pos)) and laby[go_W(pos)[0]][go_W(pos)[1]] != 1:
            pos = go_W(pos)
            if pos != vertex and pos in G.keys():
                graph.add_arc(G, vertex, pos)
                break

    return G

if __name__ == "__main__":
    import solve

    laby, start, end = maze.open_maze("./maze.txt")
    G = make_graph(laby)
    assert solve.dead_end_filling(G, start, end)
    assert solve.depth_first_search(G, start, end)
