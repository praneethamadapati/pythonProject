def intersection(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            if arr1[i] not in result:
                result.append(arr1[i])
    return result

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1, nums2))

