# adj_arr = [[1,2], [0], [3,8],[0,4,5,2],[3,6],[3],[4,7],[6],[2]]
adj_arr = [[1,3], [0], [3,8],[0,4,5,2],[3,6],[3],[4,7],[6],[2]]

def bfs_traversal(graph):
  q = [0]
  values = []
  seen_vertices = {}
  
  while len(q) > 0:
    vertex = q.pop(0)
    values.append(vertex)
    seen_vertices[vertex] = True
    connections = graph[vertex]
    for i in range(len(connections)):
      connection = connections[i]
      if not seen_vertices.get(connection):
        q.append(connection)
  return values

def dfs_traversal(vertex, graph, seen, values):
  values.append(vertex)
  seen[vertex] = True
      
  connections = graph[vertex]
  for i in range(len(connections)):
    connection = connections[i]
    if not seen.get(connection):
      dfs_traversal(connection, graph, seen, values)
  
  return values

print(bfs_traversal(adj_arr))
print(dfs_traversal(0, adj_arr, {}, []))