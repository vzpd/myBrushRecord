from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.arry = [0]
        for i in range(len(nums)):
            self.arry.append(nums[i] + self.arry[i])

    def sumRange(self, i: int, j: int) -> int:
        print(self.arry)
        return self.arry[j + 1] - self.arry[i]


na = NumArray([-2, 0, 3, -5, 2, -1])
assert na.sumRange(0, 0) == -2
assert na.sumRange(0, 2) == 1
assert na.sumRange(2, 5) == -1
assert na.sumRange(0, 5) == -3
na = NumArray([-1])
assert na.sumRange(0, 0) == -1
