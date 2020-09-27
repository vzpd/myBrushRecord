import heapq
import sys
from functools import lru_cache
from typing import List

from exercise.myUtils import timer

sys.setrecursionlimit(1000000)


class Solution:
    @timer
    def busRapidTransit(self, target: int, inc: int, dec: int, jump: List[int], cost: List[int]) -> int:
        MOD = 1000000007

        @lru_cache(None)
        def helper(target):
            if target == 0:
                return 0
            if target == 1:
                return inc
            r = target * inc
            for d, c in zip(jump, cost):
                bias = target % d
                r = min(r, bias * inc + c + helper(target // d))
                if bias:
                    r = min(r, (d - bias) * dec + c + helper(target // d + 1))

            return r

        return helper(target) % MOD


class Solution:
    def busRapidTransit(self, target: int, inc: int, dec: int, jump: List[int], cost: List[int]) -> int:
        MOD = 1000000007

        @lru_cache(None)
        def helper(k):
            if k == 0:
                return 0
            if k == 1:
                return inc
            r = k * inc
            for d, c in zip(jump, cost):
                m = k % d
                r = min(r, m * inc + c + helper(k // d))
                if m:
                    r = min(r, (d - m) * dec + c + helper(k // d + 1))

            return r

        return helper(target) % MOD


class Solution:
    def busRapidTransit(self, target: int, inc: int, dec: int, jump: List[int], cost: List[int]) -> int:
        q = [[0, target]]
        vis = set()
        while q:

            spend, cur = heapq.heappop(q)
            if cur in vis:
                continue
            if cur == 0:
                return spend % (10 ** 9 + 7)
            vis.add(cur)
            heapq.heappush(q, [spend + cur * inc, 0])
            for j, c in zip(jump, cost):
                m, y = divmod(cur, j)
                if m not in vis:
                    heapq.heappush(q, [spend + c + y * inc, m])
                if m + 1 not in vis:
                    heapq.heappush(q, [spend + c + dec * (j - y), m + 1])


s = Solution()
assert s.busRapidTransit(target=8, inc=5, dec=3, jump=[6], cost=[10])
assert s.busRapidTransit(target=31, inc=5, dec=3, jump=[6], cost=[10]) == 33
assert s.busRapidTransit(target=612,
                         inc=4,
                         dec=5,
                         jump=[
                             3, 6, 8, 11, 5, 10, 4],
                         cost=[4, 7, 6, 3, 7, 6, 4]) == 26
assert s.busRapidTransit(1000000000,
                         1,
                         1,
                         [2],
                         [1000000]) == 10953125
#
