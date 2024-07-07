class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Initialize two pointers for both strings
        s_pointer = 0
        t_pointer = 0

        # Iterate through the string t
        while t_pointer < len(t) and s_pointer < len(s):
            # If characters match, move the s_pointer
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            # Always move the t_pointer
            t_pointer += 1

        # If s_pointer has reached the end of s, it means all characters of s were found in t
        return s_pointer == len(s)

