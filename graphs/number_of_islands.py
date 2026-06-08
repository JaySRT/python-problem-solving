"""
Problem: Number of Islands

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

def number_of_islands(grid):

    if not grid:
        return 0

    rows = len(grid)

    cols = len(grid[0])

    def dfs(r, c):

        if (r < 0 or c < 0 or r >= rows or c >= cols):
            return
        
        if grid[r][c] == "0":
            return 
        
        grid[r][c] = "0"

        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)

    return count



#################### TESTING ####################
def copy_grid(grid):
    return [row[:] for row in grid]


def run_tests():
    test_cases = [
        (
            [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"],
            ],
            3,
        ),
        (
            [
                ["1","1","1"],
                ["0","1","0"],
                ["1","1","1"],
            ],
            1,
        ),
        (
            [
                ["0","0","0"],
                ["0","0","0"],
            ],
            0,
        ),
        (
            [["1"]],
            1,
        ),
        (
            [["0"]],
            0,
        ),
        (
            [],
            0,
        ),
        (
            [
                ["1","0","1","0","1"],
            ],
            3,
        ),
        (
            [
                ["1"],
                ["0"],
                ["1"],
                ["1"],
            ],
            2,
        ),
    ]

    passed = 0

    for i, (grid, expected) in enumerate(test_cases, start=1):
        result = number_of_islands(copy_grid(grid))

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