class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_ones = sum(nums)
        
        if total_ones == 0:
            return 0
        
        # Create an extended array to handle the circular nature
        extended_nums = nums + nums
        
        # Initialize the current number of 1's in the first window
        current_ones = sum(extended_nums[:total_ones])
        max_ones_in_window = current_ones
        
        # Use a sliding window to find the max number of 1's in any window of size total_ones
        for i in range(1, n):
            current_ones = current_ones - extended_nums[i - 1] + extended_nums[i + total_ones - 1]
            max_ones_in_window = max(max_ones_in_window, current_ones)
        
        # The minimum swaps needed is the total number of 1's minus the max number of 1's in any window
        return total_ones - max_ones_in_window

# Example usage
solution = Solution()
print(solution.minSwaps([0, 1, 0, 1, 1, 0, 0]))  # Output: 1
print(solution.minSwaps([0, 1, 1, 1, 0, 0, 1, 1, 0]))  # Output: 2
print(solution.minSwaps([1, 1, 0, 0, 1]))  # Output: 0

