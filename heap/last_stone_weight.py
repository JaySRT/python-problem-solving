"""
Problem: Last Stone Weight

Pattern:
Heap / Priority Queue

Approach:
Use a max heap to repeatedly remove the two largest stones.

Python only provides a min heap,
so store negative values.

Algorithm:
1. Convert stones to negatives.
2. Heapify.
3. Pop two largest stones.
4. If unequal, push back the difference.
5. Repeat until <= 1 stone remains.

Time: O(n log n)

Space: O(n)

Key Insight:
Max Heap in Python:

heap = [-x for x in nums]

largest = -heapq.heappop(heap)

Heap Template:

heapq.heapify(heap)

while heap:

    largest = heapq.heappop(heap)

My Takeaways:
- Python heaps are min heaps.
- Negatives simulate max heaps.
- Heaps are ideal when repeatedly needing the largest or smallest element.

Interview Pattern Recognition

When you hear:
Largest repeatedly
Smallest repeatedly
Top K
Priority
Ranking
Streaming
"""

import heapq


def last_stone_weight(stones):

    heap = [-stone for stone in stones]

    heapq.heapify(heap)

    while len(heap) > 1:

        first = -heapq.heappop(heap)

        second = -heapq.heappop(heap)

        if first != second:
            heapq.heappush(heap,-(first-second))
        
    if heap:
        return -heap[0]
   
    return 0


def run_tests():
    test_cases = [
        ([2,7,4,1,8,1], 1),
        ([1], 1),
        ([1,1], 0),
        ([5,5], 0),
        ([10,4], 6),
        ([3,3,3], 3),
        ([9,3,2,10], 0),
        ([8,7,6], 5),
        ([10,10,10], 10),
        ([], 0),
    ]

    passed = 0

    for i, (stones, expected) in enumerate(test_cases, start=1):
        result = last_stone_weight(stones)

        if result == expected:
            print(f"✅ Test {i} Passed | Input={stones}")
            passed += 1
        else:
            print(
                f"❌ Test {i} Failed | "
                f"Input={stones} | Expected={expected} Got={result}"
            )

    print(f"\nPassed {passed}/{len(test_cases)} tests")


if __name__ == "__main__":
    run_tests()