class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prefix_sum = 0
        seen = {0: -1}  # Store prefix sums and their indices

        for i, num in enumerate(nums):
            prefix_sum += num
            if k != 0:
                prefix_sum %= k
            
            if prefix_sum in seen:
                if i - seen[prefix_sum] >= 2:
                    return True
            else:
                seen[prefix_sum] = i

        return False
