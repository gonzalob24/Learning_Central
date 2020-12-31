import sys
sys.path.insert(0, '/home/gonzalo/Documents/git/Learning_Central/Python_Programming/LinkedLists')
from edu_linked_list import LinkedList


class Graph():
    def __init__(self, vertices):
        # set the number of vertices
        self.vertices = vertices
        self.array = []
        # Creating a new LinkedList for each vertex/index of the list
        for item in range(vertices):
            temp = LinkedList()
            self.array.append(temp)

    def add_edge(self, source, destination):
        # add an edge
        if source < self.vertices and destination < self.vertices:
            # for directed graph use only this line
            self.array[source].insert_at_head(destination)
            # use this line as well for undirected graph
            # self.array[destination].insert_at_head(source)

            # If I were to implement an Undirected Graph i.e (1,0) == (0,1)
            # I would create an edge from destination towards source as well
            # i.e self.list[destination].insertAtHead(source)
    def bfs(self):
        result = ""
        num_of_vertices = self.vertices
        # Write - Your - Code
        queue = MyQueue()
        sta
        # For the above graph, it should return "01234" or "02143" etc
        return result

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        print
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")


g = Graph(3)
g.print_graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.print_graph()
