def maximumSubarray(nums):
    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(current_sum, max_sum)
    return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maximumSubarray(nums))