from collections import deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        if not nums:
            return 0
        
        min_deque = deque()
        max_deque = deque()
        left = 0
        max_len = 0

        for right in range(len(nums)):
            # Maintain the increasing order in min_deque
            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Maintain the decreasing order in max_deque
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Check if the current window is valid
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                if min_deque[0] < left:
                    min_deque.popleft()
                if max_deque[0] < left:
                    max_deque.popleft()

            # Update the maximum length of a valid window
            max_len = max(max_len, right - left + 1)

        return max_len

# Example usage:
sol = Solution()
nums = [1, 5, 6, 7, 8, 10, 6, 5, 6]
limit = 4
print(sol.longestSubarray(nums, limit))  # Expected output: 5

