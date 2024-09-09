def threeSum(nums):
    n = len(nums)
    result = []
    nums.sort()

    for i in range(0, n - 1):
        if i > 0 and nums[i] == nums[i - 1]:
            continue


        j = i + 1
        k = n - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                result.append([nums[i], nums[j], nums[k]])
                j += 1

                # while nums[j] == nums[j - 1] and j < k:
                #     j += 1
    return result


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
