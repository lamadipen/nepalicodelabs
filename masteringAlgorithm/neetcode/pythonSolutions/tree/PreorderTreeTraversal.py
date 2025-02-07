#Preorder Tree Traversal
# Preorder Tree Traversal of binary tree means
# Root Node
# Left SubTree
# Right Sub Tree
class TreeNode:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


class Solution:
    def preOrderTraversal(self, root: TreeNode):
        if root:
            print(root.val, end=' ')
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)

    def preOrderTraversalIterative(self, root: TreeNode):
        stack = [root]

        while stack:
            current = stack.pop()
            print(current.val, end=' ')
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left= TreeNode(3)
root.left.right = TreeNode(4)

solution = Solution()
solution.preOrderTraversal(root)
print('Iterative Solution')
solution.preOrderTraversalIterative(root)






