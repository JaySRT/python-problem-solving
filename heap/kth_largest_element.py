"""
Problem: Kth Largest Element

Approach: Use heap to get the kth largest from a list

Time: O(n log k)

Space: O(k)
"""
import heapq

def kth_largest(nums,k):
    if not nums:
        return None
    
    heap = []
    for i in nums:
        heapq.heappush(heap,i)

        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]



def run_tests():
    test_cases = [
    ([3,2,1,5,6,4], 2, 5),
    ([3,2,3,1,2,4,5,5,6], 4, 4),
    ([1], 1, 1),
    ([2,1], 1, 2),
    ([2,1], 2, 1),
    ([7,6,5,4,3,2,1], 3, 5),
    ([5,5,5,5], 2, 5),
    ([-1,-2,-3], 2, -2),
]
    passed = 0

    for i, (nums, k, expected) in enumerate(test_cases, start=1):

        result = kth_largest(nums,k)

        if result == expected:
            print(
                f"✅ Test {i} Passed | "
                f"Input={nums}"
            )
            passed += 1

        else:
            print(
                f"❌ Test {i} Failed | "
                f"Input={nums} | "
                f"Expected={expected} Got={result}"
            )

    print(f"\nPassed {passed}/{len(test_cases)} tests")


if __name__ == "__main__":
    run_tests()