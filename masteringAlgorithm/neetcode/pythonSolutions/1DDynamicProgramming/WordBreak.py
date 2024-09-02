from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:




solution = Solution()
actual1 = solution.wordBreak("neetcode",  ["neet","code"])
print(actual1)

actual2 = solution.wordBreak("applepenapple",  ["apple","pen","ape"])
print(actual2)


actual3= solution.wordBreak("catsincars",  ["cats","cat","sin","in","car"])
print(actual3)