"use strict";

class Graph {
	constructor() {
		this.adjacencyList = {};
	}

	addVertex(vertex) {
		if (!this.adjacencyList[vertex]) {
			this.adjacencyList[vertex] = [];
		}
	}

	addEdge(vertex1, vertex2) {
		if (this.adjacencyList[vertex1]) {
			this.adjacencyList[vertex1].push(vertex2);
			this.adjacencyList[vertex2].push(vertex1);
		}
	}

	removeEdge(vertex1, vertex2) {
		this.adjacencyList[vertex1] = this.adjacencyList[vertex1].filter(
			(vertex) => vertex !== vertex2
		);

		this.adjacencyList[vertex2] = this.adjacencyList[vertex2].filter(
			(vertex) => vertex !== vertex1
		);
	}

	removeVertex(vertex) {
		const del_vertex = this.adjacencyList[vertex];
		del_vertex.forEach((city) => this.removeEdge(vertex, city));
		delete this.adjacencyList[vertex];

		// while (this.adjacencyList[vertex].length) {
		// 	const del_vertex = this.adjacencyList[vertex].pop();
		// 	this.removeEdge(vertex, del_vertex);
		// }
	}

	dfsRecursive(start) {
		const endResult = [];
		const visited = {};
		// Store adjacency list in variable becasue inside of the IIFE "this" will be refering to IEFF
		const adjacencyList = this.adjacencyList;
		(function dfs(vertex) {
			if (!vertex) {
				return null;
			}
			visited[vertex] = true;
			endResult.push(vertex);
			adjacencyList[vertex].forEach((neighbor) => {
				if (!visited[neighbor]) {
					dfs(neighbor);
				}
			});
		})(start); // invoke it with start

		return endResult;
	}

	dfsIterative(start) {
		const stack_arr = [];
		stack_arr.push(start);
		const results = [];
		const visited = {}; // set visited vertex to true

		let vertex;
		visited[start] = true;
		// as long as stack is not empty
		while (stack_arr.length !== 0) {
			vertex = stack_arr.pop();
			results.push(vertex);

			this.adjacencyList[vertex].forEach((neighbor) => {
				if (!visited[neighbor]) {
					visited[neighbor] = true;
					stack_arr.push(neighbor);
				}
			});
		}

		return results;
	}
}

const g = new Graph();
g.addVertex("Dallas");
g.addVertex("Tokyo");
g.addVertex("Aspen");
g.addVertex("Los Angeles");
g.addVertex("Hong Kong");
g.addEdge("Hong Kong", "Tokyo");
g.addEdge("Dallas", "Aspen");
g.addEdge("Dallas", "Tokyo");
g.addEdge("Hong Kong", "Dallas");
g.addEdge("Los Angeles", "Hong Kong");
g.addEdge("Los Angeles", "Aspen");
// g.removeEdge("SEA", "HOU");
// g.removeVertex("Hong Kong");
const g2 = new Graph();
g2.addVertex("A");
g2.addVertex("B");
g2.addVertex("C");
g2.addVertex("D");
g2.addVertex("E");
g2.addVertex("F");
g2.addEdge("A", "B");
g2.addEdge("A", "C");
g2.addEdge("B", "D");
g2.addEdge("C", "E");
g2.addEdge("D", "E");
g2.addEdge("D", "F");
g2.addEdge("E", "F");
// g2.dfsRecursive("A");
