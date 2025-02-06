import heapq
from heapq import heapify


def topKFrequentElements(nums, k):
    dict = {}
    for number in nums:
        if number in dict:
            dict[number] += 1
        else:
            dict[number] = 1

    largest_number = heapq.nlargest(k, dict.items(), key=lambda x:x[1])
    # sorted_dict = sorted(dict.items(), key=lambda x:x[1])
    print(largest_number[1][0])

nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequentElements(nums, k))