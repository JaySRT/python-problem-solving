"""
Problem: Intersection of Two Arrays

Approach: Use Set to reduce comparison checks

Time: O(n + m)

Space: Space: O(m + k) k = size of intersection
"""

def intersection(nums1, nums2):
    if not nums1 or not nums2:
        return []
    nums2 = set(nums2)
    out = set()
    for i in nums1:
        if i in nums2:
            out.add(i)
    
    return list(out)



def run_tests():
    test_cases = [
    ([1,2,2,1], [2,2], [2]),
    ([4,9,5], [9,4,9,8,4], [4,9]),
    ([], [], []),
    ([1,2], [], []),
    ([], [1,2], []),
    ([1], [1], [1]),
    ([1], [2], []),
    ([1,1,1], [1], [1]),
    ([1,2,3], [4,5,6], []),
    ([1,2,3], [3,4,5], [3]),
    ([1,2,3], [1,2,3], [1,2,3]),
    ([100], [100], [100]),
    ]
    passed = 0

    for i, (arg1, arg2, expected) in enumerate(test_cases, start=1):

        result = intersection(arg1, arg2)

        if set(result) == set(expected):
            print(f"✅ Test {i} Passed | "
                    f"Input=({arg1}, {arg2})"
            )
            passed += 1
        else:
            print(f"❌ Test {i} Failed | "
                    f"Input=({arg1}, {arg2}) | "
                    f"Expected={expected} Got={result}"
            )

    print(f"\nPassed {passed}/{len(test_cases)} tests")


if __name__ == "__main__":
    run_tests()