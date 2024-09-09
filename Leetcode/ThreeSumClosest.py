def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    n = len(nums)
    for i in range(n - 2):
        left_pointer = i + 1
        right_pointer = n-1

        while left_pointer < right_pointer:
            current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]

            if current_sum == target:
                return current_sum

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            elif current_sum < target:
                left_pointer += 1
            else:
                right_pointer -= 1

    return closest_sum




nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))