"""
Problem: Product of Array Except Self

Approach: 
Build prefix products (left array) and suffix products (right array).
For each index:
answer[i] = left[i] * right[i]

Time: O(n)

Space: O(n)
"""

def product_except_self(nums):
    if not nums:
        return []

    left = [1]
    right = [1]
    answer = []


    for i in range(1,len(nums)):
        left.append(left[-1] * nums[i - 1])
    
    for i in range(len(nums)-2, -1, -1):
        right.append(right[-1] * nums[i + 1])

    right.reverse()

    for i in range(len(nums)):
        answer.append(left[i] * right[i])
    
    return answer
 

def product_except_self_optimal(nums):
    prefix = 1
    answer = [1] * len(nums)
    suffix = 1

    for i in range(len(nums)):
        answer[i] = prefix
        prefix *= nums[i]
    
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


def run_tests():
    test_cases = [
    ([1,2,3,4], [24,12,8,6]),
    ([2,3,4,5], [60,40,30,24]),
    ([1,1,1,1], [1,1,1,1]),
    ([0,1,2,3], [6,0,0,0]),
    ([1,0,3,4], [0,12,0,0]),
    ([5], [1]),
    ([], []),
    ([-1,1,-1,1], [-1,1,-1,1]),
]
    passed = 0

    for i, (nums, expected) in enumerate(test_cases, start=1):

        result = product_except_self_optimal(nums)

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