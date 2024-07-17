class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_length = max(max_length, right - left)

        return max_length

# Example usage
solution = Solution()
print(solution.longestSubarray([1, 1, 0, 1]))  # Output: 3
print(solution.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))  # Output: 5
print(solution.longestSubarray([1, 1, 1]))  # Output: 2

