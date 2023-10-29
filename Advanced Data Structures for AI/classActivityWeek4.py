class UndirectedGraph:
    #n is the number of vertices
    #we will label the vertices from 0 to self.n-1
    #Initialize to an empty adjacency list
    #we will store the outgoing edges using a set data structure
    def __init__(self, n):
        self.n = n
        self.adj_list = [set() for i in range(self.n)]

    def add_edge(self, i, j):
        assert 0<=i<self.n
        assert 0<=j<self.n
        assert i!=j
        #make sure to add edge from i to j
        #your code here
        self.adj_list[i].add(j)
        #also add edge from j to i
        #your code here
        self.adj_list[j].add(i)

    #get a set of all vertices that are neighbours of the vertex i
    def get_neighbouring_vertices(self, i):
        #your code here
        return print(self.adj_list[i])

#Test your code
#create the graph for G
g = UndirectedGraph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,4)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.get_neighbouring_vertices(0)