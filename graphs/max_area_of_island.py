"""
Problem: Max area of Islands

Pattern:
Graph DFS / Flood Fill

Approach:
Scan every cell.

When land ("1") is found:
- Increment island count
- DFS from that cell
- Mark all connected land as visited

DFS explores:
- Up
- Down
- Left
- Right

Time: O(rows * cols)

Space: O(rows * cols)

Key Insight:
Every island is counted exactly once.
DFS "sinks" the entire island by converting land to water.

DFS Grid Template:

def dfs(r, c):

    if outside_grid:
        return

    if water:
        return

    mark_visited

    dfs(up)
    dfs(down)
    dfs(left)
    dfs(right)

My Takeaways:
- Trees use left/right.
- Grids use up/down/left/right.
- Graph DFS is very similar to tree DFS.
- Mark visited immediately to avoid revisiting.
"""

def max_area_of_island(grid):

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    def dfs(r, c):

        if (r < 0 or c < 0 or r >= rows or c >= cols):
            return 0
        
        if grid[r][c] == 0:
            return 0
        
        grid[r][c] = 0

        # dfs(r - 1, c)
        # dfs(r + 1, c)
        # dfs(r, c - 1)
        # dfs(r, c + 1)

        return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) +dfs(r, c + 1)

    area = 0
    max_area = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                area = dfs(r, c)
                max_area = max(max_area, area)

    
    return max_area



#################### TESTING ####################
def copy_grid(grid):
    return [row[:] for row in grid]


def run_tests():
    test_cases = [
    (
        [
            [0,0,1,0],
            [1,1,1,0],
            [0,0,0,1],
        ],
        4,
    ),
    (
        [
            [1,1,0,0],
            [1,0,0,1],
            [0,0,1,1],
        ],
        3,
    ),
    (
        [
            [0,0,0],
            [0,0,0],
        ],
        0,
    ),
    (
        [[1]],
        1,
    ),
    (
        [[0]],
        0,
    ),
    (
        [],
        0,
    ),
]

    passed = 0

    for i, (grid, expected) in enumerate(test_cases, start=1):
        result = max_area_of_island(copy_grid(grid))

        if result == expected:
            print(f"✅ Test {i} Passed")
            passed += 1
        else:
            print(
                f"❌ Test {i} Failed | "
                f"Expected={expected} Got={result}"
            )

    print(f"\nPassed {passed}/{len(test_cases)} tests")


if __name__ == "__main__":
    run_tests()