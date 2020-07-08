"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
"""
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def getnext(pre, left, i):
            if i == len(candidates) or left < candidates[i]:
                return
            elif left == candidates[i]:
                ans.append(pre + [candidates[i]])
            else:
                j = 1
                while i + j < len(candidates) and candidates[i] == candidates[i + j]:
                    j += 1
                k = j
                while j >= 0 and left >= candidates[i]:
                    if left == candidates[i] and j != 0:
                        ans.append(pre + [candidates[i]] * (k - j + 1))
                        break
                    getnext(pre + [candidates[i]] * (k - j), left, i + k)
                    j -= 1
                    left -= candidates[i]

        getnext([], target, 0)

        return ans


s = Solution()
assert s.combinationSum2([1], 2) == []
assert s.combinationSum2([1, 1], 2) == [[1, 1]]
assert s.combinationSum2([1, 1], 3) == []
assert s.combinationSum2([1, 1], 4) == []
assert s.combinationSum2([1, 1, 1, 1, 1, 1, 1], 2) == [[1, 1]]
assert s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [
    [2, 6], [1, 7], [1, 2, 5], [1, 1, 6]
]
assert s.combinationSum2([], 1) == []
assert s.combinationSum2([1, 1, 1, 1, 1, 1, 1], 1) == [[1]]
assert s.combinationSum2([1, 1, 1, 1, 1, 1, 1], 9) == []

