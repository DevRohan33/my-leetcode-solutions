class Solution(object):
    def findMaxAverage(self, nums, k):
        # Calculate the sum of the first window of size k
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Slide the window from the start to the end of the array
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        
        # Return the maximum average
        return max_sum / float(k)

# Example usage
solution = Solution()
print(solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # Output: 12.75000
print(solution.findMaxAverage([5], 1))  # Output: 5.00000

