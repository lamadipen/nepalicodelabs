# Word Search II
# https://leetcode.com/problems/word-search-ii/description/
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def add(self, word: str):
        current = self
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:



solution = Solution()
actual1 = solution.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                             ["oath", "pea", "eat", "rain"])
print(actual1 == ["oath", "eat"])
actual2 = solution.findWords([["a", "b"], ["c", "d"]], ["abcb"])
print(actual2 == [])
