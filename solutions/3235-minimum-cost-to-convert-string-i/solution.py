class Solution(object):
    def __init__(self):
        # Number of lowercase English letters
        self.CHAR_COUNT = 26
        self.inf = float('inf')
    
    def char_to_index(self, c):
        # Convert character to index (a -> 0, b -> 1, ..., z -> 25)
        return ord(c) - ord('a')
    
    def minimumCost(self, source, target, original, changed, cost):
        n = len(source)
        
        # Initialize the cost matrix with inf
        cost_matrix = [[self.inf] * self.CHAR_COUNT for _ in range(self.CHAR_COUNT)]
        
        # Distance from a character to itself is 0
        for i in range(self.CHAR_COUNT):
            cost_matrix[i][i] = 0
        
        # Fill the cost matrix with the given transformations
        for o, c, z in zip(original, changed, cost):
            cost_matrix[self.char_to_index(o)][self.char_to_index(c)] = min(cost_matrix[self.char_to_index(o)][self.char_to_index(c)], z)
        
        # Apply Floyd-Warshall algorithm to find shortest paths
        for k in range(self.CHAR_COUNT):
            for i in range(self.CHAR_COUNT):
                for j in range(self.CHAR_COUNT):
                    if cost_matrix[i][k] < self.inf and cost_matrix[k][j] < self.inf:
                        cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i][k] + cost_matrix[k][j])
        
        # Calculate the total minimum cost to convert source to target
        total_cost = 0
        for s_char, t_char in zip(source, target):
            s_index = self.char_to_index(s_char)
            t_index = self.char_to_index(t_char)
            if cost_matrix[s_index][t_index] == self.inf:
                return -1
            total_cost += cost_matrix[s_index][t_index]
        
        return total_cost

# Example usage:
solution = Solution()
source = "abcd"
target = "acbe"
original = ["a", "b", "c", "c", "e", "d"]
changed = ["b", "c", "b", "e", "b", "e"]
cost = [2, 5, 5, 1, 2, 20]
print(solution.minimumCost(source, target, original, changed, cost))  # Output: 28

