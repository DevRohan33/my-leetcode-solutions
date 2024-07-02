class Solution(object):
    def reverseWords(self, s):
        # Split the string by spaces to get the words
        words = s.split()
        
        # Reverse the list of words
        words.reverse()
        return ' '.join(words)
