class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []

        left_products = [1] * n
        right_products = [1] * n
        answer = [1] * n

        # Calculate left products
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]

        # Calculate right products
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]

        # Combine left and right products
        for i in range(n):
            answer[i] = left_products[i] * right_products[i]

        return answer
