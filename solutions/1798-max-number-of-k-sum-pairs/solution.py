class Solution:
    def maxOperations(self, nums, k):
        from collections import Counter
        
        counts = Counter(nums)
        operations = 0
        
        for num in nums:
            complement = k - num
            if counts[num] > 0 and counts[complement] > 0:
                if num == complement and counts[num] > 1:
                    operations += 1
                    counts[num] -= 2
                elif num != complement:
                    operations += 1
                    counts[num] -= 1
                    counts[complement] -= 1
                
        return operations

# Example 1
nums1 = [1, 2, 3, 4]
k1 = 5
solution = Solution()
print(solution.maxOperations(nums1, k1))  # Output: 2

# Example 2
nums2 = [3, 1, 3, 4, 3]
k2 = 6
print(solution.maxOperations(nums2, k2))  # Output: 1

