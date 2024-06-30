class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Sort edges by type (type 3 first, then type 1, then type 2)
        edges.sort(key=lambda x: x[0], reverse=True)
        
        # Use disjoint sets to track connected components for Alice and Bob
        alice_set = DisjointSet(n)
        bob_set = DisjointSet(n)
        
        # Track the number of edges removed
        removed_edges = 0
        
        # Iterate through edges in order of type
        for edge_type, u, v in edges:
            if edge_type == 3:
                # Try to add the edge to both Alice's and Bob's disjoint sets
                alice_connected = alice_set.union(u-1, v-1)
                bob_connected = bob_set.union(u-1, v-1)
                if not alice_connected and not bob_connected:
                    # If the union operation returns False for both, it means the edge is redundant
                    removed_edges += 1
            elif edge_type == 1:
                # If Alice can traverse the edge, add it to her disjoint set
                if not alice_set.union(u-1, v-1):
                    removed_edges += 1
            elif edge_type == 2:
                # If Bob can traverse the edge, add it to his disjoint set
                if not bob_set.union(u-1, v-1):
                    removed_edges += 1
        
        # Check if both Alice and Bob can traverse the entire graph
        if alice_set.count_sets() == 1 and bob_set.count_sets() == 1:
            return removed_edges
        else:
            # If either Alice or Bob cannot traverse the entire graph, return -1
            return -1

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u == root_v:
            return False
        
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
        self.count -= 1
        return True
    
    def count_sets(self):
        return self.count

