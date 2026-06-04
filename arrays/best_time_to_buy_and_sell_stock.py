"""
Problem: Best Time to Buy and Sell Stock

Approach:
Track the minimum price seen so far and calculate max profit at each step.

Time: O(n)
Space: O(1)
"""


def max_profit(prices):
    if not prices:
        return 0
    
    min_price_so_far = prices[0]
    max_profit = 0

    for price in prices:
        min_price_so_far = min(min_price_so_far, price)
        profit = price - min_price_so_far

        max_profit = max(max_profit, profit)


    return max_profit




def run_tests():
    test_cases = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([1,2,3,4,5], 4),
        ([2,4,1], 2),
        ([3,3,3,3], 0),
        ([1], 0),
        ([], 0),
        ([5,1,5], 4),
        ([10,1,2,3,0,5], 5),
        ([2,1,2,1,0,1,2], 2),
    ]

    passed = 0

    for i, (prices, expected) in enumerate(test_cases, start=1):
        result = max_profit(prices)

        if result == expected:
            print(f"✅ Test {i} Passed | Input={prices}")
            passed += 1
        else:
            print(
                f"❌ Test {i} Failed | "
                f"Input={prices} | Expected={expected} Got={result}"
            )

    print(f"\nPassed {passed}/{len(test_cases)} tests")


if __name__ == "__main__":
    run_tests()