import math

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def get_tree_lines(root, space=0, level_spacing=6):
    """ Recursively generates tree lines for printing """
    if root is None:
        return [], 0, 0, 0  # No lines, width, root start position, gap

    line1, width1, start1, end1 = get_tree_lines(root.left, space + level_spacing, level_spacing)
    line2, width2, start2, end2 = get_tree_lines(root.right, space + level_spacing, level_spacing)

    node_value = str(root.value)
    node_width = len(node_value)

    # Position of current root
    first_line = (start1 + end1) // 2 if root.left else 0
    second_line = (start2 + end2) // 2 + width1 + level_spacing if root.right else width1 + level_spacing

    first_line = max(first_line, len(line1))
    second_line = max(second_line, len(line2))

    # Compute tree width
    new_width = max(first_line + node_width, second_line)

    # Construct first line (node value centered)
    root_line = " " * first_line + node_value + " " * (new_width - first_line - node_width)

    # Construct second line (branches)
    if root.left or root.right:
        left_branch = "/" if root.left else " "
        right_branch = "\\" if root.right else " "
        branch_line = " " * first_line + left_branch + " " * (new_width - first_line - 1) + right_branch
    else:
        branch_line = ""

    # Merge lines
    gap = " " * level_spacing
    lines = [root_line, branch_line] + [l1 + gap + l2 for l1, l2 in zip(line1 + [""] * (len(line2) - len(line1)),
                                                                        line2 + [""] * (len(line1) - len(line2)))]

    return lines, new_width, first_line, second_line


def print_tree(root):
    """ Prints tree structure in ASCII format """
    lines, *_ = get_tree_lines(root)
    for line in lines:
        print(line)

def buildTree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    return root;