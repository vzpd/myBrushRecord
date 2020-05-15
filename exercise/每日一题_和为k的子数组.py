# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
#
# 示例 1 :
#
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
# 说明 :
#
# 数组的长度为 [1, 20,000]。
# 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        dict = {0: [1]}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            pre = sum - k
            if pre in dict:
                count += len(dict.get(pre))
            if sum in dict:
                dict[sum].append(i)
            else:
                dict[sum] = [i]
        return count


s = Solution()
assert s.subarraySum([-1, -1, 1], 0) == 1
assert s.subarraySum([1, 2, 3, 4, 5, 6], 9) == 2
assert s.subarraySum([1, 1, 1], 2) == 2
assert s.subarraySum([1, 1, 1], 1) == 3
assert s.subarraySum([2, 3, 4], 1) == 0
assert s.subarraySum([1, 2, 3, 4, 5, 6], 22) == 0
