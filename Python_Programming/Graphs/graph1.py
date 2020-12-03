class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex] = []

    def addEdge(self, vertex1, vertex2):
        self.adjacencyList[vertex1].append(vertex2)
        self.adjacencyList[vertex2].append(vertex1)

    def removeEdge(self, vertex1, vertex2):

        # Good use for a lambda function
        self.adjacencyList[vertex1] = list(
            filter(lambda vertex: vertex != vertex2, self.adjacencyList[vertex1]))
        self.adjacencyList[vertex2] = list(
            filter(lambda vertex: vertex != vertex1, self.adjacencyList[vertex2]))

    def removeVertex(self, vertex):
        del_vertex = self.adjacencyList[vertex]

        for city in del_vertex:
            self.removeEdge(vertex, city)

        # delete teh vertex
        del self.adjacencyList[vertex]

    def dfsRecursive(self, start):
        # Store results here
        endResults = []
        # Mark node as visited
        visited = {}
        adjacencyList = self.adjacencyList

        # Helper function called recursively
        def dfs(vertex):
            if vertex is None:
                return None
            visited[vertex] = True
            # store results
            endResults.append(vertex)
            for neighbor in adjacencyList[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(start)
        return endResults

    def dfsIterative(self, start):
        # create a stack to store vertex and neighbors
        stack_arr = [start]
        visited = {}
        results = []
        popped_vertex = None
        visited[start] = True

        while len(stack_arr) != 0:
            popped_vertex = stack_arr.pop()
            # append popped verted to results
            results.append(popped_vertex)
            # check neighbors
            for neighbor in self.adjacencyList[popped_vertex]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    stack_arr.append(neighbor)
        return results

    def displayGraph(self):
        for city, route in self.adjacencyList.items():
            print(city, route)


if __name__ == "__main__":
    g = Graph()
    g.addVertex("Dallas")
    g.addVertex("Tokyo")
    g.addVertex("Aspen")
    g.addVertex("Los Angeles")
    g.addVertex("Hong Kong")
    g.addEdge("Hong Kong", "Tokyo")
    g.addEdge("Dallas", "Aspen")
    g.addEdge("Dallas", "Tokyo")
    g.addEdge("Hong Kong", "Dallas")
    g.addEdge("Los Angeles", "Hong Kong")
    g.addEdge("Los Angeles", "Aspen")
    g.displayGraph()
    # g.removeEdge("Hong Kong", "Dallas")
    # print("\n------Remove Edge--------")
    # g.displayGraph()
    print("\n------Remove Vertex--------")
    g.removeVertex('Hong Kong')
    g.displayGraph()

    print("-------Graph 2------------")
    g2 = Graph()
    g2.addVertex("A")
    g2.addVertex("B")
    g2.addVertex("C")
    g2.addVertex("D")
    g2.addVertex("E")
    g2.addVertex("F")
    g2.addEdge("A", "B")
    g2.addEdge("A", "C")
    g2.addEdge("B", "D")
    g2.addEdge("C", "E")
    g2.addEdge("D", "E")
    g2.addEdge("D", "F")
    g2.addEdge("E", "F")
    g2.displayGraph()
    print(g2.dfsRecursive("A"))
    print(g2.dfsIterative("A"))
    print("Lambda Example")
    arr = ['a', 'b', 'c', 'a', 'a', 'e']
    print(list(filter(lambda a: a != 'a', arr)))
