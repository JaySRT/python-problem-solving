"""
Approach: Use dictionary to count frequency.
Frequency Map

Time: O(n)
Space: O(n)
"""

# s = "anagram"
# t = "nagaram"


def valid_anagram(s, t):

    if len(s) != len(t):
        return False
    freq = {}
    
    for i in s:
        # freq[i] = freq.get(i, 0) + 1
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for j in t:
        if j not in freq:
            return False
        else:
            freq[j] -=1
            if freq[j] < 0:
                return False

    return True

# print(valid_anagram("abb", "baa"))

def run_tests():

    test_cases = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),

    ("", "", True),

    ("a", "a", True),
    ("a", "b", False),

    ("ab", "ba", True),

    ("abb", "bab", True),
    ("abb", "baa", False),

    ("listen", "silent", True),
    ("triangle", "integral", True),

    ("hello", "world", False),

    ("abc", "abcc", False),
    ("abc", "", False),
    ("", "abc", False),

    ("x"*10, "x"*10, True)
    ]

    passed = 0

    for i, (arg1, arg2, expected) in enumerate(test_cases, start=1):

        result = valid_anagram(arg1, arg2)

        if result == expected:
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