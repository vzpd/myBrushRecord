from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # res = [0] * len(T)
        # his = []
        # index = []
        # for i in range(len(T)):
        #     while his and T[i] > his[-1]:
        #         res[index[-1]] = i - index[-1]
        #         his.pop(-1)
        #         index.pop(-1)
        #     his.append(T[i])
        #     index.append(i)
        #
        # return res
        index = []
        for i in range(len(T)):
            while index and T[i] > T[index[-1]]:
                T[index[-1]] = i - index[-1]
                index.pop(-1)
            index.append(i)

        for i in index:
            T[i] = 0

        return T


s = Solution()
assert s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
assert s.dailyTemperatures([1]) == [0]
assert s.dailyTemperatures([10, 9, 8]) == [0, 0, 0]
assert s.dailyTemperatures([3, 2, 1, 4]) == [3, 2, 1, 0]
