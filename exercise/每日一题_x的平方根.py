class Solution:
    def mySqrt(self, x: int) -> int:
        begin, end = 1, x
        while begin <= end:
            mid = (begin + end) // 2
            sqrt = mid * mid
            if sqrt > x:
                end = mid - 1
            elif sqrt < x:
                begin = mid + 1
            else:
                return mid
        return end


s = Solution()
assert s.mySqrt(6) == 2
assert s.mySqrt(0) == 0
assert s.mySqrt(1) == 1
assert s.mySqrt(4) == 2
assert s.mySqrt(8) == 2
assert s.mySqrt(9) == 3
assert s.mySqrt(10) == 3
assert s.mySqrt(2147395599)
