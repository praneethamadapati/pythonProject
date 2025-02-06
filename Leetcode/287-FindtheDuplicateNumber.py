def findTheDuplicateNumber(nums):

    for i in range(len(nums)):
        number = abs(nums[i])
        if nums[number] < 0:
            return number
        nums[number] = -nums[number]
    return -1
nums = [1, 3, 4, 2, 2]
print(findTheDuplicateNumber(nums))