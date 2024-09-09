# def romanNumerals(s):
#     roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     sum = 0
#     for index in range(len(s)):
#         if index < len(s) - 1 and roman_numerals[s[index]] < roman_numerals[s[index + 1]]:
#             sum -= roman_numerals[s[index]]
#         else:
#             sum += roman_numerals[s[index]]
#     return sum
# s = "III"
# print(romanNumerals(s))

# def longestCommonPrefix(strs):
#     prefix = strs[0]
#     for string in strs[1:]:
#         while not string.startswith(prefix):
#             prefix = prefix[:-1]
#     if not prefix:
#         print('No prefix found')
#     return prefix
#
# strs = ["flower", "ow", "flight"]
# print(longestCommonPrefix(strs))

# def validParenthesis(s):
#     characters = {')': '(', '}': '{', ']': '['}
#     result = []
#     for character in s:
#         if character in characters:
#             valid_parenthesis = result.pop() if result else '#'
#             if valid_parenthesis != characters[character]:
#                 return False
#         else:
#             result.append(character)
#     return not result
#
# s = "()[]{}"
# print(validParenthesis(s))

# def removeDuplicates(nums):
#     if not nums:
#         return 0
#
#     result = 1
#     for index in range(1, len(nums)):
#         if nums[index] != nums[index-1]:
#             nums[result] = nums[index]
#             result += 1
#
#     print(nums)
#     return result
#
# nums = [0,0,1,1,1,2,2,3,3,4]
# print(removeDuplicates(nums))

# def indexOfFirstOccurenceInStrinf(haystack, needle):
#     haystack_length = len(haystack)
#     needle_length = len(needle)
#     for index in range(haystack_length-needle_length+1):
#         if haystack[index:index+needle_length] == needle:
#             return index
#     return 'Not found'
#
# haystack = 'sadbutsad'
# needle = 'sad'
# print(indexOfFirstOccurenceInStrinf(haystack, needle))

# def plusOne(digits):


# sum = 0
# count = 1
# for number in digits:
#     sum += number
#     if count < len(digits):
#         sum *= 10
#     count += 1
# sum = sum + 1
# result = []
# for digit in str(sum):
#     result.append(int(digit))
# return result
#     for i in range(len(digits)-1,-1,-1):
#         digits[i] += 1
#         if digits[i] < 10:
#             return digits
#         digits[i] = 0
#         print(digits)
#     digits = [1] + digits
#     return digits
#
# digits = [1, 7, 9]
# print(plusOne(digits))

# def squareRoot(x):
#     if x < 4:
#         return 1 if x else 0
#
#     start, end = 2, x
#     squared = mid = 0
#     while start <= end:
#         mid = (start + end) // 2
#         squared = mid * mid
#
#         if squared == x:
#             return mid
#         elif squared > x:
#             end = mid - 1
#         else:
#             start = mid + 1
#
#     return mid - 1 if squared > x else mid
#
# x = 81
# print(squareRoot(x))

# def climbingStairs(n):
#     stairs = [0] * (n + 1)
#     stairs[0] = 1
#     stairs[1] = 1
#     for i in range(2, n + 1):
#         stairs[i] = stairs[i - 1] + stairs[i - 2]
#     return stairs[n]
#
# n = 5
# print(climbingStairs(n))

# def mergeSortedArray(nums1, nums2, m, n):
#     i = m - 1
#     j = n - 1
#     k = m - n - 1
#
#     while j >= 0:
#         if nums1[i] <= nums2[j]:
#             nums1[k] = nums2[j]
#             j -= 1
#         else:
#             nums1[k] = nums1[i]
#             i -= 1
#         k -= 1
#
#     return nums1
#
# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3
# print(mergeSortedArray(nums1, nums2, m, n))

# def pascalsTriangle(numRows):
#     if numRows == 0:
#         return []
#
#     first_row = [[1]]
#
#     for i in range(1, numRows):
#         row = [1]
#         previous_row = first_row[i - 1]
#         for j in range(1, i):
#             row.append(previous_row[j - 1] + previous_row[j])
#         row.append(1)
#         first_row.append(row)
#     return first_row
#
# numRows = 3
# print(pascalsTriangle(numRows))

# def bestTimeToBuyAndSell(prices):
#     min_price = float('inf')
#     max_profit = 0
#     for price in prices:
#         if price < min_price:
#             min_price = price
#         profit = price - min_price
#         if profit > max_profit:
#             max_profit = profit
#
#     return max_profit
#
# prices = [7, 1, 5, 3, 6, 4]
# print(bestTimeToBuyAndSell(prices))

# def validPalindrome(s):
#     s = ''.join(char.lower() for char in s if char.isalnum())
#     return s == s[::-1]
#
# s = "A man, a plan, a canal: Panama"
# print(validPalindrome(s))

# def singleNumber(nums):
#     dict = {}
#     for num in nums:
#         if num in dict:
#             dict[num] += 1
#         else:
#             dict[num] = 1
#
#     for key, value in dict.items():
#         if value == 1:
#             return key
#
# nums = [2, 2, 1]
# print(singleNumber(nums))

# def majorityElement(nums):
#     dict = {}
#     for num in nums:
#         if num in dict:
#             dict[num] += 1
#         else:
#             dict[num] = 1
#     number = 0
#     number_occurence = 0
#     for key, value in dict.items():
#         if value > number_occurence:
#             number_occurence = value
#             number = key
#         return number
#
# nums = [2,2,1,1,1,2,2]
# print(majorityElement(nums))

