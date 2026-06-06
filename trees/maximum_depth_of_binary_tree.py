"""
Problem: Maximum Depth of Binary Tree

Pattern:
DFS / Recursion

Approach:
Recursively calculate the depth of the left and right subtree.
Return:
1 + max(left_depth, right_depth)

Time: O(n)
Space: O(h)

Key Insight:
Each node is visited exactly once.
The depth of a node depends on the depth of its children.
"""

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):

    if not root:
        return 0

    left_depth = max_depth(root.left)

    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)


def run_tests():

    test_cases = []

    # Empty tree
    test_cases.append((None, 0))

    # Single node
    root = TreeNode(1)
    test_cases.append((root, 1))

    # Two levels
    root = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3)
    )
    test_cases.append((root, 2))

    # Three levels
    root = TreeNode(
        3,
        TreeNode(9),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7)
        )
    )
    test_cases.append((root, 3))

    # Left-heavy
    root = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(3)
        )
    )
    test_cases.append((root, 3))

    # Right-heavy
    root = TreeNode(
        1,
        None,
        TreeNode(
            2,
            None,
            TreeNode(3)
        )
    )
    test_cases.append((root, 3))

    # Four levels
    root = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(
                3,
                TreeNode(4)
            )
        )
    )
    test_cases.append((root, 4))

    passed = 0

    for i, (root, expected) in enumerate(test_cases, start=1):

        result = max_depth(root)

        if result == expected:
            print(
                f"✅ Test {i} Passed"
            )
            passed += 1

        else:
            print(
                f"❌ Test {i} Failed | "
                f"Expected={expected} Got={result}"
            )

    print(
        f"\nPassed {passed}/{len(test_cases)} tests"
    )


if __name__ == "__main__":
    run_tests()


"""
Notes:

Tree DFS Template:

def dfs(node):

    if not node:
        return 0

    left = dfs(node.left)
    right = dfs(node.right)

    return ...

Important:
- Base case handles None
- Each node visited once
- O(n) time

"""

"""
My Takeaways:

- Learned DFS recursion
- Base case is critical
- Tree problems often use:
    return 1 + max(left, right)
"""