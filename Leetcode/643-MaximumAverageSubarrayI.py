def maximumAverageSubarray(nums, k):
    maximumAverage = current_sum = sum(nums[:k])
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        maximumAverage = max(maximumAverage, current_sum)

    return maximumAverage/k

nums = [1, 12, -5, -6, 50, 3]
k = 4
print(maximumAverageSubarray(nums, k))