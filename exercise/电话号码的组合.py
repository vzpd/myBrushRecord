from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dp = ['']
        for i in [int(i) for i in digits]:
            start = 91 + 3 * i + i // 8
            length = 4 if i == 7 or i == 9 else 3
            temp = []
            for asciiNum in range(start, start + length):
                for com in dp:
                    temp.append(com + chr(asciiNum))
            dp = temp
        return dp if dp != [''] else []


s = Solution()
s.letterCombinations('9')
