# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        to_delete_set = set(to_delete)
        forest = []

        def dfs(node, is_root):
            if not node:
                return None
            root_deleted = node.val in to_delete_set
            if is_root and not root_deleted:
                forest.append(node)
            node.left = dfs(node.left, root_deleted)
            node.right = dfs(node.right, root_deleted)
            return None if root_deleted else node

        dfs(root, True)
        return forest

# Helper function to print the tree in level order (for testing purpose)
def print_tree(root):
    if not root:
        return "[]"
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()
    return result

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

solution = Solution()
forest = solution.delNodes(root, [3, 5])

# Print the resulting forest
print([print_tree(tree) for tree in forest])  # Output: [[1, 2, None, 4], [6], [7]]

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.right = TreeNode(3)
root2.left.left = TreeNode(4)

forest2 = solution.delNodes(root2, [3])

print([print_tree(tree) for tree in forest2])  # Output: [[1, 2, 4]]

        
