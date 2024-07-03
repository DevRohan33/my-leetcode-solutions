class Solution(object):
    def minDifference(self, nums):
        if len(nums) <= 4:
            return 0

        nums.sort()
        n = len(nums)

        
        return min(nums[n-1] - nums[3],
                   nums[n-2] - nums[2],
                   nums[n-3] - nums[1],  
                   nums[n-4] - nums[0])
solution = Solution()
        
