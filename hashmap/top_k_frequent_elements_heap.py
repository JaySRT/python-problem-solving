"""
Problem: Longest Consecutive Sequence

Approach: Use set to optimize the solution and avoid using sorted

Time: Time: O(n + m log m)

Space: O(m)
"""

def top_k_freq_elements_heap(nums,k):
    pass



def run_tests():
    test_cases = [
        ([1,1,1,2,2,3], 2, [1,2]),
        ([1], 1, [1]),
        ([1,2,2,3,3,3], 1, [3]),
        ([4,4,4,6,6,7], 2, [4,6]),
        ([5,5,6,6,7,7,7], 2, [7,5]),  # [7,6] also acceptable
        ([-1,-1,-2,-2,-2,3], 2, [-2,-1]),
        ([1,2,3,4], 2, [1,2]),  # any 2 are acceptable
    ]
    passed = 0

    for i, (nums, k, expected) in enumerate(test_cases, start=1):

        result = top_k_freq_elements_heap(nums,k)

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