def make_graph(laby):
  for i in range(len(laby)):
    for j in range(len(laby[i])):
      if laby[i][j] == 2:
        entree = (i, j)
      elif laby[i][j] == 3:
        sortie = (i, j)
  graph = {}
  noeud_suiv(laby, graph, entree)
  return


def noeud_suiv(laby, graph, noeud, noeud_precedent=None):
  if laby[noeud[0],noeud[1]] == 3:
    graph[noeud] = None
    return graph
  nord = (noeud[0], noeud[1]-1)
  sud = (noeud[0], noeud[1]+1)
  est = (noeud[0]+1, noeud[1])
  ouest = (noeud[0]-1, noeud[1])
  if [laby[nord], laby[sud], laby[est], laby[ouest]].count(1) == 3:
    graph[noeud] = None
    return graph
  graph[noeud] = None
  if nord == 0 or nord == 3:
    if noeud_precedent == (nord):
      pass
    else:
      graph[noeud]=nord
      noeud_suiv(laby, graph, nord, noeud)
  if sud == 0 or sud == 3:
    if noeud_precedent == (sud):
      pass
    else:
      if graph[noeud]==None:
        graph[noeud]=sud
      else:
        graph[noeud]=graph[noeud], sud
      noeud_suiv(laby, graph, sud, noeud)
  if est == 0 or est == 3:
    if noeud_precedent == (est):
      pass
    else:
      if graph[noeud]==None:
        graph[noeud]=est
      else:
        graph[noeud]=graph[noeud], est
      noeud_suiv(laby, graph, est, noeud)
  if ouest == 0 or ouest == 3:
    if noeud_precedent == (ouest):
      pass
    else:
      if graph[noeud]==None:
        graph[noeud]=ouest
      else:
        graph[noeud]=graph[noeud], ouest
      noeud_suiv(laby, graph, ouest, noeud)
  return graph


if '__name__' == __main__:
  laby = [[1, 1, 1, 1, 1, 1], [2, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 1], [1, 1, 1, 1, 3, 1]]
  print(make_graph(laby))
