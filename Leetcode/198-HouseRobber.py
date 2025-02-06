def houseRobber(nums):
    # maximumMoneyEven = 0
    # maximumMoneyOdd = 0
    # n = len(nums)
    # for i in range(n):
    #     if i % 2 == 1:
    #         maximumMoneyOdd +=nums[i]
    #     elif i % 2 == 0:
    #         maximumMoneyEven += nums[i]
    # if maximumMoneyOdd > maximumMoneyEven:
    #     return maximumMoneyOdd
    # else:
    #     return maximumMoneyEven

    n = len(nums)
    if not nums:
        return 0
    elif n == 1:
        return nums[0]
    elif n == 2:
        return max(nums[0], nums[1])

    result = [0] * n
    result[0] = nums[0]
    result[1] = max(nums[0], nums[1])

    for i in range(2, n):
        result[i] = max(result[i-1], result[i-2] + nums[i])

    return result[-1]

nums = [1, 2, 3, 1]
print(houseRobber(nums))