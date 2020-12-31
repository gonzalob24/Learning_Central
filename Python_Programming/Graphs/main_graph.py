class Graph():
    def __init__(self):
        # Use an adjaceny List to store gfaph
        self.adjacencyList = {}

    def addVertex(self, vertex):
        # Dont add duplicates
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex] = []

    def addEdge(self, vertex1, vertex2):
        if vertex1 not in self.adjacencyList:
            self.adjacencyList[vertex1] = []
        if vertex2 not in self.adjacencyList:
            self.adjacencyList[vertex2] = []

        self.adjacencyList[vertex1].append(vertex2)
        self.adjacencyList[vertex2].append(vertex1)

    def removeEdge(self, vertex1, vertex2):
        self.adjacencyList[vertex1] = list(
            filter(lambda vertex: vertex != vertex2, self.adjacencyList[vertex1]))
        self.adjacencyList[vertex2] = list(
            filter(lambda vertex: vertex != vertex1, self.adjacencyList[vertex2]))

    def removeVertex(self, vertex):
        deleted_vertex = self.adjacencyList[vertex]

        for city in deleted_vertex:
            self.removeEdge(vertex, city)

        del self.adjacencyList[vertex]

    def dfsIterative(self, start):
        # In a stack place vertex and neihbors
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

    def display(self):
        for city, route in self.adjacencyList.items():
            print(city, route)


test = {}
test["Houston"] = []
test["Seattle"] = []
test["Houston"].append("Seattle")
test["Seattle"].append("Houston")
print(test)

somelist = [1, 2, 2, 3, 4]
print(somelist)
# somelist = list(filter(lambda n: n != 2, somelist))
# print(somelist)


def remove(n):
    if n == 2:
        return False
    return True


somelist = list(filter(remove, somelist))
print(somelist)
