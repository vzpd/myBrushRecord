class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        for i in range(len(s)):
            chr = s[i]
            if chr in {'{', '[', '('}:
                temp.append(chr)
            else:
                if not temp:
                    return False
                elif chr == '}':
                    if temp.pop(-1) != '{':
                        return False
                elif chr == ')':
                    if temp.pop(-1) != '(':
                        return False
                else:
                    if temp.pop(-1) != '[':
                        return False
        return False if temp else True


s = Solution()
assert s.isValid(']') is False
assert s.isValid('([)]') is False
assert s.isValid('{[]}') is True
assert s.isValid('()[]{}') is True
