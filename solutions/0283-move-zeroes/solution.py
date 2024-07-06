class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        Do not return anything, modify nums in-place instead.
        """
        zero = 0  # Pointer for the next position to place a non-zero element
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1

# Example usage:
solution = Solution()
nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

