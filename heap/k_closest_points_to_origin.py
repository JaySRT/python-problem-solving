"""
Problem: K Closest Points to Origin

Pattern:
Heap / Priority Queue

Approach:
Compute distance squared for each point.
Store (distance, point) in a min heap.
Pop k closest points.

Time: O(n log n)

Space: O(n)

Key Insight:
We don't need sqrt().

Compare:

x*x + y*y

instead.

Heap stores:

(distance, point)

so the closest point is always at heap[0].

My Takeaways:
- Tuples in heaps are ordered by the first element.
- Distance squared is enough.
- Heaps are useful for nearest-neighbor style problems.


Optimized Version: 
Keep heap size only k
Time: O(n log k)
Space: O(k)

Approach:
Use a max heap of size k.
Python only has a min heap, so store negative distance.
If heap size exceeds k, pop the farthest point.

Time: O(n log k)
Space: O(k)

Key Insight:
To find k closest, keep only k candidates.
Remove the farthest whenever heap grows too large.

Distance:
x*x + y*y

No sqrt needed.
"""

import heapq

def k_closest(points, k):
    heap = []

    for x,y in points:
        distance = x*x + y*y

        heapq.heappush(heap, (distance, [x, y]))

    result = []

    for _ in range(k):
        distance, point = heapq.heappop(heap)

        result.append(point)

    return result

def k_closest_optimal(points, k):
    heap = []

    for x,y in points:
        distance = -(x*x + y*y)

        heapq.heappush(heap, (distance, [x, y]))

        if len(heap) > k:
            heapq.heappop(heap)

    result = []

    for distance, point in heap:
        result.append(point)

    return result

def is_valid_k_closest(points, k, result):
    if len(result) != k:
        return False

    distances = sorted([x*x + y*y for x, y in points])
    cutoff = distances[k - 1]

    for x, y in result:
        if x*x + y*y > cutoff:
            return False

    return True

def run_tests():
    test_cases = [
    ([[1,3],[-2,2]], 1, [[-2,2]]),

    ([[3,3],[5,-1],[-2,4]], 2,
     [[3,3],[-2,4]]),

    ([[0,1],[1,0]], 1,
     [[0,1]]),

    ([[1,1],[2,2],[3,3]], 2,
     [[1,1],[2,2]]),

    ([[0,0]], 1,
     [[0,0]])
]
    passed = 0

    for i, (points, k, expected) in enumerate(test_cases, start=1):

        result = k_closest_optimal(points,k)

        #if sorted(result) == sorted(expected):
        if is_valid_k_closest(points, k, result):
            print(f"✅ Test {i} Passed | Input={points}")
            passed += 1
        else:
            print(
                f"❌ Test {i} Failed | "
                f"Input={points} | Expected={expected} Got={result}"
            )

            print(f"\nPassed {passed}/{len(test_cases)} tests")


if __name__ == "__main__":
    run_tests()
