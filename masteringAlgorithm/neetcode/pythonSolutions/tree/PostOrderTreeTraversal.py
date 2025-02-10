# Postorder Tree Traversal
# Postorder Tree Traversal of binary tree means
# Right Sub Tree
# Left SubTree
# Root Node
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class Solution:
    def postOrderTraversal(self, root: TreeNode):
        if root:
            self.postOrderTraversal(root.left)
            self.postOrderTraversal(root.right)
            print(root.val, end= ' ')

    def postOrderTraversalIterative(self, root: TreeNode):
        if not root:
            return

        stack1 = [root]
        stack2 = []

        while stack1:
            current = stack1.pop()
            stack2.append(current)

            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)

        while stack2:
            print(stack2.pop().val, end=' ')

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left= TreeNode(3)
root.left.right = TreeNode(4)

solution = Solution()
print()
print('Recursive Solution')
solution.postOrderTraversal(root)
print()
print('Iterative Solution')
solution.postOrderTraversalIterative(root)
