class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sum = 0
        remainder_counts = [0] * k
        remainder_counts[0] = 1
        
        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            count += remainder_counts[prefix_sum]
            remainder_counts[prefix_sum] += 1
        
        return count
