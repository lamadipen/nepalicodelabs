# Inorder Tree Traversal
# Inorder Traversal of binary tree means visit tree in following order
# Left SubTree
# Root Node
# Right subTree
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class Solution:
    # Run time O(n) where n is number of nodes
    # Space Complexity O(H) where h is height of tree
    def inorderTraversalRecursive(self, root : TreeNode):
        if root:
            self.inorderTraversalRecursive(root.left)
            print(root.val, end=' ')
            self.inorderTraversalRecursive(root.right)

    # Run time O(n) where n is number of nodes
    # Space Complexity O(H) where h is height of tree
    def inorderTraversalIterative(self, root: TreeNode):
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            print(current.val, end=' ')

            current = current.right




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left= TreeNode(4)
root.left.right = TreeNode(5)

solution = Solution()
solution.inorderTraversalRecursive(root)