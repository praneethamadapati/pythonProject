def containsDuplicate(nums):

    nums_set = set(nums)
    return True if len(nums) != len(nums_set) else False
    # dict = {}
    # for i in nums:
    #     if i in dict:
    #         dict[i] += 1
    #     else:
    #         dict[i] = 1
    # for key, value in dict.items():
    #     if dict[key] > 1:
    #         return True
    # return False

# nums_set = set(nums)
# return False if len(nums_set) == len(nums) else True

nums = [1, 2, 3, 1]
print(containsDuplicate(nums))
