def majorityElement(nums):

    dict = {}
    for number in nums:
        if number in dict:
            dict[number] += 1
        else:
            dict[number] = 1
    majority_element_number = 0
    majority_element = 0
    for key, value in dict.items():
        if value > majority_element_number:
            majority_element_number = value
            majority_element = key
    return majority_element

nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))