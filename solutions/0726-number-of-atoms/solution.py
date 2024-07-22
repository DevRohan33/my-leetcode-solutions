class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        import collections
        stack = [collections.Counter()]
        i, n = 0, len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(collections.Counter())
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[i_start:i] or 1)
                for key in top:
                    stack[-1][key] += top[key] * multiplicity
            else:
                i_start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                name = formula[i_start:i]
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[i_start:i] or 1)
                stack[-1][name] += multiplicity
        
        result = ""
        for name in sorted(stack[-1]):
            result += name
            if stack[-1][name] > 1:
                result += str(stack[-1][name])
        
        return result

# Example usage:
solution = Solution()

# Example 1
formula = "H2O"
print(solution.countOfAtoms(formula))  # Output: "H2O"

# Example 2
formula = "Mg(OH)2"
print(solution.countOfAtoms(formula))  # Output: "H2MgO2"

# Example 3
formula = "K4(ON(SO3)2)2"
print(solution.countOfAtoms(formula))  # Output: "K4N2O14S4"

