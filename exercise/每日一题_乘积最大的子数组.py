from typing import List


# 本题为动态规划类型
# 每一步执行之后，结果可以划为2类，大于等于0 或者小于0，
# 也就是2个状态，每一步的结果都在着2个状态直接转换
# 执行第i步的时候，如果num[i]为负数，结果就有可能反转
# 需要2个变量存储每一步的结果
# 每一步计算完成之后与maxValue比较，最后得出最大值
# 时间复杂度为O(n)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        a, b = nums[0], nums[0]
        maxValue = nums[0]
        for i in range(1, len(nums)):
            # tempA = a
            # if nums[i] > 0:
            #     a = max(a, 1) * nums[i]
            #     b = min(b, 1) * nums[i]
            # else:
            #     a = max(b * nums[i], nums[i])
            #     b = min(tempA * nums[i], nums[i])
            # 上面注释部分可以优化为下面形式
            if nums[i] <= 0:
                a, b = b, a
            a, b = max(a * nums[i], nums[i]), min(b * nums[i], nums[i])

            maxValue = max(maxValue, a, b)
        print(maxValue)
        return maxValue


s = Solution()
assert s.maxProduct([-1, 1, 2, 0, -1, 3, 4, 5, -2, 0]) == 120
assert s.maxProduct([2, -1, 1, 1]) == 2
assert s.maxProduct([-2]) == -2
assert s.maxProduct([2, 3, -2, 4]) == 6
assert s.maxProduct([-2, 0, -1]) == 0
assert s.maxProduct([1, 2, 3, 4, 5, 0]) == 120
assert s.maxProduct([-1, 1, 2, 3, 4, 5, 0]) == 120
assert s.maxProduct([-1, 1, 2, 0, 3, 4, 5, 0]) == 60
assert s.maxProduct([-1, 1, 2, 0, -1, 3, 4, 5, 0]) == 60
