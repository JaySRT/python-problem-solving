"""
Problem: Longest Substring Without Repeating Characters

Approach: 

Time: 

Space: 
"""

def longest_substring(s):
    
    left = 0
    seen = set()

    max_len = 0

    for right in range(len(s)):

        while s[right] in seen:
            print(f"Removing {s[left]}")
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        current_len = right - left + 1

        max_len = max(max_len, current_len)


        # print(f"Window: {s[left:right + 1]}")
        # # print(seen)
    return max_len
        
 
# longest_substring("abba")


def run_tests():
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("a", 1),
        ("au", 2),
        ("dvdf", 3),
        ("abba", 2),
        ("abcdef", 6),
        ("tmmzuxt", 5),
    ]
    passed = 0

    for i, (nums, expected) in enumerate(test_cases, start=1):

        result = longest_substring(nums)

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