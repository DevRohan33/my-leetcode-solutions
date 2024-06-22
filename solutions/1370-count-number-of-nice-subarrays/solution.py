class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {0: 1}  # Dictionary to store the frequency of prefix sums
        current_sum = 0
        result = 0
        
        for num in nums:
            if num % 2 != 0:
                current_sum += 1
            
            if current_sum - k in count:
                result += count[current_sum - k]
            
            if current_sum in count:
                count[current_sum] += 1
            else:
                count[current_sum] = 1
        
        return result

