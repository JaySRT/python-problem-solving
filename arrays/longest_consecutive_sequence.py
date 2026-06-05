"""
Problem: Longest Consecutive Sequence

Approach: Use set to optimize the solution and avoid using sorted

Time: O(n)

Space: O(n)
"""

def longest_cons_seq(nums):
    seen = set(nums)

    current = 0
    length = 0
    result = 0

    for num in seen:
        if (num - 1) not in seen:
            current = num
            length = 1
            
            while current + 1 in seen:
                current += 1
                length += 1
            
            result = max(result, length)
    return result



def run_tests():
    test_cases = [
        ([100,4,200,1,3,2], 4),
        ([0,3,7,2,5,8,4,6,0,1], 9),
        ([1], 1),
        ([], 0),
        ([1,2,0,1], 3),
        ([9,1,4,7,3,-1,0,5,8,-1,6], 7),
        ([10,30,20], 1),
        ([1,2,3,4,5], 5),
    ]
    passed = 0

    for i, (nums, expected) in enumerate(test_cases, start=1):

        result = longest_cons_seq(nums)

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