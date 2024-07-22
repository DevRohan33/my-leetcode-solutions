class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # Convert lists to sets to remove duplicates and allow set operations
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find elements in set1 that are not in set2
        only_in_nums1 = list(set1 - set2)
        
        # Find elements in set2 that are not in set1
        only_in_nums2 = list(set2 - set1)
        
        # Return the results as a list of lists
        return [only_in_nums1, only_in_nums2]

# Example usage:
solution = Solution()

# Example 1
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
print(solution.findDifference(nums1, nums2))  # Output: [[1, 3], [4, 6]]

# Example 2
nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]
print(solution.findDifference(nums1, nums2))  # Output: [[3], []]

