class Solution(object):
    def closeStrings(self, word1, word2):
        # If the lengths of the two words are different, they can't be close.
        if len(word1) != len(word2):
            return False
        
        # Count the frequency of each character in both words.
        freq1 = {}
        freq2 = {}
        for char in word1:
            freq1[char] = freq1.get(char, 0) + 1
        for char in word2:
            freq2[char] = freq2.get(char, 0) + 1
        
        # Check if both words have the same unique set of characters.
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        
        # Check if both words have the same frequency distribution.
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False
        
        # If both conditions are satisfied, the words are close.
        return True

