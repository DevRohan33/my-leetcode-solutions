class Solution(object):
    def maximumGain(self, s, x, y):
        def remove_substring(s, first, second, points):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return "".join(stack), score

        if x > y:
            # Prioritize removing "ab" first
            s, score_ab = remove_substring(s, 'a', 'b', x)
            s, score_ba = remove_substring(s, 'b', 'a', y)
        else:
            # Prioritize removing "ba" first
            s, score_ba = remove_substring(s, 'b', 'a', y)
            s, score_ab = remove_substring(s, 'a', 'b', x)

        return score_ab + score_ba

# Test cases
sol = Solution()
print(sol.maximumGain("cdbcbbaaabab", 4, 5))  # Output: 19
print(sol.maximumGain("aabbaaxybbaabb", 5, 4))  # Output: 20

