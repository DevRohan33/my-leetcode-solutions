class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        
        # Step 1: Count the number of connections (degree) for each city
        degree = [0] * n
        for u, v in roads:
            degree[u] += 1
            degree[v] += 1
        
        # Step 2: Sort cities based on their degree in descending order
        sorted_cities = sorted(range(n), key=lambda x: degree[x], reverse=True)
        
        # Step 3: Assign the highest values to the cities with the highest degrees
        importance = [0] * n
        for i, city in enumerate(sorted_cities):
            importance[city] = n - i
        
        # Step 4: Calculate the total importance of all roads
        total_importance = 0
        for u, v in roads:
            total_importance += importance[u] + importance[v]
        
        return total_importance

# Example usage:
sol = Solution()
n = 5
roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
print(sol.maximumImportance(n, roads))  # Output: 43

        
