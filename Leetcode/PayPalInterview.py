def sortingArray(nums):
    dict = {}
    result = []
    for number in nums:
        if number in dict:
            dict[number] += 1
        else:
            dict[number] = 1

    sorted_dict = sorted(dict.items(), key = lambda item: (item[-1], item[0]))
    for key, value in sorted_dict:
        while value != 0:
            result.append(key)
            value -= 1
    return result

n = 6
items = [4, 5, 6, 5, 4, 3, 3, 4]
Expected = [3, 6, 5, 5, 4, 4, 4]
print(sortingArray(items))