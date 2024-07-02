from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        # Count the elements in nums1
        count1 = Counter(nums1)
        
        # Initialize the result list
        result = []
        
        # Iterate through nums2 and check in the count1 dictionary
        for num in nums2:
            if count1[num] > 0:
                result.append(num)
                count1[num] -= 1
        
        return result
