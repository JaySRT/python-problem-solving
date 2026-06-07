"""
Problem: Same Tree

Pattern:
DFS / Recursion

Approach:
Compare both trees node by node.

Base Cases:
- Both None -> True
- One None -> False
- Different values -> False

Recursively compare:
- Left subtree
- Right subtree

Time: O(n)

Space: O(h)

Key Insight:
Two trees are identical only if:
- Current nodes match
- Left subtrees match
- Right subtrees match

DFS Template:

def dfs(node):

    if base_case:
        return ...

    left = dfs(...)
    right = dfs(...)

    return combine(left, right)

My Takeaways:
- Recursion can return booleans, not just numbers.
- Tree comparison is naturally recursive.
- 'and' is often used when all conditions must be true.
"""

class TreeNode:

    def __init__(
        self,
        val=0,
        left=None,
        right=None
    ):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    if not p and not q:
        return True
    
    if not p or not q:
        return False
    
    if p.val != q.val:
        return False
    
    left_same = is_same_tree(p.left, q.left)
    right_same = is_same_tree(p.right, q.right)

    return left_same and right_same