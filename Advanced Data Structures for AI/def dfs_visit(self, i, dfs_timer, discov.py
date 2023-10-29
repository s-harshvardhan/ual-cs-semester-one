def dfs_visit(self, i, dfs_timer, discovery_times, finish_times, 
              dfs_tree_parent, dfs_back_edges):
    assert 0 <= i < self.n
    assert discovery_times[i] is None
    assert finish_times[i] is None
    discovery_times[i] = dfs_timer.get()
    dfs_timer.increment()
    
    for j in self.get_neighboring_vertices(i):
        if discovery_times[j] is None:
            # Vertex j has not been visited, so it's a tree edge.
            dfs_tree_parent[j] = i
            self.dfs_visit(j, dfs_timer, discovery_times, finish_times, dfs_tree_parent, dfs_back_edges)
        elif finish_times[j] is None:
            # Vertex j has been visited but not finished, so it's a back edge.
            dfs_back_edges.append((i, j))
    
    finish_times[i] = dfs_timer.get()
    dfs_timer.increment()
