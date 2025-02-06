from operator import index


def twoSum(nums, target):
    result = {}
    for index, number in enumerate(nums):
        second_number = target - number
        if second_number in result:
            return [index, result[second_number]]
        result[number] = index
    print('Target sum not found')

nums = [2, 7, 11, 15]
target = 9
# print(twoSum(nums, target))


def twoSum1(nums, target):
    for number in nums:
        second_number = target - number
        if second_number in nums:
            return nums.index(number), nums.index(second_number)
        else:
            return 'Numbers with the target sum could not be found'

print(twoSum1(nums, target))






