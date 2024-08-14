class Solution(object):
    def count_pairs(self, nums, mid):
        count = 0
        left = 0
        # Use a two-pointer approach to count pairs with distance <= mid
        for right in range(len(nums)):
            while nums[right] - nums[left] > mid:
                left += 1
            count += right - left
        return count
    
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        
        while low < high:
            mid = (low + high) // 2
            if self.count_pairs(nums, mid) >= k:
                high = mid
            else:
                low = mid + 1
                
        return low

        
