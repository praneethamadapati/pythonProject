def productOfArrayExceptSelf(nums):
    # result = []
    # maximumProduct = 1
    # for number in nums:
    #     maximumProduct = maximumProduct * number
    # for number in nums:
    #     product = maximumProduct//number
    #     result.append(product)


    # n = len(nums)
    # result = [1] * n
    # left = 1
    # for i in range(n):
    #     result[i] = left
    #     print(f'result[i]=', result[i])
    #     left *= nums[i]
    #     print(f'left=', left, 'nums[i]=', nums[i])
    # print(f'result=', result)
    # right = 1
    # for i in range(n - 1, -1, -1):
    #     result[i] *= right
    #     print(f'result[i]=', result[i])
    #     right *= nums[i]
    #     print(f'right=', right, 'nums[i]=', nums[i])
    # print(f'result=', result)


    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    result = [1] * n
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    for i in range(n):
        result[i] = left_products[i] * right_products[i]
    return result

nums = [1, 2, 3, 4]
print(productOfArrayExceptSelf(nums))