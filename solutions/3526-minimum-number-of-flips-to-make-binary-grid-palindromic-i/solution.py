class Solution(object):
    def minFlips(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def min_flips_for_line(line):
            flips = 0
            length = len(line)
            for i in range(length // 2):
                if line[i] != line[length - 1 - i]:
                    flips += 1
            return flips
        
        def total_flips_for_rows():
            flips = 0
            for row in grid:
                flips += min_flips_for_line(row)
            return flips
        
        def total_flips_for_columns():
            flips = 0
            m, n = len(grid), len(grid[0])
            for c in range(n):
                column = [grid[r][c] for r in range(m)]
                flips += min_flips_for_line(column)
            return flips

        row_flips = total_flips_for_rows()
        column_flips = total_flips_for_columns()

        # Return the minimum flips required
        return min(row_flips, column_flips)

# Example usage
solution = Solution()
grid1 = [[1,0,0],[0,0,0],[0,0,1]]
print(solution.minFlips(grid1))  # Output: 2

grid2 = [[0,1],[0,1],[0,0]]
print(solution.minFlips(grid2))  # Output: 1

