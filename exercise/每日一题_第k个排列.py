from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        nums = [str(i) for i in range(1, n + 1)]
        temp = [1]

        for i in range(2, n):
            temp.append(temp[-1] * i)

        ans = []

        while k > 0:
            num = temp.pop(-1)
            t = k // num
            ans.append(nums.pop(t))
            k -= t * num
        ans += nums
        return ''.join(ans)


s = Solution()
assert s.getPermutation(3, 3) == '213'
assert s.getPermutation(4, 9) == '2314'
assert s.getPermutation(1,1) == '1'
