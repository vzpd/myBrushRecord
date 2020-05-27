import collections
from typing import List

from exercise.myUtils import count_time


class Solution:
    @count_time
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        # count = 0
        # for i in range(len(A)):
        #     temp = 0
        #     for j in range(i, len(A)):
        #         temp += A[j]
        #         if temp % K == 0:
        #             count += 1
        # return count
        # 同余定理：两个数对K的余数相同，则差值为K的倍数
        # 所有我们这里求出所有前缀和，并求余
        # 找出之前相同余数的数量，加到总数上即可
        A = [0] + A
        dict = collections.defaultdict(int)
        dict[0] = 1
        temp = 0
        count = 0
        for i in range(1, len(A)):
            temp = (temp + A[i]) % K
            count += dict[temp]
            dict[temp] += 1
        return count


s = Solution()
assert s.subarraysDivByK([4, 5], 5) == 1
assert s.subarraysDivByK([5], 5) == 1
assert s.subarraysDivByK([2, 2], 4) == 1
assert s.subarraysDivByK(A=[4, 5, 0, -2, -3, 1], K=5) == 7
