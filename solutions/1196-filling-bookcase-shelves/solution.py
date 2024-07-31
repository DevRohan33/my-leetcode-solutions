class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            current_width = 0
            current_height = 0
            for j in range(i - 1, -1, -1):
                current_width += books[j][0]
                current_height = max(current_height, books[j][1])
                if current_width > shelf_width:
                    break
                dp[i] = min(dp[i], dp[j] + current_height)
        return dp[n]
