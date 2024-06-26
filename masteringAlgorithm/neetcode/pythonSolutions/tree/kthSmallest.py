from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallestRecursive(self, root: Optional[TreeNode], k: int) -> int:
        def valid(node):
            if not node:
                return []

            left = valid(node.left)
            current = [node.val]
            right = valid(node.right)

            return left + current + right

        sorted_result = valid(root)
        return sorted_result[k -1]

    def kthSmallestIterative(self, root: Optional[TreeNode], k: int) -> int:
        stack= []
        current = root
        count=0

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            count+=1

            if k == count:
                return current.val

            current = current.right


# Constructing a binary search tree
#         5
#        / \
#       3   6
#      / \
#     2   4
#    /
tree = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))

solution = Solution()
print('---- recursive solution soluiton------------')
acutal1= solution.kthSmallestRecursive(tree,1)
print(acutal1," Here is the final result", acutal1 ==1)

acutal2= solution.kthSmallestRecursive(tree,3)
print(acutal2," Here is the final result", acutal2 ==3)

acutal3= solution.kthSmallestRecursive(tree,5)
print(acutal3," Here is the final result", acutal3 ==3)


print('---- iterative soluiton------------')
acutal4= solution.kthSmallestIterative(tree,1)
print(acutal4," Here is the final result", acutal4 ==1)

acutal5= solution.kthSmallestIterative(tree,3)
print(acutal5," Here is the final result", acutal5 ==3)

acutal6= solution.kthSmallestIterative(tree,5)
print(acutal6," Here is the final result", acutal6 ==3)