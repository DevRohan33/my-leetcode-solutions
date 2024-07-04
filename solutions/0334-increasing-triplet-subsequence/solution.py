class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf')
        second = float('inf')
        
        for n in nums:
            if n <= first:
                first = n  # smallest element so far
            elif n <= second:
                second = n  # second smallest element so far
            else:
                # If we find a number greater than both first and second, we have our triplet
                return True
        
        return False

