# Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.isWord = True

    def search(self, word: str) -> bool:
        current = self.root

        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]

        return current.isWord


    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]

        return True


tries = Trie()
tries.insert("apple")
actual1 = tries.search("apple")
print(actual1)
actual2 = tries.search("app")
print(actual2)
actual3 = tries.startsWith("app")
print(actual3)
tries.insert("app")
actual4 = tries.search("app")
print(actual4)


