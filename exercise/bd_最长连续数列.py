# 给定一个未排序的整数数组，找出最长连续序列的长度。
#
# 要求算法的时间复杂度为 O(n)。
#
# 示例:
#
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsLen = len(nums)

        # def heap(left, rigth):
        #     for i in range(rigth, -1, -1):
        #         if nums[i // 2] < nums[i]:
        #             nums[i // 2], nums[i] = nums[i], nums[i // 2]
        #
        # maxLen = 0
        # currentLen = 0
        # for i in range(numsLen - 1, -1, -1):
        #     heap(0, i)
        #     nums[i], nums[0] = nums[0], nums[i]
        #     if i + 1 == numsLen:
        #         currentLen = 1
        #     elif nums[i] == nums[i + 1]:
        #         continue
        #     elif nums[i] + 1 == nums[i + 1]:
        #         currentLen += 1
        #     else:
        #         maxLen = max(maxLen, currentLen)
        #         currentLen = 1
        # return max(maxLen, currentLen)
        if numsLen==0:
            return 0
        minNum = min(nums)
        maxNum = max(nums)
        dp = [x for x in range(minNum, maxNum + 1)]
        print(dp)
        for x in nums:
            print(x)
            dp[x] += 1
        maxLen = 0
        currentLen = 0
        for x in dp:
            if x == 0:
                maxLen = max(maxLen, currentLen)
                currentLen = 0
            else:
                currentLen += 1
        return max(maxLen,currentLen)


s = Solution()
assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
assert s.longestConsecutive([0, 2, 3, 1, 1, 3, 4, 6]) == 5
assert s.longestConsecutive([0]) == 1
assert s.longestConsecutive([]) == 0
assert s.longestConsecutive([0, -1]) == 2
assert s.longestConsecutive([0, -1, 3, 5, 6, 7]) == 3
