# def searchInRotatedSortedArray(nums, target):
#     left = 0
#     right = len(nums) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] >= nums[left]:
#             if nums[left] <= target <= nums[mid]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         else:
#             if nums[mid] <= target <= nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#     return -1

# def searchInRotatedSortedArray(nums, target):
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         # mid = left + (right - left ) // 2
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] >= nums[left]:
#             if nums[left] <= target <= nums[mid]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         else:
#             if nums[mid] <= target <= nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#     return -1

def searchInRotatedSortedArray(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(searchInRotatedSortedArray(nums, target))

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
