def findFirstAndLastPositionOfElementInSortedArray(nums, target):
    left = 0
    right = len(nums)
    mid = right - left//2
    result = []
    while left <= right:

        if nums[mid] == target:
            result.append(mid)
            if nums[mid-1] == target:
                result.append(mid)

        elif nums[mid] < target:





nums = [5, 7, 7, 8, 8, 10]
target = 8
print(findFirstAndLastPositionOfElementInSortedArray(nums, target))