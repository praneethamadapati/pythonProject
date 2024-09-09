def intersectionOfTwoArraysII(nums1, nums2):
    # if len(nums1) > len(nums2):
    #     nums1, nums2 == nums2, nums1
    #
    # print(f'nums1: {nums1}, nums2: {nums2}')
    result = []
    dictionary = {}
    for number in nums1:
        if number in dictionary:
            dictionary[number] += 1
        else:
            dictionary[number] = 1
    for number in nums2:
        print(dictionary[number])
        if number in dictionary and dictionary[number] > 0:
            result.append(number)
            dictionary[number] -= 1
        else:
            continue
    return result

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersectionOfTwoArraysII(nums1, nums2))