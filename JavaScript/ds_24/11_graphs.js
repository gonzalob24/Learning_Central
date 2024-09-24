// Edge list: shows the connections
const graph = [[0, 1], [2, 3], [2, 1], 1, 3];

// adjacent list
const graph_2 = [[2], [2, 3], [0, 1, 3], [1, 2]];

// Adjacent Matrix
const graph_3 = [
	[0, 0, 1, 0],
	[0, 0, 1, 1],
	[1, 1, 0, 1],
	[0, 1, 1, 0],
];

class Graph {
	constructor() {
		this.num_of_nodes = 0;
		this.adjacent_list = {};
	}

	add_vertex(node) {
		this.adjacent_list[this.num_of_nodes] = node;
		this.num_of_nodes++;
	}

	add_edge() {}

	show_connections() {}
}

const my_graph = new Graph();
my_graph.add_vertex('0');
my_graph.add_vertex('1');
my_graph.add_vertex('2');
my_graph.add_vertex('3');
my_graph.add_vertex('4');
my_graph.add_vertex('5');
my_graph.add_vertex('6');
my_graph.add_edge('3', '1');
my_graph.add_edge('3', '4');
my_graph.add_edge('4', '2');
my_graph.add_edge('4', '5');
my_graph.add_edge('1', '2');
my_graph.add_edge('1', '0');
my_graph.add_edge('0', '3');
my_graph.add_edge('0', '5');
console.log(my_graph);
