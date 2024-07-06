class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        total_passes = 2 * (n - 1)  # Total passes to complete one round trip
        remaining_passes = time % total_passes  # Remaining passes after full round trips
        
        if remaining_passes <= n - 1:
            return remaining_passes + 1  # Still in the forward direction
        else:
            return n - (remaining_passes - (n - 1))  # Returning in the backward direction

# Example usage:
solution = Solution()

# Test cases
print(solution.passThePillow(4, 5))  # Output: 2
print(solution.passThePillow(3, 7))  # Output: 1
print(solution.passThePillow(5, 12))  # Output: 4

