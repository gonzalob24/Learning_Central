class PriorityQueue():
    def __init__(self):
        self.values = []

    def enqueue(self, value, priority):
        self.values.append({"value": value, "priority": priority})
        self.values = sorted(self.values, key=lambda node: node["priority"])

    def dequeue(self):
        return self.values.pop(0)

    def display(self):
        # for obj in self.values:
        # print(f'{obj["value"]}:{obj["priority"]}').
        index = 0
        while index < len(self.values):
            vertex = self.values[index]
            print(f'{vertex["value"]}:{vertex["priority"]}')
            index += 1


class WeightedGraph:
    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex] = []

    def addEdge(self, vertex1, vertex2, weight):
        self.adjacencyList[vertex1].append({"node": vertex2, "weight": weight})
        self.adjacencyList[vertex2].append({"node": vertex1, "weight": weight})

    def dijkstra(self, start, end):
        nodes = PriorityQueue()
        distances = {}
        previous = {}  # store quickest paths to current node from pevious

        # initial state: loop over adjacency list and initialize distances start=0 and rest= inf
        for vertex in self.adjacencyList:
            if vertex == start:
                distances[vertex] = 0
                # 1. add vertex with priority
                nodes.enqueue(vertex, 0)
            else:
                distances[vertex] = float('inf')
                nodes.enqueue(vertex, float('inf'))

            previous[vertex] = None

        smallest = None
        # as long as nodes has an item in it
        while len(nodes.values) > 0:
            # dequeue a vertex and get smallest priority
            smallest = nodes.dequeue()["value"]
            if smallest == end:
                # Finished
                # build path to return at the end
                pass
            if (smallest != 'inf' or distances[smallest] != 'inf'):
                for neighbor in self.adjacencyList[smallest]:
                    # find neighboring node
                    nextNode = self.adjacencyList[smallest][neighbor]
                    # calc distance to neighboring node
                    candidate = distances[smallest] + nextNode["weight"]
                    nextNeighbor = nextNode["node"]

                    if candidate < distances[nextNeighbor]:
                        distances[nextNeighbor] = candidate
                        previous[nextNeighbor] = smallest
                        nodes.enqueue(nextNeighbor, candidate)

        return smallest

    def display(self):
        for vertex, neighbors in self.adjacencyList.items():
            print(f'{vertex}: {neighbors}')


wg = WeightedGraph()
wg.addVertex("A")
wg.addVertex("B")
wg.addVertex("C")
wg.addVertex("D")
wg.addVertex("E")
wg.addVertex("F")

wg.addEdge("A", "B", 4)
wg.addEdge("A", "C", 2)
wg.addEdge("B", "E", 3)
wg.addEdge("C", "D", 2)
wg.addEdge("C", "F", 4)
wg.addEdge("D", "E", 3)
wg.addEdge("D", "F", 1)
wg.addEdge("E", "F", 1)
wg.display()

print(wg.dijkstra("A", "E"))
