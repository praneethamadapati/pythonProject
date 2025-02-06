def subarraySumEqualsK(nums, k):
    dict = {0: 1}
    count = 0
    current_sum = 0

    for number in nums:
        current_sum += number
        required_sum = current_sum - k
        if required_sum in dict:
            count += dict[required_sum]

        if current_sum in dict:
            dict[current_sum] += 1
        else:
            dict[current_sum] = 1
    return count

nums = [1, 1, 1]
k = 2
print(subarraySumEqualsK(nums, k))