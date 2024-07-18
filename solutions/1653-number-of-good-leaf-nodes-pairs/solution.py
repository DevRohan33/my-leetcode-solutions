class Solution(object):
    def countPairs(self, root, distance):
        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [1]
            
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # Check all pairs between left and right distances
            for ld in left_distances:
                for rd in right_distances:
                    if ld + rd <= distance:
                        self.result += 1
            
            # Return distances incremented by 1
            return [d + 1 for d in left_distances + right_distances if d + 1 < distance]
        
        self.result = 0
        dfs(root)
        return self.result

# Helper function to build a tree from a list input
def build_tree(lst, idx=0):
    if idx >= len(lst) or lst[idx] is None:
        return None
    node = TreeNode(lst[idx])
    node.left = build_tree(lst, 2 * idx + 1)
    node.right = build_tree(lst, 2 * idx + 2)
    return node

# Example usage:
root1 = build_tree([1, 2, 3, None, 4])
distance1 = 3

root2 = build_tree([1, 2, 3, 4, 5, 6, 7])
distance2 = 3

root3 = build_tree([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2])
distance3 = 3

solution = Solution()
print(solution.countPairs(root1, distance1))  # Output: 1
print(solution.countPairs(root2, distance2))  # Output: 2
print(solution.countPairs(root3, distance3))  # Output: 1

        
