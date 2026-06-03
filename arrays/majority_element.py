"""
Problem: Majority Element

Approach: Use dictionary to get frequence

Time: O(n)

Space: O(n)
"""

def majority_element(nums):
    if not nums:
        return None
    
    freq = {}
    for i in nums:
        freq[i] = freq.get(i, 0) + 1

    for num, count in freq.items():
        if count > len(nums) // 2:
            return num
 

def run_tests():
    test_cases = [
    ([3,2,3], 3),
    ([2,2,1,1,1,2,2], 2),
    ([1], 1),
    ([5,5], 5),
    ([1,2,1], 1),
    ([9,9,9,1,2], 9),
    ([7,7,7,7], 7),
    ([8,8,1,2,8], 8),
    ([10], 10),
    ([6,6,6,3,3], 6),
]
    passed = 0

    for i, (nums, expected) in enumerate(test_cases, start=1):

        result = majority_element(nums)

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