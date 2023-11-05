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


g = UndirectedGraph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,4)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,4)


# Test DFS visit
discovery_times = [None]*5
finish_times = [None]*5
dfs_tree_parents = [None]*5
dfs_back_edges = []
g.dfs_visit(0, DFSTimeCounter(), discovery_times, finish_times, dfs_tree_parents, dfs_back_edges )

print('DFS visit discovery and finish times given by your code.')
print('Node\t Discovery\t Finish')
for i in range(5):
    print(f'{i} \t {discovery_times[i]}\t\t {finish_times[i]}')

assert(discovery_times[0] == 0), f'Fail: Node 0 expected discovery time must be 0'
assert(discovery_times[1] == 1), f'Fail: Node 1 expected discovery is 1'
assert(finish_times[1] == 2), f'Fail: Node 1 finish time expected value is 2 (are you incrementing counter before you return from dfs_visit function and before recording finish times)'
assert(discovery_times[2] == 3), f'Fail: Node 2 expected discovery is 3'
assert(finish_times[2] == 8), f'Fail: Node 2 finish time expected value is 8'
assert(discovery_times[3] == 4),f'Fail: Node 3 discovery time expected value is 4'
assert(finish_times[3] == 7), f'Fail: Node 3 finish time expected value is 7'
assert(discovery_times[4] == 5),f'Fail: Node 4 discovery time expected value is 5'
assert(finish_times[4] == 6), f'Fail: Node 4 finish time expected value is 6'

print('Success -- discovery and finish times seem correct.')
print()
    
print('Node\t DFS-Tree-Parent')
for i in range(5):
    print(f'{i} \t {dfs_tree_parents[i]}')

assert(dfs_tree_parents[0] == None), 'Fail: node 0 cannot have a parent (must be root)'
assert(dfs_tree_parents[1] == 0), 'Fail: node 1 parent must be 0'
assert(dfs_tree_parents[2] == 0), 'Fail: node 2 parent must be 0'
assert(dfs_tree_parents[3] == 2), 'Fail: node 3 parent must be 2'
assert(dfs_tree_parents[4] == 3), 'Fail: node 4 parent must be 3'

print('Success-- DFS parents are set correctly.')


print()
# Filter out all trivial back eddges (i,j)  where j is simply the parent of i.
# such back edges occur because we are treating an undirected edge as two directed edges
# in either direction.
non_trivial_back_edges = [(i,j) for (i,j) in dfs_back_edges if dfs_tree_parents[i] != j]
print('Back edges are')
for (i,j) in non_trivial_back_edges:
    print(f'{(i,j)}')
    
    
assert len(non_trivial_back_edges) == 2, f'Fail: There must be 2 non trivial back edges -- your code reports {len(non_trivial_back_edges)}. Note that (4,0) and (4,2) are the only non trivial backedges'
assert (4,2) in non_trivial_back_edges, '(4,2) must be a backedge that is non trivial'
assert (4,0) in non_trivial_back_edges, '(4,3) must be a non-trivial backedges'

print('Success -- 15 points!')