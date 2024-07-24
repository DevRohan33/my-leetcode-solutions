class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter

        # Step 1: Count the frequency of each number
        frequencyMap = Counter(nums)
        
        # Step 2: Create a custom comparator for sorting
        def customComparator(a, b):
            freqA = frequencyMap[a]
            freqB = frequencyMap[b]
            if freqA == freqB:
                return b - a  # If frequencies are the same, sort in decreasing order
            return freqA - freqB  # Otherwise, sort by frequency in increasing order
        
        # Sort the nums array using the custom comparator
        nums.sort(key=lambda x: (frequencyMap[x], -x))
        
        return nums

# Example usage
solution = Solution()

nums1 = [1, 1, 2, 2, 2, 3]
print(solution.frequencySort(nums1))  # Output: [3, 1, 1, 2, 2, 2]

nums2 = [2, 3, 1, 3, 2]
print(solution.frequencySort(nums2))  # Output: [1, 3, 3, 2, 2]

nums3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
print(solution.frequencySort(nums3))  # Output: [5, -1, 4, 4, -6, -6, 1, 1, 1]

