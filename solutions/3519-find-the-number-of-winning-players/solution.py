class Solution(object):
    def winningPlayerCount(self, n, pick):
        """
        :type n: int
        :type pick: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        color_counts = defaultdict(lambda: defaultdict(int))
        
    
        for player, color in pick:
            color_counts[player][color] += 1

    
        winners = 0
        for player in range(n):
            # Check if any color count for the player is greater than player index + 1
            if any(count > player for count in color_counts[player].values()):
                winners += 1

        return winners

# Example usage:
solution = Solution()
n = 4
pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]
print(solution.winningPlayerCount(n, pick))  # Output: 2
        
