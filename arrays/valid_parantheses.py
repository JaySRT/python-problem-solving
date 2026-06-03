"""
Problem: Valid Parentheses

Approach:

Time:

Space:
"""

def valid_parentheses(s):

    stack = []

    pairs = {")" : "(", "]" : "[" , "}" : "{"}

    for i in range(0,len(s)):
        if s[i] not in pairs:
            stack.append(s[i])
        else: 
            if not stack:
                return False
            
            if stack[-1] != pairs[s[i]]:
                return False
            
            stack.pop()
    
    return stack == []

   
 

def run_tests():
    test_cases = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("", True),
    ("(", False),
    (")", False),
    ("((()))", True),
    ("((())", False),
    ("(()))", False),
    ("[[[[]]]]", True),
    ("{[()]}", True),
    ("{[(])}", False),
    ]

    passed = 0

    for i, (nums, expected) in enumerate(test_cases, start=1):

        result = valid_parentheses(nums)

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