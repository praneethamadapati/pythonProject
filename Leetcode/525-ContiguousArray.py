def contiguousArray(nums):
    dict = {0: -1}
    count = 0
    max_length = 0

    for index, number in enumerate(nums):
        if number == 1:
            count += 1
        else:
            count -= 1

        if count in dict:
            max_length = max(max_length, index - dict[count])
        else:
            dict[count] = index
    return max_length

nums = [0, 1, 0, 0, 1, 1, 0]
print(contiguousArray(nums))