from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxCount = float('-inf')
        self.calcuateMax(root)
        return self.maxCount
    def calcuateMax(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = max(self.calcuateMax(root.left),0)
        right = max(self.calcuateMax(root.right),0)

        total = left +right + root.val

        self.maxCount = max(self.maxCount, total)
        return total

# Constructing a binary search tree
#        -10
#        / \
#       9   20
#           / \
#          15   7

tree = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
solution = Solution()
actual1= solution.maxPathSum(tree)
print(actual1)