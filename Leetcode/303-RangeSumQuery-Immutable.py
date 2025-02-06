class NumArray:

    def __init__(self, nums):
        self.sum = []
        sum_until = 0
        for num in nums:
            sum_until += num
            self.sum.append(sum_until)

    def sumRange(self, left: int, right: int) -> int:

        if left > 0 and right > 0:
            return self.sum[right] - sum[left-1]
        else:
            return self.sum[left or right]

print(NumArray["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]])