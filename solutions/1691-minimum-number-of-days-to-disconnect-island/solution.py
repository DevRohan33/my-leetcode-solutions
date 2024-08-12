class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def count_islands(grid):
            m, n = len(grid), len(grid[0])
            visited = [[False] * n for _ in range(m)]

            def dfs(x, y):
                if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0 or visited[x][y]:
                    return
                visited[x][y] = True
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)

            islands = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        islands += 1
                        dfs(i, j)

            return islands

        def is_disconnected():
            return count_islands(grid) != 1

        # Check if already disconnected
        if is_disconnected():
            return 0

        # Check if disconnecting by removing one land cell
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if is_disconnected():
                        return 1
                    grid[i][j] = 1

        # If it’s not possible to disconnect by removing one cell, return 2
        return 2

