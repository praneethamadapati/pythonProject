def longestIncreasingSubsequence(nums):
    left = 0
    max_length = 0
    for right in range(len(nums) - 1):
        if nums[right + 1] > nums[right]:
            max_length = max(max_length, right - left + 1)

        else:
            left = right

        # max_length = max(max_length, right - left + 1)

    return max_length
nums = [10,9,2,5,3,7,101,18]
print(longestIncreasingSubsequence(nums))