# def excelSheetColumnNumber(columnTitle):
#     columnNumber = 0
#     for char in columnTitle:
#         columnNumber = (columnNumber * 26) + (ord(char) - 64)
#     return columnNumber
#
# columnTitle = "ZY"
# print(excelSheetColumnNumber(columnTitle))

# def reverseBits(n):
#     binaryNumber = bin(n)[2:]
#     binaryNumber = binaryNumber.zfill(32)
#     reverseBinaryNumber = binaryNumber[::-1]
#     reverseBinaryNumber = int(reverseBinaryNumber, 2)
#     return reverseBinaryNumber
#
# n = 0b00000010100101000001111010011100
# print(reverseBits(n))

# def numberOfOneBits(n):
#     n = str(bin(n))
#     print(n)
#     count = n.count('1')
#     return count
#
# n = 11
# print(numberOfOneBits(n))

# def happyNumber(n):
#
#     count = 1
#     while count <= 10:
#         result = numberToArray(n)
#         print(result)
#         happyNumber = numberSquare(result)
#         print(happyNumber)
#         count += 1
#         if happyNumber == 1:
#             return True
#         n = happyNumber
#     return False
#
# def numberToArray(n):
#     result = []
#     while n > 0:
#         result.append(n % 10)
#         n = n // 10
#     return result
#
# def numberSquare(arr):
#     result = 0
#     for number in arr:
#         result += number * number
#     return result
#
# n = 19
# print(happyNumber(n))

# def containsDuplicate(nums):
#     nums_set = set(nums)
#     return False if len(nums) == len(nums_set) else True
#
# nums = [1, 2, 3, 1]
# print(containsDuplicate(nums))

# def validAnagram(s, t):
#     dict_s = {}
#     dict_t = {}
#     for char in s:
#         if char in dict_s:
#             dict_s[char] += 1
#         else:
#             dict_s[char] = 1
#     for char in t:
#         if char in dict_t:
#             dict_t[char] += 1
#         else:
#             dict_t[char] = 1
#     return dict_s == dict_t
#
# s = "anagram"
# t = "nagaram"
# print(validAnagram(s, t))

# def missingNumber(nums):
#     result = len(nums)
#     for i in range(len(nums)):
#         result += (i - nums[i])
#     return result
#
# nums = [3, 0, 1]
# print(missingNumber(nums))

# def moveZeros(nums):
#
#     j = 0
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[i], nums[j] = nums[j], nums[i]
#             j += 1
#     return nums
#
# nums = [0, 1, 0, 3, 12]
# print(moveZeros(nums))

# def powerOfThree(n):
#     if n <= 0:
#         return False
#
#     while n:
#         if n == 1:
#             return True
#         elif n % 3 != 0:
#             return False
#         else:
#             n = n/3
#
# n = 27
# print(powerOfThree(n))

# def reverseString(s):
#     return s[::-1]
#
# s = ["h", "e", "l", "l", "o"]
# print(reverseString(s))

# def intersectionOfTwoArraysII(nums1, nums2):
#     dict_nums1 = {}
#     result = []
#     for number in nums1:
#         if number in dict_nums1:
#             dict_nums1[number] += 1
#         else:
#             dict_nums1[number] = 1
#     for number in nums2:
#         if number in dict_nums1 and dict_nums1[number] > 0:
#             result.append(number)
#             dict_nums1[number] -= 1
#         else:
#             continue
#     return result
#
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
# print(intersectionOfTwoArraysII(nums1, nums2))

# def firstUniqueCharacterInString(s):
#     dict_s = {}
#     for character in s:
#         if character in dict_s:
#             dict_s[character] += 1
#         else:
#             dict_s[character] = 1
#     for key, value in dict_s.items():
#         if dict_s[key] == 1:
#             return key
#     return -1
#
# s = "aabb"
# print(firstUniqueCharacterInString(s))

# def fizzBuzz(n):
#     result = []
#     for i in range(1, n+1):
#         if i % 5 == 0 and i % 3 == 0:
#             result.append('FizzBuzz')
#         elif i % 3 == 0:
#             result.append('Fizz')
#         elif i % 5 == 0:
#             result.append('Buzz')
#         else:
#             result.append(i)
#     return result
# n = 5
# print(fizzBuzz(n))

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# def mergeSortedArrays(list1: [ListNode], list2: [ListNode]):
#     head_node1 = ListNode(list1[0])
#     current = head_node1
#     for i in range(1, len(list1)):
#         current.next = ListNode(list1[i])
#         current = current.next
#     print(list1)
#     head_node2 = ListNode(list2[0])
#     current = head_node2
#     for i in range(1, len(list2)):
#         current.next = ListNode(list2[i])
#         current = current.next
#     print(list2)
#
#     while list1 and list2:
#         if list1.val < list2.val:
#             current.next = list1.val
#             list1 = list1.next
#         else:
#             current.next = list2.val
#             list2 = list2.next
#         current = current.next
#
#         if list1 is not None:
#             current.next = list1.val
#         else:
#             current.next = list2.val
#     return head_node1.next
#
# list1 = [1, 2, 4]
# list2 = [1, 3, 4]
# print(mergeSortedArrays(list1, list2))

def reverseLinkedList(head:[ListNode]):
    head_node = ListNode(head[0])
    current = head_node
    for number in head[1:]:
        current.next = ListNode(number)
        current = current.next
    print(head)

    prev = None
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    print(prev)
    return prev


head = [1, 2, 3, 4, 5]
print(reverseLinkedList(head))