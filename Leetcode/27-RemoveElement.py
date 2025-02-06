class Solution:
    def removeElement(self, nums, val):
        for number in nums:
            if number == val:
                nums.pop(val)

        return nums, len(nums)


nums = [3,2,2,3]
val = 3
print(Solution.removeElement(nums, val))