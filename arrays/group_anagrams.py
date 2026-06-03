"""
Problem: Valid Parentheses

Approach:

Time: O(n * k log k) Sorting costs for k avg word length and n words

Space: O(n * k) Dictionary stores every word:
"""

def group_anagrams(words):

    groups = {}

    for word in words:

        key = "".join(sorted(word))
        
        #groups.setdefault(key, []).append(word)

        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]

    return list(groups.values())
    

   
 

def run_tests():
    test_cases = [
    (
        ["eat","tea","tan","ate","nat","bat"],
        [["eat","tea","ate"], ["tan","nat"], ["bat"]]
    ),
    (
        [""],
        [[""]]
    ),
    (
        ["a"],
        [["a"]]
    ),
    (
        ["abc","cba","bac"],
        [["abc","cba","bac"]]
    ),
    (
        ["abc","def"],
        [["abc"],["def"]]
    ),
    ]

    passed = 0

    for i, (nums, expected) in enumerate(test_cases, start=1):

        result = group_anagrams(nums)

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