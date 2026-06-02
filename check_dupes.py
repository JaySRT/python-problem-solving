# nums = [10, 20, 30, 40]

# print(nums[0])
# print(nums[-1])

# nums.append(50)

# print(nums)

# for num in nums:
#     print(num)

# for i,num in enumerate(nums):
#     print(i,num)


# nums = [1,2,3,1]

def contains_duplicate(nums):
    seen = set()

    if not nums:
        return False

    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
            

    return False


print(contains_duplicate([1,2,3,4]))
print(contains_duplicate([1,2,3,1]))
print(contains_duplicate([]))