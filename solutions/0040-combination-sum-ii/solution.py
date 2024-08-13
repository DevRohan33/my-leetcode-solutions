class Solution(object):
    def combinationSum2(self, candidates, target):
        def backtrack(start, current_combination, current_sum):
            if current_sum == target:
                result.append(list(current_combination))
                return
            if current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                current_combination.append(candidates[i])
                backtrack(i + 1, current_combination, current_sum + candidates[i])
                current_combination.pop()
        
        candidates.sort()
        result = []
        backtrack(0, [], 0)
        return result

# Example usage:
solution = Solution()
print(solution.combinationSum2([10,1,2,7,6,1,5], 8))
# Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

print(solution.combinationSum2([2,5,2,1,2], 5))
# Output: [[1, 2, 2], [5]]

