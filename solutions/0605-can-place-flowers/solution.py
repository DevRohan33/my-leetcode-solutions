class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                # Check if the previous and next plots are empty or if it is the edge of the flowerbed
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                next_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    count += 1
                
                if count >= n:
                    return True
        
        return count >= n

# Example usage:
# sol = Solution()
# print(sol.canPlaceFlowers([1,0,0,0,1], 1))  # Output: True
# print(sol.canPlaceFlowers([1,0,0,0,1], 2))  # Output: False

