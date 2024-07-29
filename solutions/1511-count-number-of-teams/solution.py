class Solution:
    def numTeams(self, rating):
        n = len(rating)
        increasing_teams = 0
        decreasing_teams = 0

        for j in range(n):
            # Counts for increasing teams
            less_left = sum(rating[i] < rating[j] for i in range(j))
            greater_right = sum(rating[k] > rating[j] for k in range(j + 1, n))
            increasing_teams += less_left * greater_right

            # Counts for decreasing teams
            greater_left = sum(rating[i] > rating[j] for i in range(j))
            less_right = sum(rating[k] < rating[j] for k in range(j + 1, n))
            decreasing_teams += greater_left * less_right
        
        return increasing_teams + decreasing_teams

# Example usage
solution = Solution()
print(solution.numTeams([2, 5, 3, 4, 1]))  # Output: 3
print(solution.numTeams([2, 1, 3]))        # Output: 0
print(solution.numTeams([1, 2, 3, 4]))    # Output: 4

