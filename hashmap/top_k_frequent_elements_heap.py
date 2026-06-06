"""
Problem: Top K Frequent Elements using Heap

Approach:
Build a frequency dictionary.
Use a min heap of size k.
Push (frequency, number) into the heap.
If heap size exceeds k, pop the least frequent element.

Time: O(n log k)

Space: O(n)
"""

import heapq

def top_k_freq_elements_heap(nums,k):

    if not nums:
        return []
    
    freq = {}
    for num in nums:
        freq[num] = freq.get(num,0) + 1

    
    heap = []
    
    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)

    result = []

    for count, num in heap:
        result.append(num)

    return result



def is_valid_top_k(nums, k, result):
    if len(result) != k:
        return False

    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    result_freqs = [freq[num] for num in result]

    for num, count in freq.items():
        if num not in result and count > min(result_freqs):
            return False

    return True

def run_tests():

    test_cases = test_cases = [
    ([1,1,1,2,2,3], 2, [1,2]),
    ([1], 1, [1]),
    ([1,2,2,3,3,3], 1, [3]),
    ([4,4,4,6,6,7], 2, [4,6]),
    ([5,5,6,6,7,7,7], 2, [7,5]),
    ([-1,-1,-2,-2,-2,3], 2, [-2,-1]),
    ([1,2,3,4], 2, [1,2]),
]
    passed = 0

    for i, (nums, k, expected) in enumerate(test_cases, start=1):

        result = top_k_freq_elements_heap(nums, k)

        if is_valid_top_k(nums, k, result):
            print(
                f"✅ Test {i} Passed | "
                f"Input={nums}"
            )
            passed += 1

        else:
            print(
                f"❌ Test {i} Failed | "
                f"Input={nums} | "
                f"Expected top {k} frequent Got={result}"
            )

    print(f"\nPassed {passed}/{len(test_cases)} tests")


if __name__ == "__main__":
    run_tests()