"""
Problem: Binary Tree Level Order Traversal

Pattern:
BFS / Queue

Approach:
Use a queue.
Process nodes level by level.
Use len(queue) to determine how many nodes belong
to the current level.

Time: O(n)

Space: O(n)

Key Insight:
The queue always contains the next nodes to visit.

BFS Template:

q = deque([root])

while q:

    level_size = len(q)

    for _ in range(level_size):

        node = q.popleft()

        ...

My Takeaways:
- DFS goes deep first.
- BFS goes level by level.
- deque is the preferred queue implementation.
- len(queue) helps separate levels.
"""

from collections import deque

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    if not root:
        return []

    q = deque([root])

    result = []

    while q:
        level_size = len(q)
        level = []

        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        result.append(level)
    
    return result

    



test_cases = [
    (None, []),

    (
        TreeNode(1),
        [[1]]
    ),

    (
        TreeNode(
            1,
            TreeNode(2),
            TreeNode(3)
        ),
        [[1], [2, 3]]
    ),

    (
        TreeNode(
            3,
            TreeNode(9),
            TreeNode(
                20,
                TreeNode(15),
                TreeNode(7)
            )
        ),
        [[3], [9, 20], [15, 7]]
    ),

    (
        TreeNode(
            1,
            TreeNode(
                2,
                TreeNode(4)
            ),
            TreeNode(3)
        ),
        [[1], [2, 3], [4]]
    ),
]

def run_tests():

    passed = 0

    for i, (root, expected) in enumerate(test_cases, start=1):

        result = level_order(root)

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