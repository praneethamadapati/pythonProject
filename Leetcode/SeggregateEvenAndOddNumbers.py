def seggregateEvenAndOddNumbers(nums):
    left = 0
    right = len(nums)-1
    while left < right:
        while nums[left] % 2 == 0 and left < right:
            left += 1
        while nums[right] % 2 == 1 and left < right:
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
    return nums

    # Method-1
    # nums[:] = [number for number in nums if number % 2 == 0] + [number for number in nums if number % 2 != 0]
    # return nums


nums = [1,2,3,4]
print(seggregateEvenAndOddNumbers(nums))