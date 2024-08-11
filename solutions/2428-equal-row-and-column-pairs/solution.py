class Solution(object):
    def equalPairs(self, grid):
        n = len(grid)
        count = 0
        
        # Create a list of tuples for rows and columns
        rows = [tuple(row) for row in grid]
        columns = [tuple(grid[i][j] for i in range(n)) for j in range(n)]
        
        # Count how many rows match with columns
        for row in rows:
            count += columns.count(row)
        
        return count

