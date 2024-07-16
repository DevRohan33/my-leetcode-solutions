class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_altitude = 0
        current_altitude = 0
        
        for g in gain:
            current_altitude += g
            if current_altitude > max_altitude:
                max_altitude = current_altitude
                
        return max_altitude

# Example usage
solution = Solution()
print(solution.largestAltitude([-5,1,5,0,-7]))  # Output: 1
print(solution.largestAltitude([-4,-3,-2,-1,4,3,2]))  # Output: 0

