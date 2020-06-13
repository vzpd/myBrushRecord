class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False
        # else:
        #     nums = []
        #     temp = 1
        #     while x >= temp:
        #         r = x // temp
        #         temp *= 10
        #         nums.append(r % 10)
        #     l, r = 0, len(nums) - 1
        #     while l < r:
        #         if nums[l] != nums[r]:
        #             return False
        #         else:
        #             l += 1
        #             r -= 1
        #     return True
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversex = 0
        while reversex < x:
            reversex = reversex * 10 + x % 10
            x //= 10
        return reversex == x or reversex // 10 == x


s = Solution()
assert s.isPalindrome(10) is False
assert s.isPalindrome(10001) is True
assert s.isPalindrome(101) is True
assert s.isPalindrome(121) is True
assert s.isPalindrome(-121) is False
