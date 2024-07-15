# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: TreeNode
        """
        from collections import defaultdict

        nodes = {}
        has_parent = set()

        # Create all nodes and establish relationships
        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)

            if is_left == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

            has_parent.add(child)

        # The root is the node that has no parent
        root = None
        for node in nodes:
            if node not in has_parent:
                root = nodes[node]
                break

        return root

# Example usage
# Example 1
descriptions1 = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
solution = Solution()
root1 = solution.createBinaryTree(descriptions1)

# Example 2
descriptions2 = [[1, 2, 1], [2, 3, 0], [3, 4, 1]]
root2 = solution.createBinaryTree(descriptions2)

