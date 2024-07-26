class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        # Initialize the distance matrix with infinity
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Distance from a city to itself is zero
        for i in range(n):
            dist[i][i] = 0
        
        # Fill in the initial distances from the edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Floyd-Warshall algorithm to find all pairs shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Find the city with the smallest number of reachable cities
        min_reachable = float('inf')
        result_city = -1
        
        for i in range(n):
            count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            if count < min_reachable or (count == min_reachable and i > result_city):
                min_reachable = count
                result_city = i
        
        return result_city

# Example usage:
solution = Solution()

# Example 1
n1 = 4
edges1 = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold1 = 4
print(solution.findTheCity(n1, edges1, distanceThreshold1))  # Output: 3

# Example 2
n2 = 5
edges2 = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
distanceThreshold2 = 2
print(solution.findTheCity(n2, edges2, distanceThreshold2))  # Output: 0

