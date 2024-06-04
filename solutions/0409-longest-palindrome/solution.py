class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_counts = {}
        for char in s:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        
        palindrome_length = 0
        has_odd_count = False
        for count in char_counts.values():
            if count % 2 == 0:
                palindrome_length += count
            else:
                palindrome_length += count - 1
                has_odd_count = True
        
        if has_odd_count:
            palindrome_length += 1
        
        return palindrome_length
