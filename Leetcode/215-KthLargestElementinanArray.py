import heapq
from heapq import heapify


def kthLargestElementInAnArray(nums, k):
    array = []
    for number in nums:
        heapq.heappush(array, number)
        if len(array) > k:
            heapq.heappop(array)
    return array[0]

nums = [3, 2, 1, 5, 6, 4]
k = 2
print(kthLargestElementInAnArray(nums, k))