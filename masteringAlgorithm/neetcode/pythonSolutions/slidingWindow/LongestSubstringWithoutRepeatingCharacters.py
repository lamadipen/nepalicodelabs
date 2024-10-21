#Longest Substring Without Repeating Characters
#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    # O(n^2) and space complexity O(n)
    def lengthOfLongestSubstringBruteForce(self, s: str) -> int:
        maxLength =0
        for left in range(len(s)):
            visited = set()
            for right in range(left, len(s)):
                if s[right] in visited:
                    break
                visited.add(s[right])
                maxLength = max(maxLength, right - left +1)
        return maxLength

    # Runtime O(n) and space complexity O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        maxLength = 0
        left =0

        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left+=1
            visited.add(s[right])
            maxLength = max(maxLength,right- left +1)

        return maxLength





solution = Solution()
actual1 = solution.lengthOfLongestSubstringBruteForce('abcabcbb');
print(actual1)
print(actual1 == 3)

actual2 = solution.lengthOfLongestSubstringBruteForce('bbbbb');
print(actual2)
print(actual2 ==1)

actual3 = solution.lengthOfLongestSubstring('pwwkew');
print(actual3)
print(actual3 ==3)

actual1 = solution.lengthOfLongestSubstring('abcabcbb');
print(actual1)
print(actual1 == 3)

actual2 = solution.lengthOfLongestSubstring('bbbbb');
print(actual2)
print(actual2 ==1)

actual3 = solution.lengthOfLongestSubstring('pwwkew');
print(actual3)
print(actual3 ==3)