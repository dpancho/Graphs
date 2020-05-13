class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()

    def add_edge(self, child, parent):
        self.nodes[child].add(parent)

    def getNeighbors(self, child):
        return self.nodes[child]

class Stack:
    def __init__(self):
        self.storage = []

    def pop(self):
        return self.storage.pop()

    def push(self, item):
        self.storage.append(item)

    def size(self):
        return len(self.storage)

# Three steps to almost any graphs problem:
## Describe in terms of graphs
#### Nodes: people
#### Edges: if they're parent-child

## To build our graph we:
#### Build a graph class
#### Write a getNeighbors (not an adjacency list or matrix)

## Choose a graph algorithm
#### Traversal or search? No node we're looking for, no node at which we'll just stop, visit all
#### Breadth or depth? DFT

def dft(graph, starting_node):
    s = Stack()

    s.push((starting_node, 0))
    visited = set()
    ## create visited set and pairs
    visited_pairs = set()

    while s.size() > 0:
        current_pair = s.pop()
        visited_pairs.add(current_pair)
        current_node = current_pair[0]
        current_distance = current_pair[1]

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.getNeighbors(current_node)

            for parent in parents:
                parent_distance = current_distance + 1
                s.push((parent, parent_distance))

    longest_distance = 0
    aged_one = -1
    for pair in visited_pairs:
        node = pair[0]
        distance = pair[1]
        if distance > longest_distance:
            longest_distance = distance
            aged_one = node
    return aged_one

def earliest_ancestor(ancestors, starting_node):
    # build our graph
    g = Graph()
    for parent, child in ancestors:
        g.add_node(child)
        g.add_node(parent)
        g.add_edge(child, parent)

    # run dft
    aged_one = dft(g, starting_node)

    # choose the most distant ancestor
    ## run dft but track each path, then choose the longest path
    ## run dft but add each node as a tuple (node, distance)

    return aged_one 
