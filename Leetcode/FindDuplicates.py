# def findDuplicates(nums):
#     dict = {}
#     for number in nums:
#         if number in dict:
#             dict[number] += 1
#         else:
#             dict[number] = 1
#     result = []
#     print(dict)
#     for number in dict:
#         if dict[number] > 1:
#             result.append(number)
#
#     return result
# nums = [1,1,2,2,2,3,4,4,5,6,7]
# print(findDuplicates(nums))

def findDuplicatesUsingSet(nums):
    set1 = set()
    for number in nums:
        if number in set1:
            return True
        else:
            set1.add(number)
    return False

nums = [1,1,2,2,2,3,4,4,5,6,7]
print(findDuplicatesUsingSet(nums))