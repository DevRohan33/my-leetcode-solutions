class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        flips = 0
        res = 0
        is_flipped = [0] * n
        
        for i in range(n):
            if i >= k:
                flips ^= is_flipped[i - k]
            
            if (nums[i] ^ flips) == 0:
                if i + k > n:
                    return -1
                flips ^= 1
                is_flipped[i] = 1
                res += 1
        
        return res

# Example usage:
solution = Solution()
print(solution.minKBitFlips([0,1,0], 1))  # Output: 2
print(solution.minKBitFlips([1,1,0], 2))  # Output: -1
print(solution.minKBitFlips([0,0,0,1,0,1,1,0], 3))  # Output: 3
class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        flips = 0
        res = 0
        is_flipped = [0] * n
        
        for i in range(n):
            if i >= k:
                flips ^= is_flipped[i - k]
            
            if (nums[i] ^ flips) == 0:
                if i + k > n:
                    return -1
                flips ^= 1
                is_flipped[i] = 1
                res += 1
        
        return res


