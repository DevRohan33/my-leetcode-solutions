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
    def getDirections(self, root, startValue, destValue):
        """
        :type root: TreeNode
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        def findPath(node, value, path):
            if not node:
                return False
            if node.val == value:
                return True
            
            # Try left subtree
            path.append('L')
            if findPath(node.left, value, path):
                return True
            path.pop()
            
            # Try right subtree
            path.append('R')
            if findPath(node.right, value, path):
                return True
            path.pop()
            
            return False
        
        # Find paths from root to startValue and destValue
        startPath = []
        destPath = []
        findPath(root, startValue, startPath)
        findPath(root, destValue, destPath)
        
        # Find the common path length
        i = 0
        while i < len(startPath) and i < len(destPath) and startPath[i] == destPath[i]:
            i += 1
        
        # Steps to go up to the common ancestor
        stepsUp = 'U' * (len(startPath) - i)
        # Steps from the common ancestor to the destination
        stepsDown = ''.join(destPath[i:])
        
        # Combine the steps
        return stepsUp + stepsDown

# Example usage
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(4)

solution = Solution()
print(solution.getDirections(root, 3, 6))  # Output: "UURL"

root2 = TreeNode(2)
root2.left = TreeNode(1)

print(solution.getDirections(root2, 2, 1))  # Output: "L"

