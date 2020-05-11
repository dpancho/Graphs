"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
# class Queue():
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, value):
#         self.queue.append(value)
#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None
#     def size(self):
#         return len(self.queue)

# class Stack():
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None
#     def size(self):
#         return len(self.stack)


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set() #set of edges

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else: 
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)

        #Keep track of visited nodes
        visited = set()

        #Repeat until queue is empty
        while q.size() > 0:
            #dequeue first vert
            v = q.dequeue()

            #if its not visited: 
            if v not in visited:
                print(v)

                #mark visited
                visited.add(v)

                for next_vert in  self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        # push the starting_vertex onto the stack
        stack.push(starting_vertex)
        # create a visited set
        visited = set()
        # while our stack isn't empty:
        while stack.size() > 0:
        ## pop off what's on top, this is our current_node
            current_node = stack.pop()
        ## if it hasn't been visited:
            if current_node not in visited:
                print(current_node)
                ### mark it as visited
                visited.add(current_node)
                ### get its neighbors
                neighbors = self.get_neighbors(current_node)
                ### and add each neighbor to the top of the stack
                for neighbor in neighbors:
                    stack.push(neighbor)
        return visited

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Initial Case
        if visited is None:
            visited = set()

        # Track visited vertices
        visited.add(starting_vertex)

        # Print vertex
        print(starting_vertex)

        # Call the function on neighbors
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a empty queue, and enqueue a PATH to the starting vertex (list)
        q = Queue()
        q.enqueue([starting_vertex])

        # create a set for visited vertices
        visited_vertices = set()
        paths = []

        # while the queue is not empty
        while q.size() > 0:

            # dequeue the first PATH
            path = q.dequeue()

            # grab the last vertex in the path
            current_vertex = path[-1]

            # if it hasn't been visited
            if current_vertex not in visited_vertices:

                # check if its the target
                if current_vertex == destination_vertex:
                    # Return the path
                    return path

                # mark it as visited
                visited_vertices.add(current_vertex)

                # make new versions of the current path, with each neighbor added to them
                for neighbor in self.get_neighbors(current_vertex):
                    # duplicate the path
                    new_path = list(path)
                    # add the neighbor
                    new_path.append(neighbor)
                    # add the new path to the queue
                    q.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a plan_to_visit stack and add starting_vertex to it
        stack = Stack()
        stack.push([starting_vertex])

        # create a Set for visited_vertices
        visited_vertices = set()

        # while the plan_to_visit stack is not Empty:
        while stack.size() > 0:

            # pop the first vertex from the stack
            path = stack.pop()
            # Get current_vertex
            current_vertex = path[-1]

            # if its not been visited
            if current_vertex not in visited_vertices:

                # check if its the target
                if current_vertex == destination_vertex:
                    # Return the path
                    return path

                # mark it as visited, (add it to visited_vertices)   
                visited_vertices.add(current_vertex)

                # add all unvisited neighbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    # duplicate the path
                    new_path = list(path)
                    # add the neighbor
                    new_path.append(neighbor)
                    # add the new path to the queue
                    stack.push(new_path)


    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Initial Case
        if visited is None:
            visited = set()
        if path is None:
            path = []

        # Track visited vertices
        visited.add(starting_vertex)

        # Add to path
        path = path + [starting_vertex]

        # If at destination_vertex return the path
        if starting_vertex == destination_vertex:
            return path

        # Call the function on neighbors
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                # Look for a path
                neighbor_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                # Return only if there is a path
                if neighbor_path:
                    return neighbor_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print("Verticies")
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print('BFT PATHS')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('DFT PATHS')
    graph.dft(1)
    print('DFT RECURSIVE PATHS')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('BFS PATHS Expect [1 ,2, 4, 6]')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('DFS PATHS Expect [1 ,2, 4, 6] or [1, 2, 4, 7, 6]')
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
