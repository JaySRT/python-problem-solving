"""
Problem: Longest Consecutive Sequence

Approach: Use set to optimize the solution and avoid using sorted

Time: Time: O(n + m log m)

Space: O(m)
"""

def top_k_freq_element(nums,k):
    if not nums:
        return []
    
    freq = {}
    result = []
    
    for num in nums:
        freq[num] = freq.get(num,0) + 1

    sorted_items = sorted(freq.items(),key=lambda x:x[1],reverse=True)

    print(sorted_items)

    for i in range(0,k):
        result.append(sorted_items[i][0])
    
    return result



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

        result = top_k_freq_element(nums,k)

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