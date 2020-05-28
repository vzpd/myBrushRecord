class Solution:
    def decodeString(self, s: str) -> str:
        # res = ''
        # nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        # num = ''
        # count = 0
        # index = 0
        # for i in range(len(s)):
        #     chr = s[i]
        #     if chr in nums:
        #         if count == 0:
        #             num += chr
        #     elif chr == '[':
        #         if count == 0:
        #             index = i + 1
        #         count += 1
        #     elif chr == ']':
        #         count -= 1
        #         if count == 0:
        #             res += int(num) * self.decodeString(s[index:i])
        #             num = ''
        #     else:
        #         if count == 0:
        #             res += chr
        #
        # return res
        # nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        # num = ''
        # chrs = ''
        # all = []
        # for i in range(len(s)):
        #     chr = s[i]
        #     if chr in nums:
        #         if chrs:
        #             all.append(chrs)
        #             chrs = ''
        #         num += chr
        #     elif chr == '[':
        #         all.append(num)
        #         num = ''
        #         all.append('[')
        #     elif chr == ']':
        #         while all[-1] != '[':
        #             chrs = all.pop(-1) + chrs
        #         all.pop(-1)
        #         tempnum = all.pop(-1)
        #         all.append(int(tempnum) * chrs)
        #         chrs = ''
        #     else:
        #         chrs += chr
        # all.append(chrs)
        # return ''.join(all)
        nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        all = []
        for i in range(len(s)):
            if s[i] == ']':
                chrs = ''
                while all[-1] != '[':
                    chrs = all.pop(-1) + chrs
                all.pop(-1)
                num = ''
                while all and all[-1] in nums:
                    num = all.pop(-1) + num
                all.append(int(num) * chrs)
            else:
                all.append(s[i])

        return ''.join(all)


s = Solution()

assert s.decodeString("3[a]2[bc]") == "aaabcbc"
assert s.decodeString("3[a2[c]]") == "accaccacc"
assert s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
