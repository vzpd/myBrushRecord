import collections
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums)
        temp = list(set(nums))
        temp.sort()
        if temp and temp[-1] < 0:
            return []
        elif temp and temp[-1] == 0:
            return [[0, 0, 0]] if counter[0] > 2 else []
        else:
            res = []
            for i in range(len(temp)):
                if temp[i] >= 0:
                    break
                if counter[temp[i]] > 1:
                    left = -temp[i] * 2
                    if left in counter:
                        res.append([temp[i], temp[i], left])
                for j in range(i + 1, len(temp)):
                    left = -temp[i] - temp[j]
                    if left == temp[j] and counter[temp[j]] > 1:
                        res.append([temp[i], temp[j], temp[j]])
                    elif left > temp[j] and left in counter:
                        res.append([temp[i], temp[j], left])

            if 0 in counter and counter[0] > 2:
                res.append([0, 0, 0])

        return res


s = Solution()
assert s.threeSum([0, 0, 0, 0, 0, 0, ]) == [[0, 0, 0]]
assert s.threeSum([]) == []
assert s.threeSum([0, -4, -1, -4, -2, -3, 2]) == [[-2, 0, 2]]
assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert s.threeSum([-1, 0, 1, 0]) == [[-1, 0, 1]]
assert s.threeSum([1, 1, -2]) == [[-2, 1, 1]]
assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert s.threeSum([1, 0, 1, 0, 1, 0, 1]) == [[0, 0, 0]]
assert s.threeSum([-2, -1, 0, 1]) == [[-1, 0, 1]]
assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
