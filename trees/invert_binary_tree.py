"""
Problem: Invert Binary Tree

Pattern:
DFS / Recursion

Approach:
Swap the left and right child.
Recursively invert both subtrees.

Time: O(n)

Space: O(h)

Key Insight:
Invert the current node first,
then recursively invert the left and right subtree.

DFS Template:

def dfs(node):

    if not node:
        return

    dfs(node.left)
    dfs(node.right)

My Takeaways:
- Recursion works on smaller subtrees.
- Every recursive call must make progress.
- Tree problems often use:
    process current node
    recurse left
    recurse right
"""

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):

    if not root:
        return None

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)

    return root