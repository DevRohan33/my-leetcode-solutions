from collections import defaultdict, deque

class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        def topologicalSort(conditions):
            adj_list = defaultdict(list)
            in_degree = [0] * (k + 1)
            
            for u, v in conditions:
                adj_list[u].append(v)
                in_degree[v] += 1
            
            queue = deque([i for i in range(1, k + 1) if in_degree[i] == 0])
            topo_order = []
            
            while queue:
                node = queue.popleft()
                topo_order.append(node)
                
                for neighbor in adj_list[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
            return topo_order if len(topo_order) == k else []
        
        rowOrder = topologicalSort(rowConditions)
        colOrder = topologicalSort(colConditions)
        
        if not rowOrder or not colOrder:
            return []
        
        rowIndex = {num: i for i, num in enumerate(rowOrder)}
        colIndex = {num: i for i, num in enumerate(colOrder)}
        
        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            matrix[rowIndex[num]][colIndex[num]] = num
        
        return matrix

# Example usage:
solution = Solution()

# Example 1
k = 3
rowConditions1 = [[1, 2], [3, 2]]
colConditions1 = [[2, 1], [3, 2]]
print(solution.buildMatrix(k, rowConditions1, colConditions1))  
# Output: [[3, 0, 0], [0, 0, 1], [0, 2, 0]]

# Example 2
k = 3
rowConditions2 = [[1, 2], [2, 3], [3, 1], [2, 3]]
colConditions2 = [[2, 1]]
print(solution.buildMatrix(k, rowConditions2, colConditions2))  
# Output: []

