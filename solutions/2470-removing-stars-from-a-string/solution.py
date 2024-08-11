class Solution(object):
    def removeStars(self, s):
        result = []
        
        # Iterate through each character in the string
        for char in s:
            if char == '*':
                # Pop the last character from result if a star is encountered
                if result:
                    result.pop()
            else:
                # Append the character to result if it's not a star
                result.append(char)
        
        # Join the list into a string and return
        return ''.join(result)

