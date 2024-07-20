class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        rows = len(rowSum)
        cols = len(colSum)
        matrix = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                # Determine the value for the current cell
                val = min(rowSum[i], colSum[j])
                matrix[i][j] = val
                
                # Update the rowSum and colSum
                rowSum[i] -= val
                colSum[j] -= val
        
        return matrix

# Example usage:
solution = Solution()

# Example 1
rowSum1 = [3, 8]
colSum1 = [4, 7]
print(solution.restoreMatrix(rowSum1, colSum1))  # Output: [[3,0], [1,7]]

# Example 2
rowSum2 = [5, 7, 10]
colSum2 = [8, 6, 8]
print(solution.restoreMatrix(rowSum2, colSum2))  # Output: [[0,5,0], [6,1,0], [2,0,8]]

