"""
Graph implementation with the set of successors.
"""

def new_graph():
    """
    Creates a new graph.
    :return dict: empty graph
    """
    return dict()

def is_vertex(G, v):
    """
    :return bool: true if k is an existing vertex
    """
    return v in G.keys()

def add_vertex(G, v):
    """
    Adds the vertex `v` to the graph `G`.
    The vertex `v` must not already be present in the graph `G`.
    :return None:
    """
    assert not is_vertex(G, v), "Can't add a vertex : the vertex already exists."
    G[v] = set()

def is_arc(G, v1, v2):
    """
    The vertex `v1` must already be present in the graph `G`.
    :return bool: true if an arc exists between `v1`and v2`
    """
    assert is_vertex(G, v1), "The vertex `v1`doesn't exist."
    return v2 in G[v1]

def del_vertex(G, v):
    """
    Deletes the vertex `v` from the graph `G` and all its arcs.
    The vertex `v` must already be present in the graph `G`.
    :return None:
    """
    assert is_vertex(G, v), "Can't delete the vertex : the vertex doesn't exist."
    del G[v] # delete the list of its successors (outgoing arcs)
    for key in G.keys():
        if is_arc(G, key, v):
            G[key].remove(v) # delete incomming arcs

def add_arc(G, v1, v2):
    """
    Adds to the graph `G` an arc from `v1` to `v2`.
    The vertex `v1` must already be present in the graph `G`.
    The vertex `v2` must already be present in the graph `G`.
    :return None:
    """
    assert is_vertex(G, v1), "Can't add an arc : the vertex v1 doesn't exist."
    assert is_vertex(G, v2), "Can't add an arc : the vertex v2 doesn't exist."
    G[v1].add(v2)

def del_arc(G, v1, v2):
    """
    Deletes from the graph `G` the arc from `v1` to `v2`.
    The arc `v1 -> v2` must already exist in the graph `G`.
    :return None:
    """
    assert is_arc(G, v1, v2), "Can't delete an arc : the arc doesn't exist."
    G[v1].remove(v2)

def successors(G, v):
    """
    :return set: the set of successors of `v`
    """
    return G[v]

if __name__ == "__main__":
    G = new_graph()
    for v in ["A", "B", "C"]:
        add_vertex(G, v)

    assert G == {"A":set(), "B":set(), "C":set()}
    assert is_vertex(G, "A")
    assert is_vertex(G, "B")
    assert is_vertex(G, "C")
    assert not is_vertex(G, "D")

    assert not is_arc(G, "A", "B")

    add_arc(G, "A", "B")
    add_arc(G, "A", "C")
    add_arc(G, "B", "C")
    add_arc(G, "C", "A")

    assert G == {"A":{"B", "C"}, "B":{"C"}, "C":{"A"}}
    assert is_arc(G, "A", "B")
    assert is_arc(G, "A", "C")
    assert is_arc(G, "B", "C")
    assert is_arc(G, "C", "A")
    assert not is_arc(G, "C", "B")

    del_arc(G, "A", "C")

    assert not is_arc(G, "A", "C")

    del_vertex(G, "B")

    assert G == {"A":set(), "C":{"A"}}
