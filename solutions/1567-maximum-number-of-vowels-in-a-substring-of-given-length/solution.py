class Solution(object):
    def maxVowels(self, s, k):
        vowels = set('aeiou')
        max_vowels = 0
        current_vowels = 0
        
        # Initial count of vowels in the first window of size k
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        max_vowels = current_vowels
        
        # Slide the window over the string
        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowels += 1
            if s[i - k] in vowels:
                current_vowels -= 1
            max_vowels = max(max_vowels, current_vowels)
        
        return max_vowels

# Examples
solution = Solution()
print(solution.maxVowels("abciiidef", 3))  # Output: 3
print(solution.maxVowels("aeiou", 2))      # Output: 2
print(solution.maxVowels("leetcode", 3))   # Output: 2

