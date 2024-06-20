class Solution(object):
    def maxDistance(self, position, m):
        position.sort()
        low, high = 0, position[-1] - position[0]
        res = 0
        
        while low <= high:
            mid = (low + high) // 2
            if self.can_place_cameras(position, mid, m):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return res
    
    def can_place_cameras(self, position, distance, m):
        count, last_position = 1, position[0]
        
        for i in range(1, len(position)):
            if position[i] - last_position >= distance:
                count += 1
                last_position = position[i]
                if count == m:
                    return True
        
        return count >= m

