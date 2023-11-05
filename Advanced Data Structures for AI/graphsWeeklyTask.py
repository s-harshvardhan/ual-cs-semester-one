# This is a useful data structure for implementing 
# a counter that counts the time.
class DFSTimeCounter:
    def __init__(self):
        self.count = 0
    
    def reset(self):
        self.count = 0
    
    def increment(self):
        self.count = self.count + 1
        
    def get(self):
        return self.count 
    
class UndirectedGraph:
    
    # n is the number of vertices
    # we will label the vertices from 0 to self.n -1 
    # Initialize to an empty adjacency list
    # We will store the outgoing edges using a set data structure
    def __init__(self, n):
        self.n = n
        self.adj_list = [ set() for i in range(self.n) ]
        
    def add_edge(self, i, j):
        assert 0 <= i < self.n
        assert 0 <= j < self.n
        assert i != j
        # Make sure to add edge from i to j
        self.adj_list[i].add(j)
        # Also add edge from j to i
        self.adj_list[j].add(i)
        
    # get a set of all vertices that 
    # are neighbors of the
    # vertex i
    def get_neighboring_vertices(self, i):
        assert 0 <= i < self.n
        return self.adj_list[i]
    
    # Function: dfs_visit
    # Program a DFS visit of a graph.
    # We maintain a list of discovery times and finish times.
    # Initially all discovery times and finish times are set to None.
    # When a vertex is first visited, we will set discovery time
    # When DFS visit has processed all the neighbors then 
    # set the finish time.
    # DFS visit should update the list of discovery and finish times in-place
    # Arguments
    #  i --> id of the vertex being visited.
    #  dfs_timer --> An instance of DFSTimeCounter structure provided for you.
    #  discovery --> discovery time of each vertex -- a list of size self.n
    #                None if the vertex is yet to be visited.
    #  finish --> finish time of each vertex -- a list of size self.n
    #                None if the vertex is yet to be finished.
    #  dfs_tree_parent --> the parent for for each node 
    #                       if we visited node j from node i, then j's parent is i.
    #                      Do not forget to set tree_parent when you call dfs_visit 
    #                                                         on node j from node i.
    #  dfs_back_edges --> a list of back edges.
    #                     a back edge is an edge from i to j wherein
    #                     DFS has already discovered j when i is discovered 
    #                                     but not finished j
    
    def dfs_visit(self, i, dfs_timer, discovery_times, finish_times, 
                        dfs_tree_parent, dfs_back_edges):
        assert 0 <= i < self.n
        assert discovery_times[i] == None
        assert finish_times[i] == None
        discovery_times[i] = dfs_timer.get()
        dfs_timer.increment()
        # your code here
        # Sort the neighboring vertices in increasing order
        neighboring_vertices = sorted(self.get_neighboring_vertices(i))
        
        for j in neighboring_vertices:
            if discovery_times[j] is None:
                dfs_tree_parent[j] = i
                self.dfs_visit(j, dfs_timer, discovery_times, finish_times, dfs_tree_parent, dfs_back_edges)
            elif finish_times[j] is None and j != dfs_tree_parent[i]:
                dfs_back_edges.append((i, j))

        finish_times[i] = dfs_timer.get()
        dfs_timer.increment()

    # Function: dfs_traverse_graph
    # Traverse the entire graph.
    # Place this function inside your UndirectedGraph class, for example, after dfs_visit function
    def dfs_traverse_graph(self):
        dfs_timer = DFSTimeCounter()
        discovery_times = [None]*self.n
        finish_times = [None]*self.n
        dfs_tree_parents = [None]*self.n
        dfs_back_edges = []
        for i in range(self.n):
            if discovery_times[i] == None:
                self.dfs_visit(i,dfs_timer, discovery_times, finish_times, 
                               dfs_tree_parents, dfs_back_edges)
        # Clean up the back edges so that if (i,j) is a back edge then j cannot
        # be i's parent.
        non_trivial_back_edges = [(i,j) for (i,j) in dfs_back_edges if dfs_tree_parents[i] != j]
        return (dfs_tree_parents, non_trivial_back_edges, discovery_times, finish_times)

def num_connected_components(g): # g is an UndirectedGraph class
    # your code here
    visited = set()
    num_components = 0

    for vertex in range(g.n):
        if vertex not in visited:
            num_components += 1
            stack = [vertex]

            while stack:
                current_vertex = stack.pop()
                visited.add(current_vertex)

                for neighbor in g.get_neighboring_vertices(current_vertex):
                    if neighbor not in visited:
                        stack.append(neighbor)

    return num_components

# create the graph from problem 1A.
g = UndirectedGraph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,4)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,4)

assert num_connected_components(g) == 1, f' Test A failed: g must have 1 connected component. Your code returns {num_connected_components(g)}'


g2 = UndirectedGraph(7)
g2.add_edge(0,1)
g2.add_edge(0,2)
g2.add_edge(0,4)
g2.add_edge(2,3)
g2.add_edge(2,4)
g2.add_edge(3,4)
g2.add_edge(5,6)

assert num_connected_components(g2) == 2, f' Test B failed: g2 must have 2 connected components. Your code returns {num_connected_components(g2)}'


g3 = UndirectedGraph(8)
g3.add_edge(0,1)
g3.add_edge(0,2)
g3.add_edge(0,4)
g3.add_edge(2,3)
g3.add_edge(2,4)
g3.add_edge(3,4)
g3.add_edge(5,6)

assert num_connected_components(g3) == 3, f' Test C failed: g3 must have 3 connected components. Your code returns {num_connected_components(g3)}'

g3.add_edge(7,5)
assert num_connected_components(g3) == 2, f' Test D failed: g3 must now have 2 connected components. Your code returns {num_connected_components(g3)}'

print('All tests passedd: 10 points!')

def find_all_nodes_in_cycle(g):
    def dfs(node, parent, current_path, visited):
        visited.add(node)
        current_path.append(node)

        for neighbor in g.get_neighboring_vertices(node):
            if neighbor == parent:
                continue  # Skip the parent in an undirected graph
            if neighbor in current_path:
                # Found a cycle, add all nodes in the cycle to the result set
                cycle_start = current_path.index(neighbor)
                set_of_nodes.update(current_path[cycle_start:])
            if neighbor not in visited:
                dfs(neighbor, node, current_path, visited)

        current_path.pop()

    set_of_nodes = set()
    visited = set()
    current_path = []

    for node in range(g.n):
        if node not in visited:
            dfs(node, None, current_path, visited)

    return set_of_nodes

#this is the example that we had for the problem.
g3 = UndirectedGraph(8)
g3.add_edge(0,1)
g3.add_edge(0,2)
g3.add_edge(0,4)
g3.add_edge(2,3)
g3.add_edge(2,4)
g3.add_edge(3,4)
g3.add_edge(5,6)
g3.add_edge(5,7)

s = find_all_nodes_in_cycle(g3)
print(f'Your code returns set of nodes: {s}')
assert s == {0,2,3,4}, 'Fail: Set of nodes must be {0,2,3,4}.'

# let's also add the edge 6,7
g3.add_edge(6,7)
s1 = find_all_nodes_in_cycle(g3)
print(f'Your code returns set of nodes: {s1}')
assert s1 == {0,2,3,4,5,6,7}, 'Fail: Set of nodes must be {0,2,3,4,5,6,7}.'

print('All tests passedd: 10 points!')
