class DisjointForests:
    def __init__(self, n):
        assert n >= 1, ' Empty disjoint forest is disallowed'
        self.n = n
        self.parents = [None]*n
        self.rank = [None]*n
        
    # Function: dictionary_of_sets
    # Convert the disjoint forest structure into a dictionary d
    # wherein d has an entry for each representative i
    # d[i] maps to each elements which belongs to the tree corresponding to i
    # in the disjoint forest.
    def dictionary_of_sets(self):
        d = {}
        for i in range(self.n):
            if self.is_representative(i):
                d[i] = set([i])
        for j in range(self.n):
            if self.parents[j] != None:
                root = self.find(j)
                assert root in d
                d[root].add(j)
        return d
    
    def make_set(self, j):
        assert 0 <= j < self.n
        assert self.parents[j] == None, 'You are calling make_set on an element multiple times -- not allowed.'
        self.parents[j] = j
        self.rank[j] = 1 
        
    def is_representative(self, j):
        return self.parents[j] == j 
    
    def get_rank(self, j):
        return self.rank[j]
    
    # Function: find
    # Implement the find algorithm for a node j in the set.
    # Repeatedly traverse the parent pointer until we reach a root.
    def find(self, j):
        assert 0 <= j < self.n
        assert self.parents[j] != None, 'You are calling find on an element that is not part of the family yet. Please call make_set first.'
        # your code here
        if self.parents[j] == j:
            return j
        else:
            # Path compression: Set the parent to the root for faster future lookups.
            self.parents[j] = self.find(self.parents[j])
            return self.parents[j]
    
    # Function : union
    # Compute union of j1 and j2
    # First do a find to get to the representatives of j1 and j2.
    # If they are not the same, then 
    #  implement union using the rank strategy I.e, lower rank root becomes
    #  child of the higher ranked root.
    #  break ties by making the first argument j1's root the parent.
    def union(self, j1, j2):
        assert 0 <= j1 < self.n
        assert 0 <= j2 < self.n
        assert self.parents[j1] != None
        assert self.parents[j2] != None
        # your code here
        root1 = self.find(j1)
        root2 = self.find(j2)

        if root1 != root2:
            # Union by rank: Attach the shorter tree to the root of the taller tree.
            if self.rank[root1] > self.rank[root2]:
                self.parents[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parents[root1] = root2
            else:
                # If ranks are equal, choose one to be the new root and increase its rank.
                self.parents[root2] = root1
                self.rank[root1] += 1

d = DisjointForests(10)
for i in range(10):
    d.make_set(i)

for i in range(10):
    assert d.find(i) == i, f'Failed: Find on {i} must return {i} back'

d.union(0,1)
d.union(2,3)
assert(d.find(0) == d.find(1)), '0 and 1 have been union-ed together'
assert(d.find(2) == d.find(3)), '2 and 3 have been union-ed together'
assert(d.find(0) != d.find(3)), '0 and 3 should be in  different trees'
assert((d.get_rank(0) == 2 and d.get_rank(1) == 1) or 
       (d.get_rank(1) == 2 and d.get_rank(0) == 1)), 'one of the nodes 0 or 1 must have rank 2'

assert((d.get_rank(2) == 2 and d.get_rank(3) == 1) or 
       (d.get_rank(3) == 2 and d.get_rank(2) == 1)), 'one of the nodes 2 or 3 must have rank 2'


d.union(3,4)
assert(d.find(2) == d.find(4)), '2 and 4 must be in the same set in the family.'

d.union(5,7)
d.union(6,8)
d.union(3,7)
d.union(0,6)

assert(d.find(6) == d.find(1)), '1 and 6 must be in the same set in the family'
assert(d.find(7) == d.find(4)), '7 and 4 must be in the same set in the family'
print('All tests passed: 10 points.')

class UndirectedGraph:
    
    # n is the number of vertices
    # we will label the vertices from 0 to self.n -1 
    # We simply store the edges in a list.
    def __init__(self, n):
        assert n >= 1, 'You are creating an empty graph -- disallowed'
        self.n = n
        self.edges = []
        self.vertex_data = [None]*self.n
       
        
    def set_vertex_data(self, j, dat):
        assert 0 <= j < self.n
        self.vertex_data[j] = dat
        
    def get_vertex_data(self, j):
        assert 0 <= j < self.n
        return self.vertex_data[j] 
        
    def add_edge(self, i, j, wij):
        assert 0 <= i < self.n
        assert 0 <= j < self.n
        assert i != j
        # Make sure to add edge from i to j with weight wij
        self.edges.append((i, j, wij))
        
    def sort_edges(self):
        # sort edges in ascending order of weights.
        self.edges = sorted(self.edges, key=lambda edg_data: edg_data[2])

def compute_scc(g, W):
    # create a disjoint forest with as many elements as number of vertices
    # Next compute the strongly connected components using the disjoint forest data structure
    d = DisjointForests(g.n)
    # your code here
    for i in range(g.n):
        d.make_set(i)
    
    g.sort_edges()

    for edge in g.edges:
        i, j, wij = edge
        if wij <= W:
            d.union(i, j)
           
    # extract a set of sets from d
    return d.dictionary_of_sets()  

g3 = UndirectedGraph(8)
g3.add_edge(0,1,0.5)
g3.add_edge(0,2,1.0)
g3.add_edge(0,4,0.5)
g3.add_edge(2,3,1.5)
g3.add_edge(2,4,2.0)
g3.add_edge(3,4,1.5)
g3.add_edge(5,6,2.0)
g3.add_edge(5,7,2.0)
res = compute_scc(g3, 2.0)
print('SCCs with threshold 2.0 computed by your code are:')
assert len(res) == 2, f'Expected 2 SCCs but got {len(res)}'
for (k, s) in res.items():
    print(s)
    
# Let us check that your code returns what we expect.
for (k, s) in res.items():
    if (k in [0,1,2,3,4]):
        assert (s == set([0,1,2,3,4])), '{0,1,2,3,4} should be an SCC'
    if (k in [5,6,7]):
        assert (s == set([5,6,7])), '{5,6,7} should be an SCC'

        
# Let us check that the thresholding works
print('SCCs with threshold 1.5')
res2 = compute_scc(g3, 1.5) # This cutsoff edges 2,4 and 5, 6, 7
for (k, s) in res2.items():
    print(s)
assert len(res2) == 4, f'Expected 4 SCCs but got {len(res2)}'

for (k, s) in res2.items():
    if k in [0,1,2,3,4]:
        assert (s == set([0,1,2,3,4])), '{0,1,2,3,4} should be an SCC'
    if k in [5]:
        assert s == set([5]), '{5} should be an SCC with just a single node.'
    if k in [6]:
        assert s == set([6]), '{6} should be an SCC with just a single node.'
    if k in [7]:
        assert s == set([7]), '{7} should be an SCC with just a single node.'
        
print('All tests passed: 10 points')

def compute_mst(g):
    # return a tuple of two items
    #   1. list of edges (i,j) that are part of the MST
    #   2. sum of MST edge weights.
    d = DisjointForests(g.n)
    mst_edges = []
    g.sort_edges()
    # your code here
    total_weight = 0

    for i in range(g.n):
        d.make_set(i)

    for edge in g.edges:
        i, j, wij = edge
        # check for cycle in MST
        if d.find(i) != d.find(j):
            # add this edge in the MST.
            mst_edges.append((i, j, wij))
            total_weight += wij
            # union the two components to grow the MST.
            d.union(i, j)

    return mst_edges, total_weight

g3 = UndirectedGraph(8)
g3.add_edge(0,1,0.5)
g3.add_edge(0,2,1.0)
g3.add_edge(0,4,0.5)
g3.add_edge(2,3,1.5)
g3.add_edge(2,4,2.0)
g3.add_edge(3,4,1.5)
g3.add_edge(5,6,2.0)
g3.add_edge(5,7,2.0)
g3.add_edge(3,5,2.0)

(mst_edges, mst_weight) = compute_mst(g3)
print('Your code computed MST: ')
for (i,j,wij) in mst_edges:
    print(f'\t {(i,j)} weight {wij}')
print(f'Total edge weight: {mst_weight}')

assert mst_weight == 9.5, 'Optimal MST weight is expected to be 9.5'

assert (0,1,0.5) in mst_edges
assert (0,2,1.0) in mst_edges
assert (0,4,0.5) in mst_edges
assert (5,6,2.0) in mst_edges
assert (5,7,2.0) in mst_edges
assert (3,5,2.0) in mst_edges
assert (2,3, 1.5) in mst_edges or (3,4, 1.5) in mst_edges

print('All tests passed: 10 points!')
