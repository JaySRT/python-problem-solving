nums = [2,7,11,15]
target = 9

def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        need = target - num

        if need in seen:
            return [seen[need], i]
        else:
            seen[num] = i



print(two_sum(nums, target))

"""
Whenever you see:

Find pair
Find duplicate
Frequency count
Fast lookup
Group items

ask yourself:

Can I use a dictionary?
"""