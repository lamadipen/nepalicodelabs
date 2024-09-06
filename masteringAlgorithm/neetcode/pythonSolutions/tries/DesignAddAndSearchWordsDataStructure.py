# Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.isWord = True
    def search(self, word: str) -> bool:
        def dfs(index, node):
            current = node
            for i in range(index,len(word)):
                c = word[i]
                if c == '.':
                   for child in current.children:
                       if dfs(i + 1, child):
                           return True
                   return False
                else:
                    if c not in current.children:
                        return False
                    current = current.children[c]
            return current.isWord

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
wordDictionary.addWord("bad")
actual1 = wordDictionary.search("pad") # return False
print(actual1)
actaul2 = wordDictionary.search("bad") # return True
print(actaul2)
actaul3 = wordDictionary.search(".ad") # return True
print((actaul3))
actual4 = wordDictionary.search("b..") # return True
print(actual4)