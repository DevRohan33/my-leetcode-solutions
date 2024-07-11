class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        
        for char in s:
            if char == ')':
                # Pop characters until the corresponding '('
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Pop the '(' itself
                if stack: stack.pop()
                # Reverse the characters and put them back in the stack
                stack.extend(temp)
            else:
                # Push current character to stack
                stack.append(char)
        
        # Join the characters in the stack to form the final result
        return ''.join(stack)

# Examples
solution = Solution()
print(solution.reverseParentheses("(abcd)"))           # Output: "dcba"
print(solution.reverseParentheses("(u(love)i)"))       # Output: "iloveu"
print(solution.reverseParentheses("(ed(et(oc))el)"))   # Output: "leetcode"

