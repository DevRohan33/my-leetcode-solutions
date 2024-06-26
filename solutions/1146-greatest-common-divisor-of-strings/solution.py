class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Check if concatenation of both in both orders are the same
        if str1 + str2 != str2 + str1:
            return ""
        
        # Calculate the gcd of lengths of both strings
        gcd_length = self.gcd(len(str1), len(str2))
        
        # Return the prefix of str1 up to gcd_length
        return str1[:gcd_length]

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

# Example usage
sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
print(sol.gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
print(sol.gcdOfStrings("LEET", "CODE"))    # Output: ""

    
