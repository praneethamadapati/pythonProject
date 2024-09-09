def medianOfSortedArrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    n = len(nums1)
    if n % 2 == 0:
        half = int(n / 2)
        halfMinusOne = half - 1
        median = (nums1[half] + nums1[halfMinusOne])/2
    else:
        half = int((n + 1)/2)
        median = nums1[half-1]

    return median

nums1 = [1, 3]
nums2 = [2]
print(medianOfSortedArrays(nums1, nums2))