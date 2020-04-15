# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        numsLen, dp = len(nums), []
        for i in range(numsLen - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            temp0, numsDict, tempdp = target - nums[i], {}, []
            for x in nums[i + 1:]:
                if numsDict.get(x):
                    numsDict[x] += 1
                else:
                    numsDict[x] = 1
                    tempdp.append(x)
            for x in tempdp:
                if numsDict.get(x) > 2 or (numsDict.get(x) == 2 and temp0 - x * 2 != x):
                    if numsDict.get(temp0 - x * 2):
                        dp.append([nums[i], x, x, temp0 - x * 2])

            for k in range(len(tempdp)):
                m, n = k + 1, len(tempdp) - 1
                temp1 = temp0 - tempdp[k]
                while m < n:
                    if tempdp[m] + tempdp[n] == temp1:
                        dp.append([nums[i], tempdp[k], tempdp[m], tempdp[n]])
                        m += 1
                        n -= 1
                    elif tempdp[m] + tempdp[n] < temp1:
                        m += 1
                    else:
                        n -= 1
        return dp


# (l-3)*
s = Solution()
assert s.fourSum([1, 1, 1, 1, 1, 1, 1, 1, 1], 4) == [[1, 1, 1, 1]]
assert s.fourSum([1, 0, -1, 0, -2, 2], 0) == [[-2, 0, 0, 2], [-2, -1, 1, 2], [-1, 0, 0, 1]]
assert s.fourSum([0, 1, 5, 0, 1, 5, 5, -4], 11) == [[-4, 5, 5, 5], [0, 5, 5, 1]]
assert s.fourSum([2, 0, 3, 0, 1, 2, 4], 7) == [[0, 2, 2, 3], [0, 0, 3, 4], [0, 1, 2, 4]]
